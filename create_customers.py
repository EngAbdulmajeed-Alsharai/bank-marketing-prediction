#
# import pandas as pd
# from pathlib import Path
#
# data = [
#     {
#         "age": 56, "job": "housemaid", "marital": "married",
#         "education": "basic.4y", "default": "no", "housing": "no",
#         "loan": "no", "contact": "telephone", "month": "may",
#         "day_of_week": "mon", "campaign": 1, "pdays": 999,
#         "previous": 0, "poutcome": "nonexistent", "emp.var.rate": 1.1,
#         "cons.price.idx": 93.994, "cons.conf.idx": -36.4,
#         "euribor3m": 4.857, "nr.employed": 5191.0
#     },
#     {
#         "age": 37, "job": "services", "marital": "married",
#         "education": "high.school", "default": "unknown", "housing": "yes",
#         "loan": "no", "contact": "cellular", "month": "nov",
#         "day_of_week": "wed", "campaign": 2, "pdays": 999,
#         "previous": 0, "poutcome": "nonexistent", "emp.var.rate": -0.1,
#         "cons.price.idx": 93.200, "cons.conf.idx": -42.0,
#         "euribor3m": 4.076, "nr.employed": 5195.8
#     },
#     {
#         "age": 29, "job": "technician", "marital": "single",
#         "education": "professional.course", "default": "no", "housing": "yes",
#         "loan": "no", "contact": "cellular", "month": "jul",
#         "day_of_week": "thu", "campaign": 1, "pdays": 999,
#         "previous": 0, "poutcome": "nonexistent", "emp.var.rate": 1.4,
#         "cons.price.idx": 93.918, "cons.conf.idx": -42.7,
#         "euribor3m": 4.968, "nr.employed": 5228.1
#     },
#     {
#         "age": 45, "job": "admin.", "marital": "married",
#         "education": "university.degree", "default": "no", "housing": "no",
#         "loan": "yes", "contact": "cellular", "month": "aug",
#         "day_of_week": "tue", "campaign": 3, "pdays": 999,
#         "previous": 0, "poutcome": "nonexistent", "emp.var.rate": 1.4,
#         "cons.price.idx": 93.444, "cons.conf.idx": -36.1,
#         "euribor3m": 4.963, "nr.employed": 5228.1
#     },
#     {
#         "age": 32, "job": "blue-collar", "marital": "single",
#         "education": "basic.9y", "default": "unknown", "housing": "yes",
#         "loan": "no", "contact": "telephone", "month": "jun",
#         "day_of_week": "fri", "campaign": 1, "pdays": 999,
#         "previous": 0, "poutcome": "nonexistent", "emp.var.rate": 1.4,
#         "cons.price.idx": 94.465, "cons.conf.idx": -41.8,
#         "euribor3m": 4.959, "nr.employed": 5228.1
#     }
# ]
#
# df = pd.DataFrame(data)
#
# # حفظ الملف بجوار هذا السكربت داخل مجلد المشروع
# output_path = Path(__file__).resolve().parent / "new_customers.csv"
#
# df.to_csv(output_path, index=False, encoding="utf-8")
#
# print("تم إنشاء ملف العملاء التجريبيين بنجاح.")
# print("عدد الصفوف والأعمدة:", df.shape)
# print("مسار الملف:", output_path)
# print("\nمعاينة البيانات:")
# print(df.head())
import pandas as pd
from pathlib import Path
import random

# Create 100 varied synthetic customers with all 19 required input columns.
random.seed(42)

jobs = ["admin.", "blue-collar", "technician", "services", "management",
        "retired", "student", "housemaid", "entrepreneur", "unemployed",
        "self-employed", "unknown"]
maritals = ["married", "single", "divorced", "unknown"]
educations = ["basic.4y", "basic.6y", "basic.9y", "high.school",
              "professional.course", "university.degree", "illiterate", "unknown"]
defaults = ["no", "yes", "unknown"]
housing_vals = ["no", "yes", "unknown"]
loan_vals = ["no", "yes", "unknown"]
contacts = ["cellular", "telephone"]
months = ["mar", "apr", "may", "jun", "jul", "aug", "sep", "oct", "nov", "dec"]
days = ["mon", "tue", "wed", "thu", "fri"]
poutcomes = ["nonexistent", "failure", "success"]

rows = []
for i in range(100):
    # Vary economic context and campaign history, while keeping values in familiar dataset ranges.
    rows.append({
        "age": random.choice([18, 22, 25, 29, 32, 37, 42, 45, 50, 56, 61, 67, 74]),
        "job": random.choice(jobs),
        "marital": random.choice(maritals),
        "education": random.choice(educations),
        "default": random.choice(defaults),
        "housing": random.choice(housing_vals),
        "loan": random.choice(loan_vals),
        "contact": random.choice(contacts),
        "month": random.choice(months),
        "day_of_week": random.choice(days),
        "campaign": random.choice([1, 1, 2, 2, 3, 4, 5, 7, 10]),
        "pdays": random.choice([999, 999, 999, 3, 6, 9, 12, 15, 20, 27]),
        "previous": random.choice([0, 0, 0, 1, 2, 3, 4]),
        "poutcome": random.choice(poutcomes),
        "emp.var.rate": random.choice([-3.4, -1.8, -0.1, 1.1, 1.4]),
        "cons.price.idx": random.choice([92.201, 92.893, 93.200, 93.444, 93.918, 93.994, 94.465]),
        "cons.conf.idx": random.choice([-50.8, -47.1, -42.7, -42.0, -36.4, -33.6, -26.9]),
        "euribor3m": random.choice([0.634, 1.044, 1.405, 2.453, 3.743, 4.076, 4.857, 4.968, 5.045]),
        "nr.employed": random.choice([4963.6, 4991.6, 5008.7, 5076.2, 5099.1, 5191.0, 5195.8, 5228.1])
    })

df = pd.DataFrame(rows)
output_path = Path(__file__).resolve().parent / "new_customers_100.csv"
df.to_csv(output_path, index=False, encoding="utf-8", lineterminator="\n")
print(f"Created: {output_path}")
print(f"Shape: {df.shape}")
print(df.head(5).to_string(index=False))
