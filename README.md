# Bank Marketing ML Package

## Contents
- artifacts.joblib: trained CatBoost and KMeans objects.
- inference.py: feature engineering, prediction and segmentation.
- metadata.json: model metrics and library versions.
- requirements.txt: matching Python dependency versions.

## Quick start
Keep inference.py and artifacts.joblib in the same directory.

```python
import pandas as pd
from inference import load_bundle, predict_customers

bundle = load_bundle()
new_customers = pd.read_csv("new_customers.csv")
results = predict_customers(new_customers, bundle)

print(results.head())
results.to_csv("customer_predictions.csv", index=False)
```

Input must contain the original model input columns.
Do not include target `y` or `duration` as required input fields.
Additional columns are ignored.

Predicted subscription:
- 1 / yes: predicted probability meets or exceeds the saved threshold.
- 0 / no: predicted probability is below the threshold.

Security: only load joblib files from trusted sources.
