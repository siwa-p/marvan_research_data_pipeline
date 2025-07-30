{{  config(
  materialized="incremental"
)
}}

SELECT
   TO_DATE("date") AS "date",
   "epiweek",
   "metric_value"::INTEGER AS "daily_case_count"
FROM {{ source("RAW", "UK_COVCASESBYDAY_RAW") }}
