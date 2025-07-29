{{ config(
    materialized="incremental",
    unique_key="VECTOR"
  )
}}

SELECT
    REF_DATE,
    DGUID,
    "North American Industry Classification System (NAICS)",
    "COVID-19 rapid test kits demand and usage",
    VECTOR,
    COORDINATE,
    VALUE as PERCENT,
    STATUS as DATA_QUALITY_RATING
FROM {{ source("RAW", "CA_ANTIBODY_RAW") }}
WHERE GEO = 'Canada'
