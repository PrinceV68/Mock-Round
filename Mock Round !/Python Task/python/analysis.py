import pandas as pd
import matplotlib.pyplot as plt

tickets = pd.read_csv("data/raw/tickets.csv")
teams = pd.read_csv("data/raw/teams.csv")   
# Check numeric columns
tickets["resolution_hours"] = pd.to_numeric(tickets["resolution_hours"])
tickets["satisfaction"] = pd.to_numeric(tickets["satisfaction"])

print("Resolution hours type:", tickets["resolution_hours"].dtype)
print("Satisfaction type:", tickets["satisfaction"].dtype)
print("Rows before removing duplicates:", len(tickets))

# Remove duplicate records
tickets = tickets.drop_duplicates()

print("Rows after removing duplicates:", len(tickets))

# Merge ticket data with team data
data = pd.merge(tickets, teams, on="team_id", how="left")

# Basic checks
assert len(data) == 12
assert data["department"].isna().sum() == 0

# Create breach flag
data["breach_flag"] = (data["resolution_hours"] > 24).astype(int)

# Department summary
department_summary = data.groupby("department").agg(
    total_tickets=("ticket_id", "count"),
    breached_tickets=("breach_flag", "sum")
).reset_index()

department_summary["sla_breach_rate_pct"] = (
    department_summary["breached_tickets"] /
    department_summary["total_tickets"] * 100
).round(2)

print("\nDepartment Summary:")
print(department_summary)

# Team breach rate
team_summary = data.groupby(["team_id", "team"]).agg(
    total_tickets=("ticket_id", "count"),
    breached_tickets=("breach_flag", "sum")
).reset_index()

team_summary["breach_rate_pct"] = (
    team_summary["breached_tickets"] /
    team_summary["total_tickets"] * 100
)

highest_rate = team_summary["breach_rate_pct"].max()
highest_team = team_summary[team_summary["breach_rate_pct"] == highest_rate]

print("\nTeam with highest breach rate:")
print(highest_team[[
    "team_id", "team", "breached_tickets",
    "total_tickets", "breach_rate_pct"
]])

# Monthly average resolution time
month_order = ["Jan", "Feb", "Mar"]

monthly_avg = data.groupby("month")["resolution_hours"].mean()
monthly_avg = monthly_avg.reindex(month_order)

plt.figure(figsize=(8, 5))
monthly_avg.plot(kind="bar")

plt.title("Monthly Average Resolution Time")
plt.xlabel("Month")
plt.ylabel("Average Resolution Hours")
plt.xticks(rotation=0)
plt.tight_layout()

plt.savefig("outputs/python_chart.png")
plt.close()

# Save output files
data.to_csv("outputs/clean_data.csv", index=False)
department_summary.to_csv("outputs/python_summary.csv", index=False)

print("\nAnalysis completed successfully.")
