CREATE EXTERNAL TABLE IF NOT EXISTS `hoanghai_database`.`accelerometer_customer_curated` (
  `user` string,
  `timeStamp` bigint,
  `x` float,
  `y` float,
  `z` float,
  `serialNumber` string,
  `shareWithPublicAsOfDate` bigint,
  `birthDay` string,
  `registrationDate` bigint,
  `shareWithResearchAsOfDate` bigint,
  `customerName` string,
  `email` string,
  `lastUpdateDate` bigint,
  `phone` string
)
ROW FORMAT SERDE 'org.openx.data.jsonserde.JsonSerDe'
WITH SERDEPROPERTIES (
  'ignore.malformed.json' = 'FALSE',
  'dots.in.keys' = 'FALSE',
  'case.insensitive' = 'TRUE',
  'mapping' = 'TRUE'
)
STORED AS INPUTFORMAT 'org.apache.hadoop.mapred.TextInputFormat' OUTPUTFORMAT 'org.apache.hadoop.hive.ql.io.HiveIgnoreKeyTextOutputFormat'
LOCATION 's3://hainguyen/accelerometer/curated/'
TBLPROPERTIES ('classification' = 'json');
