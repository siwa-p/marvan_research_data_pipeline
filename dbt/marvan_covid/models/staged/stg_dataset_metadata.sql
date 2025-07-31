{{ config(
    materialized="incremental",
    unique_key="table"
  )
}}

SELECT
  dataset_id,
  country,
  dataset_name,
  description,
  last_updated
FROM {{ source("RAW", "DATASET_METADATA_RAW") }}
