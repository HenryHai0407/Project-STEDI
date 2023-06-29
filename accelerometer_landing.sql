CREATE EXTERNAL TABLE hoanghai_database.accelerometer_landing (
  user string,
  timestamp bigint,
  x float,
  y float,
  z float
)
ROW FORMAT SERDE 'org.openx.data.jsonserde.JsonSerDe'
WITH SERDEPROPERTIES ('classification'='json')
LOCATION 's3://hainguyen/accelerometer/landing/'
