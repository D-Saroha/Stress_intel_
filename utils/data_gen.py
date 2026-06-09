import pandas as pd
import numpy as np

def generate_demo_data():
    np.random.seed(42)
    n_samples = 1000
    
    data = {
        "sleep_hours": np.random.uniform(4, 10, n_samples),
        "study_hours": np.random.uniform(1, 12, n_samples),
        "physical_activity": np.random.uniform(0, 90, n_samples),
        "social_interaction": np.random.uniform(0, 120, n_samples),
        "screen_time": np.random.uniform(1, 10, n_samples),
        "diet_quality": np.random.uniform(1, 10, n_samples),
        "heart_rate": np.random.uniform(60, 110, n_samples),
        "anxiety_score": np.random.uniform(0, 100, n_samples),
    }
    
    df = pd.DataFrame(data)
    
    # Simple logic for target
    score = (df["anxiety_score"] * 0.4 + 
             (12 - df["sleep_hours"]) * 10 * 0.3 + 
             df["study_hours"] * 2 - 
             df["physical_activity"] * 0.1)
             
    df["stress_level"] = pd.cut(score, bins=[-np.inf, 40, 70, np.inf], labels=["Low", "Medium", "High"])
    
    df.to_csv("c:\\Users\\mksme\\Desktop\\StressIntel_PRO\\data\\raw\\StressLevelDataset_Mapped.csv", index=False)
    print("Demo dataset generated.")

if __name__ == "__main__":
    generate_demo_data()
