import pandas as pd
import numpy as np
import joblib
import os

def process_new_properties(raw_df, training_features):
    """
    Clean and align raw data for prediction. Assumes that
    preprocessing and scaling are handled by the saved pipeline.
    """
    try:
        # Step 1: Lowercase categoricals
        categorical_to_lower = ['BsmtExposure', 'BsmtFinType1', 'GarageFinish', 'KitchenQual']
        for col in categorical_to_lower:
            if col in raw_df.columns:
                raw_df[col] = raw_df[col].astype(str).str.lower()

        # Step 2: Feature engineering
        required_cols = ['YearBuilt', 'GrLivArea', 'LotArea', 'BsmtFinSF1', 'TotalBsmtSF', 'OverallQual', 'OverallCond']
        if all(col in raw_df.columns for col in required_cols):
            raw_df["Age"] = 2025 - raw_df["YearBuilt"]
            raw_df["LivingLotRatio"] = raw_df["GrLivArea"] / (raw_df["LotArea"] + 1)
            raw_df["FinishedBsmtRatio"] = raw_df["BsmtFinSF1"] / (raw_df["TotalBsmtSF"] + 1)
            raw_df["OverallScore"] = raw_df["OverallQual"] * raw_df["OverallCond"]
            raw_df.drop(columns=required_cols, inplace=True)

        # Step 3: Prefix columns
        raw_df.columns = [f"num__{col}" for col in raw_df.columns]

        # Step 4: Add missing columns
        for col in training_features.columns:
            if col not in raw_df.columns:
                raw_df[col] = 0
        raw_df = raw_df[training_features.columns]  # Enforce order

        return raw_df

    except Exception as e:
        print(f"[ERROR] Failed during preprocessing: {e}")
        return None

def predict_from_raw(raw_df, model_path, training_features, save_output_path=None):
    """
    Run prediction using saved pipeline.
    """
    try:
        print("[INFO] Preprocessing input data...")
        processed_df = process_new_properties(raw_df, training_features)
        if processed_df is None:
            print("[ERROR] Preprocessing failed. Cannot proceed with prediction.")
            return None

        print("[INFO] Loading model pipeline...")
        model_pipeline = joblib.load(model_path)

        print("[INFO] Generating predictions...")
        predictions = model_pipeline.predict(processed_df)

        raw_df = raw_df.copy()
        raw_df["Predicted_LogSalePrice"] = predictions
        raw_df["Predicted_SalePrice"] = np.expm1(predictions)

        if save_output_path:
            os.makedirs(os.path.dirname(save_output_path), exist_ok=True)
            raw_df.to_csv(save_output_path, index=False)
            print(f"[INFO] Predictions saved to: {save_output_path}")

        return raw_df

    except Exception as e:
        print(f"[ERROR] Prediction pipeline failed: {e}")
        return None
