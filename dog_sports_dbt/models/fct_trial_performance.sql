{{ config(materialized='table') }}

WITH raw_logs AS (
    -- Reads directly from the data loaded by your Python script
    SELECT * FROM dog_sports_db.raw.trial_logs
)

SELECT
    dog_name,
    sport_type,
    COUNT(trial_id) AS total_entries,
    SUM(CASE WHEN is_qualified THEN 1 ELSE 0 END) AS total_qualifications,
    -- Calculate your passing rate
    ROUND(SUM(CASE WHEN is_qualified THEN 1 ELSE 0 END) / COUNT(trial_id) * 100, 2) AS qualification_rate,
    -- Budget tracking: See how much cash you are routing away from debt payoff
    SUM(entry_fee_usd) AS cumulative_sport_spend_usd
FROM raw_logs
GROUP BY dog_name, sport_type
