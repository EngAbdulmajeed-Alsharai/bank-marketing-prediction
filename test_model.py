
from pathlib import Path
import pandas as pd

from inference import load_bundle, predict_customers

# تحديد مجلد المشروع تلقائيًا
BASE_DIR = Path(__file__).resolve().parent

# قراءة بيانات العملاء التجريبية الموجودة مسبقًا
input_path = BASE_DIR / "new_customers_100.csv"
# input_path = BASE_DIR / "new_customers.csv"
# فحص محتوى الملف قبل قراءته
print("أول أسطر الملف:")
print(input_path.read_text(encoding="utf-8-sig")[:500])

# قراءة CSV مع اكتشاف الفاصل تلقائيًا
customers = pd.read_csv(
    input_path,
    sep=None,
    engine="python",
    quotechar='"'
)

print("\nأسماء الأعمدة المقروءة:")
print(customers.columns.tolist())

print("\nشكل البيانات:", customers.shape)

print("تم تحميل بيانات العملاء بنجاح.")
print("شكل البيانات:", customers.shape)

# تحميل النموذج المدرّب
bundle = load_bundle(str(BASE_DIR))
print("\nتم تحميل النموذج بنجاح.")

# إجراء التنبؤات
results = predict_customers(customers, bundle)

# عرض النتائج
print("\nنتائج اختبار النموذج:\n")
print(results.to_string(index=False))

# حفظ النتائج في ملف CSV
output_path = BASE_DIR / "test_results.csv"
results.to_csv(output_path, index=False)

print(f"\nتم حفظ النتائج في: {output_path}")
