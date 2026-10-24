
from pathlib import Path
import joblib
import numpy as np
import pandas as pd

def load_bundle(package_dir=None):
    """Load saved models and metadata from the package directory."""
    package_dir = Path(package_dir or Path(__file__).parent)
    return joblib.load(package_dir / "artifacts.joblib")

def engineer_features(data, raw_columns):
    """Apply the exact feature engineering used during training."""
    missing = [c for c in raw_columns if c not in data.columns]
    if missing:
        raise ValueError(f"Missing required input columns: {missing}")

    d = data.loc[:, raw_columns].copy()

    d["was_contacted_before"] = (d["pdays"] != 999).astype(int)
    d["previous_success"] = (d["poutcome"] == "success").astype(int)
    d["campaign_log"] = np.log1p(d["campaign"])
    d["previous_log"] = np.log1p(d["previous"])

    d["age_group"] = pd.cut(
        d["age"],
        bins=[0, 25, 35, 45, 55, 65, 100],
        labels=["18-25", "26-35", "36-45",
                "46-55", "56-65", "65+"],
        include_lowest=True
    ).astype(str)

    cat = d.select_dtypes(exclude=np.number).columns
    for col in cat:
        d[col] = d[col].fillna("unknown").astype(str)

    return d

def predict_customers(data, bundle):
    """
    Input: raw customer DataFrame.
    Output: subscription probabilities, predictions and cluster IDs.
    """
    features = engineer_features(data, bundle["raw_columns"])

    # Keep the exact feature order used during training.
    model_columns = bundle["model_feature_columns"]
    cluster_columns = bundle["cluster_feature_columns"]

    missing_model = [c for c in model_columns if c not in features.columns]
    missing_cluster = [c for c in cluster_columns if c not in features.columns]

    if missing_model or missing_cluster:
        raise ValueError(
            f"Feature mismatch. Model missing={missing_model}; "
            f"Clustering missing={missing_cluster}"
        )

    model_input = features.loc[:, model_columns]
    cluster_input = features.loc[:, cluster_columns]

    probabilities = bundle["model"].predict_proba(model_input)[:, 1]
    threshold = bundle["threshold"]
    predictions = (probabilities >= threshold).astype(int)

    clusters = bundle["kmeans"].predict(
        bundle["cluster_preprocessor"].transform(cluster_input)
    )

    result = pd.DataFrame(index=data.index)
    result["subscription_probability"] = probabilities
    result["predicted_subscription"] = predictions
    result["customer_cluster"] = clusters

    result["predicted_label"] = np.where(
        predictions == 1, "yes", "no"
    )

    return result
