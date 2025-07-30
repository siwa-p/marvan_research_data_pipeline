{{  config(
  materialized="table",
  schema="CLEANED"
)
}}

SELECT
   "date",
   "epiweek",
   "daily_case_count",
    CURRENT_TIMESTAMP AS LAST_UPDATED
FROM {{ source("STAGED", "STG_UK_COVCASESBYDAY") }}
