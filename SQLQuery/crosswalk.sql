# CSDE Summer 2017  Author: Zhihang Dong
# This code was written in MySQL Workbench 6.3.9.CE and was successfully compiled with 0 errors and 0 warnings.
# Each Chunk represents a query, and has to be run separately.

# Replace the schema name into the schema into the scheme you use
USE new_schema;

# Check if the weight looks right. If not you need the following code to set weight variable as DOUBLE
# ALTER TABLE filename MODIFY weight DOUBLE;
SELECT af1 AS 'weight'
FROM file1
ORDER BY weight;

# Query 1: Where did the 1970 county reapportioned to by 1990? This is an example based on the 1970 -> 1990 crosswalk files
SELECT cty70, 
	GROUP_CONCAT(DISTINCT cty90), 
	COUNT(DISTINCT cty90) 
	FROM file1
	WHERE af1< 0.99 AND af1> 0.01
    GROUP BY cty70;

# Query 2: Choose reapportionments with only more than 2% of its original county (as indicated by weight) to reject cases of small cartographical errors
# Warning: This query EXCLUDES the counties that are missing by 1990 or emerged as NEW in 1990, if you don't want to do this,
# PLEASE REMOVE Line 32 - 35, with semicolon(;) followed Line 31.

SELECT cty70 AS  '1970 Origin',
	cty90 AS '1990 Destination',
    af1 AS 'Weight'
    FROM file1
    WHERE af1<0.99
    AND af1>0.01
    AND cty70 IN
	(
	SELECT cty90 FROM file1
	);

 
# Query 3: Look at how many of the old counties in 1970 disappeared, query distinct values in MySQL
		
SELECT 
DISTINCT
cty70  AS 'Missing Counties'
	FROM file1
	WHERE cty70 NOT IN
	(
	SELECT cty90 FROM file1
	);
# 16 counties disappeared. Based on the number of observations


# Query 4: Now look at how many of the new counties emerged as of 1990

SELECT 
DISTINCT
cty90 AS 'Emerged Counties'
FROM file1
WHERE cty90 NOT IN
(
SELECT cty70 FROM file1
);
# 16 counties emerged. Based on the number of observations.
