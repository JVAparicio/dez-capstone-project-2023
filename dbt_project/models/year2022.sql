SELECT
        Province_State as State,
        CAST(Confirmed as numeric) as Confirmed,
        CAST(Deaths as numeric) as Deaths,
        CAST(Recovered as numeric) as Recovered,
        CAST(Active as numeric) as Active,
        CAST(Incident_Rate as float64) as Incident_Rate,
        -- CAST(Total_Test_Results as numeric) as Total_Test_Results,
        CAST(Case_Fatality_Ratio as float64) as Case_Fatality_Ratio,
        CAST(Testing_Rate as float64) as Testing_Rate,
        -- ST_GeogPoint(Long_, Lat) AS Geo,
        -- Long_ as Long,
        -- Lat,
        -- CAST(FIPS as integer) as FIPS,
        Date,
        EXTRACT(Month FROM `Date`) as Month,
        EXTRACT(Year FROM `Date`) as Year
    FROM {{ source('staging','data-2022-18') }}
    WHERE ISO3='USA'

UNION ALL

SELECT
        Province_State as State,
        CAST(Confirmed as numeric) as Confirmed,
        CAST(Deaths as numeric) as Deaths,
        CAST(Recovered as numeric) as Recovered,
        CAST(Active as numeric) as Active,
        CAST(Incident_Rate as float64) as Incident_Rate,
        -- CAST(Total_Test_Results as numeric) as Total_Test_Results,
        CAST(Case_Fatality_Ratio as float64) as Case_Fatality_Ratio,
        CAST(Testing_Rate as float64) as Testing_Rate,
        -- ST_GeogPoint(Long_, Lat) AS Geo,
        -- Long_ as Long,
        -- Lat,
        -- CAST(FIPS as integer) as FIPS,
        Date,
        EXTRACT(Month FROM `Date`) as Month,
        EXTRACT(Year FROM `Date`) as Year
    FROM {{ source('staging','data-2022-21') }}
    WHERE ISO3='USA'
