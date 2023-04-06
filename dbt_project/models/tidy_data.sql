{{ config(materialized='table') }}

SELECT * FROM {{ ref('year2021') }}
UNION ALL 
SELECT * FROM {{ ref('year2022') }}
