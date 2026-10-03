# 📊 Training Performance Analysis

<p align="center">
  <img src="https://img.shields.io/badge/Data%20Analysis-Practical%20Exam-blue?style=for-the-badge">
  <img src="https://img.shields.io/badge/Set-C-purple?style=for-the-badge">
  <img src="https://img.shields.io/badge/Python-3.x-yellow?style=for-the-badge&logo=python">
  <img src="https://img.shields.io/badge/Power%20BI-Dashboard-orange?style=for-the-badge&logo=powerbi">
  <img src="https://img.shields.io/badge/SQL-Analysis-blue?style=for-the-badge">
  <img src="https://img.shields.io/badge/Excel-Analysis-green?style=for-the-badge&logo=microsoftexcel">
</p>

<p align="center">
  <b>📈 Training Performance & Academic Support Analysis</b><br>
  A complete data analysis project using Excel, SQL, Python and Power BI
</p>

---

## 👨‍🎓 Student Information

| 📌 Detail | Information |
|---|---|
| 👤 Student Name | **Prince Vaghasiya** |
| 📝 Exam | **Data Analysis Practical Exam** |
| 🔢 Exam Set | **Set C** |
| 🎓 Course | **Data Analysis** |
| 🏫 Institute | **Red & White Skill Education** |

---

# 🎯 Project Overview

This project analyzes training assessment performance across different courses, departments, months and batches.

The main business question is:

> **Which course needs the most academic support, and how does performance differ across batches?**

The project combines four major data-analysis tools:

```text
📊 Excel
   ↓
🗄️ SQL
   ↓
🐍 Python
   ↓
📈 Power BI
```

Each tool is used for a different part of the analysis while using the same dataset and metric definitions.

---

# 💼 Business Objective

The purpose of this project is to understand student performance across different training courses and identify areas where additional academic support may be useful.

The analysis focuses on:

- 📚 Course performance
- 🏢 Department performance
- 👥 Batch performance
- 📅 Monthly performance
- ✅ Pass rates
- 📈 Average scores
- 🎯 Underperforming courses

---

# ❓ Business Questions

1. Which course has the lowest pass rate?
2. Which department has better overall performance?
3. How does the average score change from January to March?
4. How does performance differ across batches?
5. Which course should receive additional academic support?

---

# 📂 Dataset

The project uses two main CSV files.

## 📄 Assessment Dataset

**File:** `data/raw/assessment_final.csv`

| Column | Description | Data Type |
|---|---|---|
| 🆔 `assessment_id` | Assessment identifier | Integer |
| 📅 `month` | Assessment month | Text |
| 🔑 `course_id` | Course identifier | Text |
| 👥 `batch` | Batch timing | Text |
| 📊 `score` | Assessment score | Numeric |
| 📈 `attendance_pct` | Attendance percentage | Numeric |

## 📄 Course Dataset

**File:** `data/raw/courses.csv`

| Column | Description | Data Type |
|---|---|---|
| 🔑 `course_id` | Course identifier | Text |
| 📚 `course` | Course name | Text |
| 🏢 `department` | Course department | Text |

---

# 🧹 Data Cleaning

The following cleaning steps were performed:

- 🔢 Converted numeric columns to numeric data types
- 🧹 Removed the exact duplicate assessment record
- 🔗 Merged assessment and course data using `course_id`
- 🔍 Checked course information after merging
- ✅ Created a `pass_flag`
- 📅 Ordered months as **Jan → Feb → Mar**

The supplied assessment data contains 13 rows including one exact duplicate. After cleaning, the dataset contains **12 assessment records**.

---

# ✅ Pass Flag

```text
Score >= 50  → Pass
Score < 50   → Fail
```

```text
pass_flag = 1 → Pass
pass_flag = 0 → Fail
```

## 📐 Pass Rate

```text
Pass Rate = Passing Assessments / Total Assessments × 100
```

---

# 🛠️ Technologies Used

- 🐍 Python
- 🐼 Pandas
- 📈 Matplotlib
- 🗄️ SQL
- 📊 Microsoft Excel
- 📈 Microsoft Power BI
- 🐙 Git & GitHub

---

# 📁 Project Structure

```text
Mock-2/
│
├── 📂 data/
│   └── 📂 raw/
│       ├── 📄 assessment_final.csv
│       ├── 📄 assessments.csv
│       └── 📄 courses.csv
│
├── 📂 excel/
│   └── 📊 analysis.xlsx
│
├── 📂 powerbi/
│   └── 📊 dashboard.pbix
│
├── 📂 python/
│   ├── 🐍 Analysis.py
│   └── 🐍 analysis111.py
│
├── 📂 sql/
│   ├── 📄 setup.sql
│   ├── 📄 queries.sql
│   ├── 📊 s2a_avg_score_by_department.csv
│   ├── 📊 s2b_underperforming_courses.csv
│   └── 📊 s2c_top_two_batches.csv
│
├── 📂 outputs/
│   ├── 📄 clean_data.csv
│   ├── 📄 python_summary.csv
│   └── 🖼️ python_chart.png
│
├── 📘 README.md
├── 📦 requirements.txt
└── 🚫 .gitignore
```

---

# 🐍 Python Analysis

Python is used for data cleaning, calculations and visualization.

## 🔄 Workflow

```text
📥 Load CSV Files
        ↓
🧹 Clean Data
        ↓
🔄 Remove Duplicate
        ↓
🔗 Merge Datasets
        ↓
✅ Create Pass Flag
        ↓
🏢 Department Analysis
        ↓
📚 Course Analysis
        ↓
👥 Batch Analysis
        ↓
📅 Monthly Analysis
        ↓
📈 Visualization
        ↓
💾 Export Results
```

### 📤 Python Outputs

```text
outputs/clean_data.csv
outputs/python_summary.csv
outputs/python_chart.png
```

---

# 📈 Python Visualization

The Python visualization shows the average assessment score by month.

### 📅 Month Order

```text
January → February → March
```

The chart is saved automatically as:

```text
outputs/python_chart.png
```

---

# 🗄️ SQL Analysis

SQL is used for additional analysis.

### 🔍 SQL Tasks

- 📊 Average score by department
- ⚠️ Underperforming courses
- 🏆 Top two batches

### 📄 SQL Files

```text
sql/setup.sql
sql/queries.sql
```

### 📤 SQL Results

```text
sql/s2a_avg_score_by_department.csv
sql/s2b_underperforming_courses.csv
sql/s2c_top_two_batches.csv
```

---

# 📊 Excel Analysis

Excel is used for:

- 🧹 Data cleaning
- 📊 Summary calculations
- 📈 Average score analysis
- ✅ Pass-rate calculations
- 📚 Course comparison
- 🏢 Department comparison
- 👥 Batch comparison
- 📉 Charts

Workbook:

```text
excel/analysis.xlsx
```

---

# 📊 Power BI Dashboard

Power BI is used to create an interactive training-performance dashboard.

### Dashboard Areas

- 📊 Total Assessments
- 📈 Average Score
- ✅ Pass Rate
- 📚 Course Performance
- 🏢 Department Performance
- 👥 Batch Performance
- 📅 Monthly Performance

Power BI file:

```text
powerbi/dashboard.pbix
```

Dashboard preview:

```text
outputs/powerbi_dashboard.png
```

---

# 🔎 Key Findings

## 🏢 Department Performance

| Department | Passing | Total | Pass Rate |
|---|---:|---:|---:|
| 🏢 Business | 5 | 6 | **83.33%** |
| 💻 Technology | 3 | 6 | **50.00%** |

---

## 📚 Course Performance

| Course | Passing | Total | Pass Rate |
|---|---:|---:|---:|
| Excel | 3 | 3 | 100.00% |
| PowerBI | 2 | 3 | 66.67% |
| SQL | 2 | 3 | 66.67% |
| Python | 1 | 3 | **33.33%** |

### ⚠️ Lowest Pass Rate

**Python (C4)**

```text
Passing Assessments = 1
Total Assessments   = 3

Pass Rate = 1 / 3 × 100
          = 33.33%
```

---

# 👥 Batch Performance

The three batches are:

```text
🌅 Morning
🌆 Evening
📅 Weekend
```

| Batch | Passing | Total | Pass Rate |
|---|---:|---:|---:|
| 🌅 Morning | 3 | 4 | 75.00% |
| 🌆 Evening | 3 | 4 | 75.00% |
| 📅 Weekend | 2 | 4 | 50.00% |

The results show a difference in pass rates between the batches in the supplied dataset.

---

# 📅 Monthly Performance

| Month | Average Score |
|---|---:|
| 🗓️ January | **55.00** |
| 🗓️ February | **62.75** |
| 🗓️ March | **66.75** |

The average score increases across the three months in the supplied dataset.

---

# 💡 Academic Support Recommendation

Based on the course-level pass-rate metric, **Python (C4)** is the course identified for additional academic support.

Possible support activities include:

- 📚 Additional practice exercises
- 🧪 More practical assignments
- 👨‍🏫 Doubt-solving sessions
- 📝 Revision sessions
- 💻 Additional coding practice
- 📈 Regular performance monitoring

Batch-level results can also be reviewed when planning academic support.

---

# 🔄 Cross-Tool Reconciliation

The same cleaned dataset and metric definitions should be used across Python, SQL, Excel and Power BI.

| Metric | 🐍 Python | 🗄️ SQL | 📊 Excel | 📈 Power BI |
|---|:---:|:---:|:---:|:---:|
| Total Records | ✅ | ✅ | ✅ | ✅ |
| Passing Count | ✅ | ✅ | ✅ | ✅ |
| Pass Rate | ✅ | ✅ | ✅ | ✅ |
| Course Performance | ✅ | ✅ | ✅ | ✅ |
| Department Performance | ✅ | ✅ | ✅ | ✅ |
| Batch Performance | ✅ | ✅ | ✅ | ✅ |
| Monthly Average | ✅ | ✅ | ✅ | ✅ |

---

# ⚙️ Installation & Setup

## 1️⃣ Clone the Repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

## 2️⃣ Open the Project

```bash
cd Mock-2
```

## 3️⃣ Install Python Packages

```bash
pip install -r requirements.txt
```

Or:

```bash
pip install pandas matplotlib
```

---

# ▶️ Run Python Analysis

From the project root:

```bash
python Python/Analysis.py
```

After successful execution:

```text
outputs/
├── clean_data.csv
├── python_summary.csv
└── python_chart.png
```

---

# 📊 Power BI Refresh

1. Open `powerbi/dashboard.pbix`
2. Check the data source paths
3. Refresh the dataset
4. Verify the dashboard visuals
5. Save the updated dashboard

---

# 📗 Excel Workbook

Open:

```text
excel/analysis.xlsx
```

The workbook contains the Excel-based calculations and analysis required for the practical.

---

# 🗄️ SQL Setup

Run the SQL setup script:

```text
sql/setup.sql
```

Then execute:

```text
sql/queries.sql
```

The query results are stored inside the `sql` folder.

---

# 📤 Project Outputs

## 🐍 Python

```text
📄 python_summary.csv
```

## 🗄️ SQL

```text
📊 s2a_avg_score_by_department.csv
📊 s2b_underperforming_courses.csv
📊 s2c_top_two_batches.csv
```

## 📊 Power BI

```text
📊 dashboard.pbix
🖼️ powerbi_dashboard.png
```

## 📗 Excel

```text
📊 analysis_final.csv
```

---

# 📚 References

- 📘 Data Analysis Practical Exam – Set C
- 🐍 Pandas Documentation
- 📈 Matplotlib Documentation
- 📊 Microsoft Excel Documentation
- 📊 Microsoft Power BI Documentation
- 🗄️ SQL Documentation

---

# 👤 Authorship Declaration

I confirm that this project has been prepared for the **Data Analysis Practical Exam – Set C**.

The project includes:

- 📊 Excel analysis
- 🗄️ SQL queries
- 🐍 Python analysis
- 📈 Data visualization
- 📊 Power BI dashboard
- 🧹 Data cleaning
- 📄 Project documentation

The analysis is based on the assessment and course datasets provided for the practical examination.

---

# ✅ Project Completion

| Module | Status |
|---|:---:|
| 📊 Excel | ✅ Completed |
| 🗄️ SQL | ✅ Completed |
| 🐍 Python | ✅ Completed |
| 📈 Visualization | ✅ Completed |
| 📊 Power BI | ✅ Completed |
| 🧹 Data Cleaning | ✅ Completed |
| 📘 Documentation | ✅ Completed |

---

# 🏁 Final Summary

This project provides a complete analysis of training assessment performance using multiple data-analysis tools.

```text
📥 Data Collection
      ↓
🧹 Data Cleaning
      ↓
🔗 Data Integration
      ↓
📊 Exploratory Analysis
      ↓
🗄️ SQL Analysis
      ↓
🐍 Python Analysis
      ↓
📗 Excel Analysis
      ↓
📈 Power BI Dashboard
      ↓
💡 Academic Support Insights
```

The course-level analysis identifies **Python (C4)** as having the lowest pass rate in the supplied dataset, while the batch analysis shows differences between Morning, Evening and Weekend batches.

---

<p align="center">

## 🚀 Data Analysis Practical – Set C

### 📊 Excel • 🗄️ SQL • 🐍 Python • 📈 Power BI

<b>Made for Data Analysis Practical Examination</b>

</p>
