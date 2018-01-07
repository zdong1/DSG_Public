# This is an example based on the 2010 -> 1990 crosswalk files
# Replace the schema name into the schema into the scheme you use
USE new_schema;

# Check if the weight looks right. If not you need the following code to set weight variable as DOUBLE
# ALTER TABLE filename MODIFY weight DOUBLE;
SELECT af1 AS 'weight'
FROM file1
ORDER BY weight;

SELECT cty10, 
	GROUP_CONCAT(DISTINCT cty90), 
	COUNT(DISTINCT cty90) 
	FROM file4
	 WHERE af10_90< 0.99 AND af10_90 > 0.01
    GROUP BY cty10;

SELECT cty10 AS  '2010 Origin',
	cty90 AS '1990 Destination',
    af10_90 AS 'Weight'
    FROM file4
    WHERE af10_90<0.99
    AND af10_90>0.01
    AND cty10 IN
	(
	SELECT cty90 FROM file4
	);



SELECT 
DISTINCT
cty10  AS 'Missing Counties'
	FROM file4
	WHERE cty10 NOT IN
	(
	SELECT cty90 FROM file4
	);


SELECT 
DISTINCT
cty10 AS 'Emerged Counties'
FROM file4
WHERE cty90 NOT IN
(
SELECT cty10 FROM file4
);
