
SELECT
    tm.department,
    ROUND(AVG(t.resolution_hours), 2) AS avg_resolution_hours
FROM tickets AS t
JOIN teams AS tm
    ON t.team_id = tm.team_id
GROUP BY tm.department
ORDER BY avg_resolution_hours DESC;

-- S2b - Teams breaching SLA
SELECT
    tm.team_id,
    tm.team,
    ROUND(AVG(t.resolution_hours), 2) AS avg_resolution_hours
FROM tickets AS t
JOIN teams AS tm
    ON t.team_id = tm.team_id
GROUP BY tm.team_id, tm.team
HAVING AVG(t.resolution_hours) > 24
ORDER BY avg_resolution_hours DESC, tm.team_id ASC;

-- S2c - Top two channels by breach count
SELECT
    t.channel,
    COUNT(*) AS breach_count
FROM tickets AS t
WHERE t.resolution_hours > 24
GROUP BY t.channel
ORDER BY breach_count DESC, t.channel ASC
LIMIT 2;

-- S3 - Diagnostic check: every team_id in tickets should match teams.
SELECT
    tm.team_id,
    tm.team,
    COUNT(t.ticket_id) AS ticket_count,
    COUNT(t.ticket_id) - COUNT(tm.team_id) AS unmatched_count
FROM teams AS tm
LEFT JOIN tickets AS t
    ON tm.team_id = t.team_id
GROUP BY tm.team_id, tm.team
ORDER BY tm.team_id;
