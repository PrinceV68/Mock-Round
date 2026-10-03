import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

root = Path(__file__).resolve().parent.parent
output = root / "outputs"
output.mkdir(exist_ok=True)

# find the correct csv files
assessment_file = None
course_file = None

for file in root.rglob("*.csv"):
    try:
        temp = pd.read_csv(file)

        if "assessment_id" in temp.columns:
            assessment_file = file

        if "course_id" in temp.columns and "department" in temp.columns:
            course_file = file

    except:
        pass

if assessment_file is None or course_file is None:
    print("Required CSV files were not found.")
    print("Assessment file:", assessment_file)
    print("Course file:", course_file)
    input("\nPress Enter to close...")
    raise SystemExit

print("Assessment file:", assessment_file.name)
print("Course file:", course_file.name)

# load data
assessments = pd.read_csv(assessment_file)
courses = pd.read_csv(course_file)

print("\nTraining Performance Analysis")
print("-" * 35)

print("Assessment records:", len(assessments))
print("Course records:", len(courses))

# clean numeric columns
assessments["assessment_id"] = pd.to_numeric(
    assessments["assessment_id"]
)

assessments["score"] = pd.to_numeric(
    assessments["score"]
)

assessments["attendance_pct"] = pd.to_numeric(
    assessments["attendance_pct"]
)

# remove duplicate
assessments = assessments.drop_duplicates()

print("Records after cleaning:", len(assessments))

# merge
df = assessments.merge(
    courses,
    on="course_id",
    how="left"
)

df["pass_flag"] = (df["score"] >= 50).astype(int)

# department summary
department = (
    df.groupby("department")
    .agg(
        total=("assessment_id", "count"),
        passed=("pass_flag", "sum")
    )
    .reset_index()
)

department["pass_rate"] = (
    department["passed"] /
    department["total"] * 100
).round(2)

print("\nDepartment Summary")
print(department.to_string(index=False))

# course summary
course = (
    df.groupby(["course_id", "course"])
    .agg(
        passed=("pass_flag", "sum"),
        total=("assessment_id", "count")
    )
    .reset_index()
)

course["pass_rate"] = (
    course["passed"] /
    course["total"] * 100
).round(2)

print("\nCourse Summary")
print(course.to_string(index=False))

# lowest pass rate
lowest = course["pass_rate"].min()

print("\nLowest Pass Rate Course")
print(
    course[course["pass_rate"] == lowest]
    .to_string(index=False)
)

# monthly average
months = ["Jan", "Feb", "Mar"]

df["month"] = pd.Categorical(
    df["month"],
    categories=months,
    ordered=True
)

monthly = (
    df.groupby("month", observed=False)["score"]
    .mean()
    .round(2)
)

print("\nMonthly Average Score")
print(monthly)

# graph
plt.figure(figsize=(8, 5))

bars = plt.bar(
    monthly.index,
    monthly.values
)

plt.title("Monthly Average Score")
plt.xlabel("Month")
plt.ylabel("Average Score")

for bar, value in zip(bars, monthly.values):
    plt.text(
        bar.get_x() + bar.get_width() / 2,
        value + 1,
        f"{value:.2f}",
        ha="center"
    )

plt.tight_layout()

plt.savefig(
    output / "python_chart.png",
    dpi=300
)

plt.show()

# save output
df.to_csv(
    output / "clean_data.csv",
    index=False
)

department.to_csv(
    output / "python_summary.csv",
    index=False
)

print("\nDone!")
print("python_chart.png created")
print("clean_data.csv created")
print("python_summary.csv created")