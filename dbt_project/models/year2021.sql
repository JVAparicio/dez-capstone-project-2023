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
    FROM {{ source('staging','data-2021-21') }}
    WHERE ISO3='USA'
    


-- SELECT * EXCEPT (Date, People_Tested, Mortality_Rate) FROM `hip-watch-375918.covid.test2022` LIMIT 10;

-- fullname	mode	type	description
-- Province_State		STRING	
-- Country_Region		STRING	
-- Last_Update		TIMESTAMP	
-- Lat		FLOAT	
-- Long_		FLOAT	
-- Confirmed		INTEGER	
-- Deaths		INTEGER	
-- Recovered		FLOAT	
-- Active		FLOAT	
-- FIPS		FLOAT	
-- Incident_Rate		FLOAT	
-- Total_Test_Results		FLOAT	
-- People_Hospitalized		STRING	
-- Case_Fatality_Ratio		FLOAT	
-- UID		FLOAT	
-- ISO3		STRING	
-- Testing_Rate		FLOAT	
-- Hospitalization_Rate		STRING	
-- Date		DATE	
-- People_Tested		STRING	
-- Mortality_Rate		STRING	