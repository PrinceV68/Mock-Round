# 🗃️ Customer Support Quality Analysis — SQL

<div align="center">

### SQL-Based Customer Support & SLA Analysis

**MySQL 8.0 • Joins • Aggregations • HAVING • Filtering • Data Integrity**

</div>

---

## 📌 Project Overview

This project analyzes customer-support ticket data using **MySQL 8.0** to evaluate resolution performance, identify teams exceeding the SLA threshold, analyze breach patterns by support channel, and validate the relationship between ticket and team data.

The project uses a structured relational database containing **12 unique customer-support tickets** and **4 support teams**.

The analysis demonstrates practical SQL skills including:

- Relational table design
- Primary and foreign keys
- `JOIN`
- `GROUP BY`
- Aggregate functions
- `AVG()`
- `COUNT()`
- `HAVING`
- `WHERE`
- `ORDER BY`
- `LIMIT`
- Data-integrity validation

---

## 🎯 Business Objective

The objective is to answer key customer-support performance questions:

> **How efficiently are support teams resolving tickets, where are SLA issues occurring, and which channels contribute most to breaches?**

The SQL analysis focuses on four areas:

| Analysis | Business Question |
|---|---|
| S2a | What is the average resolution time by department? |
| S2b | Which teams have an average resolution time above the 24-hour SLA? |
| S2c | Which support channels have the highest number of SLA breaches? |
| S3 | Are all ticket team IDs correctly connected to the team lookup table? |

---

## 📊 Executive Summary

The analysis reveals a clear difference between the two departments.

- **Technical** support has an average resolution time of **28.33 hours**.
- **Service** support has an average resolution time of **19.33 hours**.
- **3 of 4 teams** have average resolution times above the **24-hour SLA threshold**.
- **AppSupport** has the highest average resolution time at **28.67 hours**.
- **Chat** records the highest number of SLA breaches with **3 breaches**.
- **Phone** follows with **2 breaches**.
- All **4 team IDs** successfully match the team lookup table.

These results provide a compact view of where customer-support resolution performance requires further investigation.

---

# 📈 Key Results

## S2a — Average Resolution Time by Department

| Department | Avg. Resolution Time |
|---|---:|
| Technical | **28.33 hrs** |
| Service | **19.33 hrs** |

The Technical department has a higher average resolution time than Service and is above the 24-hour SLA threshold.

---

## 🚨 S2b — Teams Breaching SLA

The project defines an SLA breach as an average team resolution time **greater than 24 hours**.

| Team ID | Team | Avg. Resolution |
|---|---|---:|
| T3 | AppSupport | **28.67 hrs** |
| T4 | DeviceHelp | **28.00 hrs** |
| T2 | BillingHelp | **26.67 hrs** |

Three teams exceed the defined 24-hour SLA threshold.

`T1 / AccountCare` does not appear in this result because its average resolution time is below the threshold.

---

## 📞 S2c — Top Channels by Breach Count

| Channel | Breach Count |
|---|---:|
| Chat | **3** |
| Phone | **2** |

Chat has the highest number of SLA breaches in the dataset, followed by Phone.

---

## 🔍 S3 — Data Integrity Check

A diagnostic query validates whether every `team_id` appearing in the ticket data exists in the `teams` lookup table.

| Team ID | Team | Tickets | Unmatched |
|---|---|---:|---:|
| T1 | AccountCare | 3 | 0 |
| T2 | BillingHelp | 3 | 0 |
| T3 | AppSupport | 3 | 0 |
| T4 | DeviceHelp | 3 | 0 |

### Integrity Result

**All team IDs are successfully matched.**

There are **zero unmatched records** across all four teams.

---

# 🗂️ Database Structure

The project uses two relational tables.

### `teams`

Lookup/dimension table containing support-team information.

| Column | Description |
|---|---|
| `team_id` | Unique team identifier |
| `team` | Team name |
| `department` | Department classification |

### `tickets`

Fact table containing customer-support ticket information.

| Column | Description |
|---|---|
| `ticket_id` | Unique ticket identifier |
| `month` | Ticket month |
| `team_id` | Related support team |
| `channel` | Support channel |
| `resolution_hours` | Ticket resolution time |
| `satisfaction` | Customer satisfaction score |

### Relationship

```text
teams
  │
  │ team_id
  │
  ▼
tickets
```

The relationship is enforced through a foreign key:

```sql
FOREIGN KEY (team_id)
REFERENCES teams(team_id)
```

---

# 🧹 Data Handling

The supplied dataset contained an intentional duplicate ticket record.

The SQL setup uses **12 unique ticket records** and excludes the duplicate `ticket_id = 12`.

The database structure also applies:

- Primary keys
- Foreign keys
- `NOT NULL` constraints
- Appropriate numeric data types
- Relational integrity checks

---

# 🧠 SQL Analysis

## Department-Level Analysis

The project uses `JOIN`, `AVG()`, `GROUP BY`, and `ORDER BY` to calculate departmental resolution performance.

```sql
SELECT
    tm.department,
    ROUND(AVG(t.resolution_hours), 2) AS avg_resolution_hours
FROM tickets AS t
JOIN teams AS tm
    ON t.team_id = tm.team_id
GROUP BY tm.department
ORDER BY avg_resolution_hours DESC;
```

---

## SLA Breach Analysis

Teams exceeding the 24-hour average resolution threshold are identified using `HAVING`.

```sql
GROUP BY tm.team_id, tm.team
HAVING AVG(t.resolution_hours) > 24
```

This demonstrates the difference between:

- `WHERE` → filters individual rows
- `HAVING` → filters aggregated groups

---

## Channel Breach Analysis

The project counts tickets with resolution times above 24 hours and groups them by support channel.

```sql
SELECT
    t.channel,
    COUNT(*) AS breach_count
FROM tickets AS t
WHERE t.resolution_hours > 24
GROUP BY t.channel
ORDER BY breach_count DESC
LIMIT 2;
```

---

# 📁 Project Structure

```text
SQL Task/
│
├── sql/
│   ├── setup.sql
│   └── queries.sql
│
├── outputs/
│   └── sql/
│       ├── s2a_avg_resolution_by_department.csv
│       ├── s2b_teams_breaching_sla.csv
│       ├── s2c_top_two_channels_by_breach_count.csv
│       └── s3_team_lookup_integrity.csv
│
└── README.md
```

---

# 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| **MySQL 8.0** | Database engine |
| **SQL** | Data analysis and querying |
| **CSV** | Result export |
| **Relational Database Design** | Structured data modeling |

---

# ▶️ How to Run

## 1. Open MySQL 8.0

Create or select the database where you want to run the project.

## 2. Run the setup script

```sql
SOURCE sql/setup.sql;
```

This creates:

```text
teams
tickets
```

and inserts the project data.

## 3. Run the analytical queries

```sql
SOURCE sql/queries.sql;
```

The queries generate the S2a, S2b, S2c, and S3 analysis.

---

# 📤 Generated Outputs

The project includes saved CSV results for reproducibility:

```text
outputs/sql/
│
├── s2a_avg_resolution_by_department.csv
├── s2b_teams_breaching_sla.csv
├── s2c_top_two_channels_by_breach_count.csv
└── s3_team_lookup_integrity.csv
```

This makes it possible to compare the SQL execution results with the expected outputs.

---

# 💼 Skills Demonstrated

### SQL Fundamentals
- `SELECT`
- `WHERE`
- `GROUP BY`
- `ORDER BY`
- `LIMIT`

### SQL Analytics
- `AVG()`
- `COUNT()`
- `ROUND()`
- Aggregation
- SLA analysis
- Group-level filtering with `HAVING`

### Relational Database Skills
- Primary keys
- Foreign keys
- Table relationships
- `INNER JOIN`
- `LEFT JOIN`
- Lookup-table validation

### Data Quality
- Duplicate handling
- Referential integrity
- Unmatched-record detection
- Result validation

---

# 📌 Business Insights

### 1. Technical resolution time is higher

Technical support averages **28.33 hours**, compared with **19.33 hours** for Service.

### 2. Multiple teams exceed the SLA

Three teams have average resolution times above the 24-hour threshold:

```text
AppSupport   → 28.67 hrs
DeviceHelp   → 28.00 hrs
BillingHelp  → 26.67 hrs
```

### 3. Chat has the highest breach count

Chat accounts for **3 SLA breaches**, while Phone accounts for **2**.

### 4. Team mapping is clean

Every ticket team ID successfully maps to a valid team record, with **zero unmatched records**.

---

# 🚀 Possible Future Improvements

The analysis could be extended with:

- Monthly SLA trend analysis
- Customer satisfaction vs. resolution-time analysis
- Channel-level breach percentages
- Team performance ranking tables
- SLA compliance percentage
- Repeat-ticket analysis
- Customer segmentation
- Advanced SQL CTEs
- Window functions
- Automated reporting
- Power BI dashboard integration

---

# 📚 Learning Outcomes

This project demonstrates how SQL can transform raw support-ticket records into structured business insights.

The workflow covers:

```text
Raw Data
   ↓
Relational Tables
   ↓
Data Integrity
   ↓
JOIN
   ↓
Aggregation
   ↓
SLA Analysis
   ↓
Business Insights
   ↓
CSV Outputs
```

---

# 👨‍💻 Project Author

# Prince Vaghasiya #

Diploma — AI/ML & Data Science  
Vidhyadeep University

### Core Skills

`Python` • `SQL` • `Power BI` • `Excel` • `Data Analysis` • `Data Visualization` • `Machine Learning`

---

<div align="center">

### ⭐ Customer Support Quality Analysis

**A practical SQL project focused on relational data analysis, SLA monitoring, and data-quality validation.**

</div>
