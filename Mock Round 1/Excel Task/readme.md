# 📊 Customer Support Quality Analysis

<p align="center">
  <img src="https://img.shields.io/badge/Excel-Data%20Analysis-217346?style=for-the-badge&logo=microsoftexcel&logoColor=white" alt="Excel">
  <img src="https://img.shields.io/badge/Analytics-Customer%20Support-blue?style=for-the-badge&logo=googleanalytics&logoColor=white" alt="Analytics">
  <img src="https://img.shields.io/badge/Status-Completed-success?style=for-the-badge" alt="Status">
</p>

<p align="center">
  <b>Customer Support SLA & Resolution Performance Analysis</b>
  <br>
  A practical Excel-based data analysis project for understanding support performance, SLA breaches, and resolution trends.
</p>

---

## 🎯 Project Overview

**Customer Support Quality Analysis** is an Excel-based analytics project designed to transform raw customer-support ticket data into meaningful performance insights.

The project combines **data cleaning, lookup operations, calculated fields, conditional analysis, summary metrics, and visualization** to evaluate how efficiently customer-support tickets are handled.

### 🔎 The analysis focuses on:

- ⏱️ Ticket resolution performance
- 🚨 SLA breaches
- 💬 Support-channel performance
- 🏢 Department-level performance
- 📅 Monthly resolution trends
- 📈 Data visualization and reporting

---

## 🧩 Project Workflow

```text
             📁 Raw CSV Data
                   │
                   ▼
          🧹 Data Preparation
                   │
                   ▼
          🔎 Lookup & Enrichment
                   │
                   ▼
          ⚙️ Calculated Fields
                   │
                   ▼
           📊 Summary Analysis
                   │
                   ▼
          📈 Business Insights
```

---

## 📂 Project Structure

```text
Customer-Support-Quality-Analysis/
│
├── 📊 analysis.xlsx
│
├── 📁 data/
│   └── 📁 raw/
│       ├── 🎫 tickets.csv
│       └── 👥 teams.csv
│
└── 📖 README.md
```

---

## 📊 Excel Workbook

The main analysis is contained in:

**`analysis.xlsx`**

The workbook contains four structured sheets.

| Sheet | Purpose |
|---|---|
| 🗃️ **Raw** | Original customer-support ticket data |
| 🔎 **Lookup** | Team and department reference data |
| 🧹 **Clean** | Enriched and calculated ticket data |
| 📊 **Summary** | Final analysis, metrics and visualization |

---

## 🗃️ 1. Raw Data

The **Raw** sheet contains the supplied customer-support ticket information.

Typical fields include:

- 🎫 Ticket ID
- 📅 Month
- 👥 Team ID
- 💬 Support Channel
- ⏱️ Resolution Hours
- ⭐ Customer Satisfaction

The raw data is preserved separately so that the analysis can be traced back to the original source.

---

## 🔎 2. Lookup Data

The **Lookup** sheet contains reference information for support teams.

### Lookup information includes:

```text
Team ID
   ↓
Team
   ↓
Department
```

This lookup table is used to enrich the ticket dataset with team and department information.

---

## 🧹 3. Clean Data

The **Clean** sheet contains the prepared dataset used for analysis.

Additional fields are generated using Excel formulas.

### 🔍 Team Lookup

```excel
=XLOOKUP(team_id,Lookup!team_id,Lookup!team)
```

### 🏢 Department Lookup

```excel
=XLOOKUP(team_id,Lookup!team_id,Lookup!department)
```

### 🚨 SLA Breach Flag

A ticket is considered an SLA breach when its resolution time exceeds **24 hours**.

```excel
=IF(resolution_hours>24,1,0)
```

| Value | Meaning |
|---:|---|
| `0` | ✅ Within SLA |
| `1` | 🚨 SLA Breached |

---

## 📊 4. Summary Analysis

The **Summary** sheet converts the cleaned data into useful performance metrics.

### 🚨 SLA Breaches by Channel

`COUNTIFS` is used to identify the number of breached tickets across different support channels.

Example:

```excel
=COUNTIFS(Clean!channel,A2,Clean!breach_flag,1)
```

This allows the analysis to compare:

- 📧 Email
- 💬 Chat
- 📞 Phone

---

### ⏱️ Average Resolution Hours

`AVERAGEIFS` is used to calculate average resolution time based on:

- 🏢 Department
- 📅 Month

This provides a simple view of how resolution performance changes across departments and time periods.

---

## 📈 Visualization

The Summary sheet includes a **column chart** to make the results easier to understand.

### Chart focus

📊 **Average Resolution Hours by Department and Month**

The visualization makes it easier to identify differences in resolution performance without manually reviewing individual tickets.

---

## 💡 Business Questions Answered

This project is designed to answer practical customer-support questions:

| Question | Analysis |
|---|---|
| 🚨 How many tickets breached the SLA? | `breach_flag` |
| 💬 Which channels recorded breaches? | `COUNTIFS` |
| 🏢 How does performance differ by department? | `AVERAGEIFS` |
| 📅 How does resolution time change by month? | Department/month summary |
| ⏱️ How efficiently are tickets resolved? | Average resolution hours |
| 📊 How can the results be communicated clearly? | Column chart |

---

## 🛠️ Tools & Techniques

### 🧰 Tools

<p>
<img src="https://img.shields.io/badge/Microsoft%20Excel-217346?style=flat-square&logo=microsoftexcel&logoColor=white">
<img src="https://img.shields.io/badge/CSV-Data%20Source-lightgrey?style=flat-square">
</p>

### 🧠 Excel Functions

```text
XLOOKUP
IF
COUNTIFS
AVERAGEIFS
```

### 📚 Concepts

- 🧹 Data cleaning
- 🔗 Data lookup & enrichment
- ⚙️ Calculated fields
- 🚨 SLA analysis
- 📊 Aggregation
- 📈 Data visualization
- 💼 Business reporting

---

## 📌 Key Analytical Concepts

### ⏱️ SLA Performance

The project uses a **24-hour resolution threshold** to identify tickets that exceeded the defined service-level target.

### 🚨 Breach Detection

Each ticket receives a binary breach indicator:

```text
Resolution Hours > 24
        │
   ┌────┴────┐
   │         │
  YES        NO
   │         │
   ▼         ▼
  🚨 1      ✅ 0
```

### 📊 Performance Aggregation

The cleaned ticket-level data is aggregated to provide department and month-level performance indicators.

---

## 📁 Data Files

### 🎫 `tickets.csv`

Contains the source customer-support ticket records used for the analysis.

### 👥 `teams.csv`

Contains team and department mapping information used by the lookup formulas.

---

## ▶️ How to Use

### 1️⃣ Download the Repository

Clone or download the project.

### 2️⃣ Open the Workbook

Open:

```text
analysis.xlsx
```

using Microsoft Excel.

### 3️⃣ Explore the Data

Navigate through:

```text
Raw → Lookup → Clean → Summary
```

### 4️⃣ Review the Formulas

Inspect the formulas in the **Clean** and **Summary** sheets to understand how the analysis was created.

### 5️⃣ Explore the Results

Open the **Summary** sheet to view the calculated metrics and chart.

---

## 🎓 Skills Demonstrated

This project demonstrates practical experience with:

```text
📊 Excel Analytics
🧹 Data Cleaning
🔎 XLOOKUP
⚙️ Conditional Logic
📈 COUNTIFS
📉 AVERAGEIFS
🚨 SLA Analysis
📅 Time-Based Analysis
📊 Data Visualization
💼 Business Reporting
```

---

## 🏆 Project Highlights

> **Raw Data → Clean Data → Calculations → Summary → Visualization**

### ✨ What makes this project useful

- ✅ Structured Excel workbook
- ✅ Separate raw and processed data
- ✅ Formula-driven analysis
- ✅ Reusable lookup logic
- ✅ SLA breach identification
- ✅ Department/month analysis
- ✅ Visual summary
- ✅ Easy to understand and modify

---

## 📸 Workbook Preview

### 📊 Summary Dashboard

The **Summary** worksheet provides the final analytical view with SLA-breach calculations, department/month resolution metrics, and a supporting column chart.

> 💡 Add a screenshot of the `Summary` sheet here when publishing the project on GitHub.

```text
📊 SUMMARY
────────────────────────────────────────────

🚨 SLA Breaches by Channel

📧 Email      ████████
💬 Chat       █████
📞 Phone      ████


⏱️ Average Resolution Hours

Department × Month

📈 Performance Trend / Comparison
```

---

## 🚀 Possible Future Improvements

The project can be extended with:

- 📊 Interactive Excel dashboard
- 🎛️ Slicers and filters
- 📈 Additional KPI cards
- 📅 Monthly trend charts
- ⭐ Customer satisfaction analysis
- 🏢 Team-level performance comparison
- 🚨 Automated SLA alerts
- 📉 Resolution-time distribution
- 🔄 Power BI dashboard integration
- 🐍 Python-based analysis

---

## 👨‍💻 Author

# Prince Vaghasiya #

🎓 Diploma — AI/ML & Data Science

📌 **Project:** Customer Support Quality Analysis  
📂 **Category:** Data Analytics  
🛠️ **Primary Tool:** Microsoft Excel

---

## ⭐ Project Status

```text
🟢 Completed
```

If you found this project useful, consider giving the repository a ⭐.

---

<p align="center">
  <b>📊 Turning Support Data Into Actionable Insights</b>
  <br>
  Built with Microsoft Excel • Data Analysis • Business Intelligence
</p>
