{{ config(
    materialized='table',
    cluster_by = ["Year", "Month", "State"],
    )
}}

SELECT * FROM {{ ref('tidy_data') }} 