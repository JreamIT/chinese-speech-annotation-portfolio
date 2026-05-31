import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

summary_path = Path("results/summary.csv")
output_dir = Path("results")
output_dir.mkdir(exist_ok=True)

df = pd.read_csv(summary_path)

df = df.sort_values(by="severity_score", ascending=False)

print("Total audio samples:", len(df))

print("\nRanked scenarios by severity score:")
for _, row in df.iterrows():
    print(f"{row['scenario']}: {row['severity_score']}")

print("\nAverage error count:", round(df["error_count"].mean(), 2))
print("Average severity score:", round(df["severity_score"].mean(), 2))

# Chart 1: Severity Score by Scenario
plt.figure(figsize=(9, 5))
plt.bar(df["scenario"], df["severity_score"])

plt.title("Recognition Difficulty by Speech Condition")
plt.xlabel("Speech Condition")
plt.ylabel("Weighted Severity Score")

plt.xticks(rotation=30, ha="right")
plt.tight_layout()

plt.savefig(output_dir / "severity_score_by_scenario.png", dpi=300)

print("\nChart saved to results/severity_score_by_scenario.png")

# Chart 2: Error Count by Scenario
plt.figure(figsize=(9, 5))
plt.bar(df["scenario"], df["error_count"])

plt.title("Error Count by Speech Condition")
plt.xlabel("Speech Condition")
plt.ylabel("Error Count")

plt.xticks(rotation=30, ha="right")
plt.tight_layout()

plt.savefig(output_dir / "error_count_by_scenario.png", dpi=300)

print("Chart saved to results/error_count_by_scenario.png")