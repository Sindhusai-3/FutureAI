import pandas as pd
import os
from sklearn.linear_model import LinearRegression

FALLBACK_SALARIES = {
    "web developer":         [300000, 450000, 600000, 750000, 900000, 1050000, 1200000, 1350000, 1500000, 1650000, 1800000],
    "python developer":      [350000, 500000, 700000, 900000, 1100000, 1300000, 1500000, 1700000, 1900000, 2100000, 2300000],
    "data analyst":          [400000, 550000, 700000, 900000, 1100000, 1300000, 1500000, 1700000, 1900000, 2000000, 2200000],
    "machine learning engineer": [500000, 700000, 950000, 1200000, 1500000, 1800000, 2100000, 2400000, 2700000, 3000000, 3300000],
}

def predict_salary(role, experience):
    try:
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        csv_path = os.path.join(base_dir, "data", "ds_salaries.csv")
        df = pd.read_csv(csv_path, encoding="utf-8")
        role_df = df[df["Role"].str.lower() == role.lower()]
        if not role_df.empty:
            X = role_df[["Experience"]]
            y = role_df["Salary"]
            model = LinearRegression()
            model.fit(X, y)
            return round(model.predict([[experience]])[0])
    except Exception:
        pass

    # Fallback: use built-in lookup table
    key = role.lower()
    if key in FALLBACK_SALARIES:
        salaries = FALLBACK_SALARIES[key]
        idx = min(experience, len(salaries) - 1)
        return salaries[idx]
    return None
