# Task 2 - SQL | Customer Support Quality Analysis

**Assigned Set:** Set B  
**SQL dialect:** MySQL 8.0  
**Execution order:** `sql/setup.sql` first, then `sql/queries.sql`

## Objective
Analyze customer-support resolution performance and SLA breaches using the supplied Set B synthetic data.

## Data handling
- `tickets` contains exactly 12 unique fact rows after removing the intentional duplicate.
- `teams` contains 4 lookup rows.
- `team_id` is the primary lookup key.
- `tickets.team_id` references `teams.team_id` through a foreign key.

## Files
- `sql/setup.sql` — creates both tables and inserts the required data.
- `sql/queries.sql` — contains S2a, S2b, S2c and the S3 diagnostic query.
- `outputs/sql/` — saved results for the analytical queries and integrity check.

## Results
### S2a - Average resolution time by department
- Technical: 28.33 hours
- Service: 19.33 hours

### S2b - Teams breaching SLA
Teams with average resolution time above 24 hours:
- T3 / AppSupport: 28.67 hours
- T4 / DeviceHelp: 28.00 hours
- T2 / BillingHelp: 26.67 hours

### S2c - Top two channels by breach count
- Chat: 3 breaches
- Phone: 2 breaches

### S3 - Data integrity
All four team IDs match the lookup table. The unmatched count is zero for every team.

## Reproduction
1. Open MySQL 8.0.
2. Run `sql/setup.sql`.
3. Run `sql/queries.sql`.
4. Compare the generated results with the CSV files in `outputs/sql/`.
