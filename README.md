# 📊 Customer Support Quality Analysis — Excel

<div align="center">

### Excel-Based Customer Support & SLA Performance Analysis

**Microsoft Excel • Data Cleaning • COUNTIFS • KPIs • Pivot Analysis • SLA Monitoring**

</div>

---

## 📌 Project Overview

This project analyzes customer-support ticket data using **Microsoft Excel** to evaluate SLA performance, resolution time, customer satisfaction, and channel-level support performance.

The analysis follows a practical data-analysis workflow:

```text
Raw Data
   ↓
Data Cleaning
   ↓
Duplicate Removal
   ↓
Derived Fields
   ↓
SLA Analysis
   ↓
Summary Tables
   ↓
Business Insights
```

---

## 🎯 Business Objective

The objective is to understand:

- How many support tickets breach the SLA?
- Which channels have the highest number of breaches?
- What is the average resolution time?
- How satisfied are customers?
- Which support areas require attention?

The project demonstrates how Excel can be used to transform raw operational data into useful business insights.

---

## 📊 Executive Summary

After cleaning the dataset:

| KPI | Result |
|---|---:|
| Clean Tickets | **12** |
| SLA Breaches | **5** |
| SLA Breach Rate | **41.7%** |
| Average Resolution Time | **23.83 hrs** |
| Average Satisfaction | **3.58 / 5** |
| Duplicate Records Removed | **1** |

### Channel-Level Breaches

| Channel | Breaches |
|---|---:|
| Chat | **3** |
| Phone | **2** |
| Email | **0** |

Chat has the highest number of SLA breaches in the dataset.

---

## 🧹 Data Cleaning

The Excel workflow includes:

- Duplicate-record detection
- Duplicate removal
- Data validation
- Resolution-time analysis
- SLA classification
- Summary calculations

One duplicate record was identified and removed, resulting in **12 clean tickets**.

---

## 🚨 SLA Analysis

The project uses a **24-hour SLA threshold**.

A ticket is classified as breached when:

```excel
=IF(resolution_hours>24,1,0)
```

This creates a `breach_flag` field:

| Condition | Flag |
|---|---:|
| Resolution ≤ 24 hours | 0 |
| Resolution > 24 hours | 1 |

---

## 📈 Key Findings

### SLA Performance

- **5 of 12 tickets** breached the SLA.
- Overall SLA breach rate was **41.7%**.
- Chat recorded the highest number of breaches.
- Email recorded **zero breaches**.

### Resolution Performance

Average resolution time:

**23.83 hours**

### Customer Satisfaction

Average satisfaction:

**3.58 / 5**

---

## 📅 Monthly Analysis

The project also analyzes average resolution time by department and month.

### Technical

| Month | Average Resolution |
|---|---:|
| Jan | **28 hrs** |
| Feb | **29 hrs** |
| Mar | **28 hrs** |

### Service

| Month | Average Resolution |
|---|---:|
| Jan | **20 hrs** |
| Feb | **19 hrs** |
| Mar | **19 hrs** |

Technical support consistently shows higher average resolution times than Service.

---

## 🧮 Excel Functions Used

The project demonstrates practical Excel functions including:

```text
IF
COUNTIFS
AVERAGE
SUM
ROUND
```

The analysis also demonstrates:

- Relative formulas
- Derived columns
- Summary tables
- KPI calculations
- Channel analysis

---

## 📂 Project Structure

```text
Excel Task/
│
├── raw/
│   └── support_tickets.csv
│
├── Excel/
│   └── Customer_Support_Analysis.xlsx
│
├── outputs/
│   └── summary/
│
└── README.md
```

---

## 🛠️ Tools Used

- Microsoft Excel
- Excel formulas
- Data cleaning
- Conditional analysis
- Summary tables

---

## 💼 Skills Demonstrated

### Data Analysis

- Data cleaning
- Duplicate handling
- KPI calculation
- SLA analysis
- Operational reporting

### Excel

- `IF`
- `COUNTIFS`
- `AVERAGE`
- `SUM`
- `ROUND`
- Derived fields
- Summary tables

### Business Analysis

- Support-channel analysis
- SLA monitoring
- Resolution-time analysis
- Customer satisfaction analysis

---

## 🚀 Future Improvements

Possible extensions include:

- Interactive Excel dashboard
- PivotCharts
- Monthly SLA trend
- Team-level performance
- Customer satisfaction segmentation
- Conditional-formatting KPI cards
- Automated reporting

---

## 👨‍💻 Author

# Prince Vaghasiya #

Diploma — AI/ML & Data Science  
Vidhyadeep University

**Skills:**  
`Excel` • `SQL` • `Python` • `Power BI` • `Data Analysis`

---

<div align="center">

### ⭐ Customer Support Quality Analysis

**Turning support data into actionable operational insights.**

</div>
