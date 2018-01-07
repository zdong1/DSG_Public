USE new_schema;
ALTER TABLE tab1 MODIFY OriginID int;

## Set up main data and converter
SELECT OriginID AS 'origin',
	DestinationID AS 'destination',
  TravelCost AS 'time',
  NewID AS 'New_ID'
    FROM tab1
	WHERE TravelCost<5
  ORDER BY OriginID;
  

## Converter
SELECT C1 AS 'prior',
  C2 AS 'post'
  FROM convID
  ORDER BY C1;

SELECT
DISTINCT
  tab1.OriginID, tab1.DestinationID, tab1.DestinationRank,
  tab1.TravelCost, convID.C1 as 'ValidatorID', convID.C2 as 'MatchedID'
  FROM tab1
  INNER JOIN convID ON
      tab1.DestinationID=convID.C1;




## Create Subsets

SELECT OriginID AS 'OriginID',
	GROUP_CONCAT(DISTINCT RealRetID) AS Id_5,
	COUNT(RealRetID) AS Co_5
    FROM tab2
    WHERE TravelCost<=5
    GROUP BY OriginID;


SELECT OriginID AS 'OriginID',
	GROUP_CONCAT(DISTINCT RealRetID) AS Id_10,
	COUNT(RealRetID) AS Co_10
    FROM tab2
    WHERE TravelCost>5 AND TravelCost<=10
    GROUP BY OriginID;
    

SELECT OriginID AS 'OriginID',
	GROUP_CONCAT(DISTINCT RealRetID) As Id_15,
	COUNT(RealRetID) AS Co_15
    FROM tab2
    WHERE TravelCost>10 AND TravelCost<=15
    GROUP BY OriginID;
    

SELECT OriginID AS 'OriginID',
	GROUP_CONCAT(DISTINCT RealRetID) AS Id_20,
	COUNT(RealRetID) AS Co_20
    FROM tab2
    WHERE TravelCost>15 AND TravelCost<=20
    GROUP BY OriginID;
    

SELECT OriginID AS 'OriginID',
	GROUP_CONCAT(DISTINCT RealRetID) AS Id_30,
	COUNT(RealRetID) AS Co_30
    FROM tab2
    WHERE TravelCost>20 AND TravelCost<=30
    GROUP BY OriginID;
    

SELECT OriginID AS 'OriginID',
	GROUP_CONCAT(DISTINCT RealRetID) AS Id_40,
	COUNT(RealRetID) As Co_40
    FROM tab2
    WHERE TravelCost>30 AND TravelCost<=40
    GROUP BY OriginID;
    

SELECT OriginID AS 'OriginID',
	GROUP_CONCAT(DISTINCT RealRetID) AS Id_50,
	COUNT(RealRetID) as Co_50
    FROM tab2
    WHERE TravelCost>40 AND TravelCost<=50
    GROUP BY OriginID;
    

SELECT OriginID AS 'OriginID',
	GROUP_CONCAT(DISTINCT RealRetID) AS Id_60,
	COUNT(RealRetID) as Co_60
    FROM tab2
    WHERE TravelCost>50 AND TravelCost<=60
    GROUP BY OriginID;
    

SELECT OriginID AS 'OriginID',
	GROUP_CONCAT(DISTINCT RealRetID) AS Id_70,
	COUNT(RealRetID) AS Co_70
    FROM tab2
    WHERE TravelCost>60 AND TravelCost<=70
    GROUP BY OriginID;
    

SELECT OriginID AS 'OriginID',
	GROUP_CONCAT(DISTINCT RealRetID) AS Id_80,
	COUNT(RealRetID) AS Co_80
    FROM tab2
    WHERE TravelCost>70 AND TravelCost<=80
    GROUP BY OriginID;
    

SELECT OriginID AS 'OriginID',
	GROUP_CONCAT(DISTINCT RealRetID) AS Id_90,
	COUNT(RealRetID) as Co_90
    FROM tab2
    WHERE TravelCost>80 AND TravelCost<=90
    GROUP BY OriginID;
    

