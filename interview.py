import pandas as pd
import os

def get_answer(question):
    try:
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        csv_path = os.path.join(base_dir, "data", "interview_questions.csv")
        df = pd.read_csv(csv_path, encoding="utf-8")
        for _, row in df.iterrows():
            if str(row["Question"]).lower() == question.lower():
                return row["Answer"]
    except Exception:
        pass
    return None
