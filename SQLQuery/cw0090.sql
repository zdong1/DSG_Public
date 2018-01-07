# handle 2000 -> 1990 crosswalk

SELECT cty00, 
	GROUP_CONCAT(DISTINCT cty90), 
	COUNT(DISTINCT cty90) 
	FROM file3
	 WHERE af1< 0.99 AND af1> 0.01
    GROUP BY cty00;

SELECT cty00 AS  '2000 Origin',
	cty90 AS '1990 Destination',
    af1 AS 'Weight'
    FROM file3
    WHERE af1<0.99
    AND af1>0.01
    AND cty00 IN
	(
	SELECT cty90 FROM file3
	);



SELECT 
DISTINCT
cty00  AS 'Missing Counties'
	FROM file3
	WHERE cty00 NOT IN
	(
	SELECT cty90 FROM file3
	);


SELECT 
DISTINCT
cty00 AS 'Emerged Counties'
FROM file3
WHERE cty90 NOT IN
(
SELECT cty00 FROM file3
);

