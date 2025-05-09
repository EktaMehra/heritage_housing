# run_pipeline.py

import pandas as pd
from deployment_pipeline import predict_from_raw

# Paths to required files
RAW_DATA_PATH = "data/raw/inherited_houses.csv"
X_TRAIN_PATH = "data/processed/final/X_train.csv"
MODEL_PATH = "outputs/models/final_random_forest_pipeline.pkl"
OUTPUT_PATH = "outputs/predictions/new_data_predictions.csv"

def main():
    print("[INFO] Running inference using deployment pipeline...")

    # Load new data and reference feature structure
    try:
        new_data = pd.read_csv(RAW_DATA_PATH)
        X_train = pd.read_csv(X_TRAIN_PATH)
        print(f"[INFO] Loaded raw input shape: {new_data.shape}")
    except FileNotFoundError as e:
        print(f"[ERROR] Required file missing: {e}")
        return

    # Run prediction
    prediction_df = predict_from_raw(
        raw_df=new_data,
        model_path=MODEL_PATH,
        training_features=X_train,
        save_output_path=OUTPUT_PATH
    )

    print("\n[INFO] Sample predictions:")
    print(prediction_df[["Predicted_LogSalePrice", "Predicted_SalePrice"]].head())

if __name__ == "__main__":
    main()
