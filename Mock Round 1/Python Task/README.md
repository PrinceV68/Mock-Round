# 🐍 Customer Support Data Analysis — Python

<p align="center">
  <img src="https://img.shields.io/badge/Python-Data%20Analysis-3776AB?style=for-the-badge&logo=python&logoColor=white">
  <img src="https://img.shields.io/badge/Pandas-Data%20Processing-150458?style=for-the-badge&logo=pandas&logoColor=white">
  <img src="https://img.shields.io/badge/Matplotlib-Visualization-11557C?style=for-the-badge&logo=matplotlib&logoColor=white">
  <img src="https://img.shields.io/badge/Status-Completed-success?style=for-the-badge">
</p>

<p align="center">
  <b>Python-based Customer Support SLA & Performance Analysis</b>
  <br>
  Clean raw ticket data, enrich it with team information, measure SLA performance, and generate analytical outputs.
</p>

---

## 📌 Executive Summary

This project analyzes customer-support ticket data using **Python, Pandas, and Matplotlib** to evaluate resolution performance and SLA compliance.

The raw ticket dataset contains **13 records**, including **one duplicate ticket record**. After removing the duplicate, the analysis works with **12 unique tickets** across **Service** and **Technical** departments.

The analysis applies a **24-hour SLA threshold** to identify breached tickets and produces department-level and team-level performance metrics.

### 📊 Executive Snapshot

| KPI | Result |
|---|---:|
| 🎫 Raw Records | **13** |
| 🧹 Duplicate Records Removed | **1** |
| ✅ Clean Tickets | **12** |
| 🚨 SLA Breaches | **5** |
| ⏱️ Overall SLA Breach Rate | **41.67%** |
| 📅 Months Analyzed | **Jan – Mar** |
| 🏢 Departments | **2** |
| 👥 Teams | **4** |

### 🔎 Key Findings

**🚨 Overall SLA performance**

5 out of 12 unique tickets exceeded the 24-hour resolution target, resulting in an overall SLA breach rate of **41.67%**.

**🏢 Department comparison**

| Department | Tickets | Breaches | SLA Breach Rate |
|---|---:|---:|---:|
| Service | 6 | 2 | **33.33%** |
| Technical | 6 | 3 | **50.00%** |

Technical support recorded a higher SLA breach rate than Service support in this dataset.

**👥 Team performance**

The team-level analysis identifies breach rates for each support team:

| Team | Breach Rate |
|---|---:|
| AccountCare | **0.00%** |
| BillingHelp | **50.00%** |
| AppSupport | **66.67%** |
| DeviceHelp | **50.00%** |

AppSupport recorded the highest breach rate at **66.67%**, based on 2 breached tickets out of 3.

**📅 Monthly resolution performance**

Average resolution time was **24 hours in each of the three months**:

| Month | Average Resolution |
|---|---:|
| January | **24 hrs** |
| February | **24 hrs** |
| March | **24 hrs** |

The monthly average therefore remained stable across the period analyzed.

> **Executive takeaway:** The analysis identifies a **41.67% overall SLA breach rate**, with Technical support showing a **50% breach rate** compared with **33.33% for Service**. AppSupport recorded the highest team-level breach rate. At the same time, the monthly average resolution time remained consistently at 24 hours.

---

# 🎯 Project Objective

The objective is to transform raw customer-support data into structured analytical outputs using Python.

The project performs four major tasks:

```text
📁 Raw CSV Data
       │
       ▼
🧹 Data Cleaning
       │
       ▼
🔗 Data Enrichment
       │
       ▼
🚨 SLA Analysis
       │
       ▼
📊 Summary & Visualization
```

---

# 📂 Project Structure

```text
Python Task/
│
├── 📁 data/
│   └── 📁 raw/
│       ├── 🎫 tickets.csv
│       └── 👥 teams.csv
│
├── 📁 python/
│   └── 🐍 analysis.py
│
├── 📁 outputs/
│   ├── 📄 clean_data.csv
│   ├── 📊 python_summary.csv
│   └── 📈 python_chart.png
│
└── 📖 README.md
```

---

# 🗃️ Dataset

## 🎫 tickets.csv

Contains customer-support ticket information.

| Column | Description |
|---|---|
| `ticket_id` | Unique ticket identifier |
| `month` | Ticket month |
| `team_id` | Support team identifier |
| `channel` | Customer-support channel |
| `resolution_hours` | Ticket resolution time |
| `satisfaction` | Customer satisfaction score |

## 👥 teams.csv

Contains team reference information.

| Column | Description |
|---|---|
| `team_id` | Unique team identifier |
| `team` | Support team name |
| `department` | Department classification |

---

# 🧹 Data Cleaning

The analysis begins by loading both CSV files with Pandas.

```python
tickets = pd.read_csv("data/raw/tickets.csv")
teams = pd.read_csv("data/raw/teams.csv")
```

### 🔢 Numeric Conversion

The resolution and satisfaction columns are explicitly converted to numeric types:

```python
tickets["resolution_hours"] = pd.to_numeric(
    tickets["resolution_hours"]
)

tickets["satisfaction"] = pd.to_numeric(
    tickets["satisfaction"]
)
```

### ♻️ Duplicate Removal

The raw dataset contains one duplicate ticket record.

```python
tickets = tickets.drop_duplicates()
```

Result:

```text
Before cleaning  → 13 records
After cleaning   → 12 records
```

---

# 🔗 Data Enrichment

The cleaned ticket data is merged with the team lookup dataset using `team_id`.

```python
data = pd.merge(
    tickets,
    teams,
    on="team_id",
    how="left"
)
```

This adds:

- 👥 Team name
- 🏢 Department

The script also validates the merge:

```python
assert len(data) == 12
assert data["department"].isna().sum() == 0
```

These checks ensure that all cleaned tickets successfully receive department information.

---

# 🚨 SLA Analysis

A **24-hour resolution target** is used to identify SLA breaches.

```python
data["breach_flag"] = (
    data["resolution_hours"] > 24
).astype(int)
```

### Meaning

```text
Resolution > 24 hours
        │
        ▼
   🚨 SLA Breach
     breach_flag = 1

Resolution ≤ 24 hours
        │
        ▼
    ✅ Within SLA
     breach_flag = 0
```

---

# 🏢 Department Analysis

The project calculates:

- Total tickets
- Breached tickets
- SLA breach percentage

using Pandas `groupby()` and `agg()`.

```python
department_summary = data.groupby("department").agg(
    total_tickets=("ticket_id", "count"),
    breached_tickets=("breach_flag", "sum")
).reset_index()
```

The breach percentage is then calculated as:

```python
department_summary["sla_breach_rate_pct"] = (
    department_summary["breached_tickets"] /
    department_summary["total_tickets"] * 100
).round(2)
```

### 📊 Result

```text
Service
6 tickets → 2 breaches → 33.33%

Technical
6 tickets → 3 breaches → 50.00%
```

---

# 👥 Team-Level Analysis

The project also calculates SLA performance for each individual team.

```python
team_summary = data.groupby(
    ["team_id", "team"]
).agg(
    total_tickets=("ticket_id", "count"),
    breached_tickets=("breach_flag", "sum")
).reset_index()
```

The team with the highest breach rate is identified programmatically rather than manually.

```python
highest_rate = team_summary["breach_rate_pct"].max()

highest_team = team_summary[
    team_summary["breach_rate_pct"] == highest_rate
]
```

### 📊 Team Results

| Team | Tickets | Breaches | Breach Rate |
|---|---:|---:|---:|
| AccountCare | 3 | 0 | 0.00% |
| BillingHelp | 3 | 1 | 50.00% |
| AppSupport | 3 | 2 | 66.67% |
| DeviceHelp | 3 | 1 | 50.00% |

---

# 📅 Monthly Analysis

The project calculates the average resolution time for each month.

```python
month_order = ["Jan", "Feb", "Mar"]

monthly_avg = data.groupby(
    "month"
)["resolution_hours"].mean()

monthly_avg = monthly_avg.reindex(month_order)
```

### Result

```text
January   → 24 hours
February  → 24 hours
March     → 24 hours
```

The results are visualized using Matplotlib.

---

# 📈 Visualization

The project generates:

**`outputs/python_chart.png`**

The chart displays:

> **Monthly Average Resolution Time**

The visualization makes it easier to compare resolution performance across January, February, and March.

```python
plt.figure(figsize=(8, 5))

monthly_avg.plot(kind="bar")

plt.title("Monthly Average Resolution Time")
plt.xlabel("Month")
plt.ylabel("Average Resolution Hours")
plt.xticks(rotation=0)

plt.tight_layout()
plt.savefig("outputs/python_chart.png")
plt.close()
```

---

# 📤 Generated Outputs

Running the analysis creates three output files.

### 🧹 `clean_data.csv`

Contains the cleaned and enriched ticket-level dataset.

Includes:

```text
ticket_id
month
team_id
channel
resolution_hours
satisfaction
team
department
breach_flag
```

### 📊 `python_summary.csv`

Contains department-level SLA performance:

```text
department
total_tickets
breached_tickets
sla_breach_rate_pct
```

### 📈 `python_chart.png`

Contains the monthly average resolution-time visualization.

---

# 🛠️ Technologies Used

<p align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white">
  <img src="https://img.shields.io/badge/Pandas-150458?style=flat-square&logo=pandas&logoColor=white">
  <img src="https://img.shields.io/badge/Matplotlib-11557C?style=flat-square&logo=matplotlib&logoColor=white">
  <img src="https://img.shields.io/badge/CSV-Data-lightgrey?style=flat-square">
</p>

### 🐍 Python

Used as the primary programming language for the complete analysis workflow.

### 🐼 Pandas

Used for:

- CSV loading
- Data cleaning
- Duplicate removal
- Data merging
- Grouping
- Aggregation
- Output generation

### 📈 Matplotlib

Used to create the monthly resolution-time chart.

---

# ▶️ How to Run

## 1️⃣ Install Python

Make sure Python is installed on your system.

Check:

```bash
python --version
```

## 2️⃣ Install Dependencies

```bash
pip install pandas matplotlib
```

## 3️⃣ Open the Project Root

Make sure your terminal is located at:

```text
Python Task/
```

## 4️⃣ Run the Analysis

```bash
python python/analysis.py
```

### ✅ Successful execution

The script will:

```text
✔ Load the CSV files
✔ Convert numeric columns
✔ Remove duplicate records
✔ Merge ticket and team data
✔ Validate the merged dataset
✔ Calculate SLA breaches
✔ Generate department summary
✔ Calculate team breach rates
✔ Calculate monthly averages
✔ Generate the chart
✔ Export CSV results
```

---

# 📌 Important: Relative File Paths

The script is designed to run from the **repository root**.

Use:

```bash
python python/analysis.py
```

The project uses relative paths such as:

```python
data/raw/tickets.csv
data/raw/teams.csv
outputs/python_chart.png
outputs/clean_data.csv
outputs/python_summary.csv
```

This keeps the project portable across different machines without requiring machine-specific file paths.

---

# 🧠 Skills Demonstrated

```text
🐍 Python Programming
🐼 Pandas
🧹 Data Cleaning
♻️ Duplicate Detection
🔗 Data Merging
🔢 Data Type Handling
🚨 SLA Analysis
📊 GroupBy & Aggregation
📈 Data Visualization
📁 CSV Processing
✅ Data Validation
📤 Automated Output Generation
```

---

# 💼 Business Value

Although this is a small dataset, the workflow demonstrates a realistic analytics process that can be scaled to larger customer-support datasets.

The same approach can be used by organizations to monitor:

- 🎫 Support ticket volumes
- 🚨 SLA compliance
- ⏱️ Resolution efficiency
- 👥 Team performance
- 🏢 Department performance
- 💬 Channel performance
- ⭐ Customer satisfaction

---

# 🚀 Future Improvements

Potential extensions include:

- 📊 Interactive dashboards using Power BI
- 📅 More detailed time-series analysis
- 💬 Channel-level SLA analysis
- ⭐ Satisfaction vs. resolution-time analysis
- 📈 Trend and performance KPIs
- 🧪 Statistical analysis
- 🤖 SLA breach prediction using Machine Learning
- 📧 Automated performance reports
- 🗄️ Database integration
- 🌐 Web-based analytics dashboard

---

# 👨‍💻 Author

 # Prince Vaghasiya #
 
 🎓 Diploma — AI/ML & Data Science

### Project Information

| Category | Details |
|---|---|
| 📌 Project | Customer Support Data Analysis |
| 🐍 Language | Python |
| 📊 Library | Pandas |
| 📈 Visualization | Matplotlib |
| 🎯 Focus | SLA & Support Performance |
| 📅 Analysis Period | Jan – Mar |
| 🟢 Status | Completed |

---

## ⭐ Project Highlights

```text
📁 Raw Data
     ↓
🧹 Clean & Validate
     ↓
🔗 Merge Datasets
     ↓
🚨 Detect SLA Breaches
     ↓
🏢 Analyze Departments
     ↓
👥 Analyze Teams
     ↓
📅 Analyze Monthly Performance
     ↓
📊 Generate CSV + Chart Outputs
```

<p align="center">
  <b>🐍 Turning Raw Customer Support Data Into Actionable Insights</b>
  <br><br>
  Built with Python • Pandas • Matplotlib
</p>
