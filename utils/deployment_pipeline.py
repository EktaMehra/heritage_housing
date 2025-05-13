import pandas as pd
import numpy as np
import joblib
import os

def predict_from_raw(raw_df, model_path, save_output_path=None):
    """
    Run prediction using saved pipeline that includes preprocessing.
    """
    try:
        print("[INFO] Loading model pipeline...")
        model_pipeline = joblib.load(model_path)

        # Optional: validate input columns before prediction
        expected_features = model_pipeline.named_steps["preprocessor"].transformers_[0][2]
        missing = [col for col in expected_features if col not in raw_df.columns]
        if missing:
            raise ValueError(f"[ERROR] Missing expected input features: {missing}")

        print("[INFO] Generating predictions...")
        predictions = model_pipeline.predict(raw_df)

        # Combine predictions with original data
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
