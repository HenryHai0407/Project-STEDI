CREATE EXTERNAL TABLE IF NOT EXISTS customer_landing (
  customerName STRING,
  email STRING,
  phone STRING,
  birthDay STRING,
  serialNumber STRING,
  registrationDate STRING,
  lastUpdateDate STRING,
  shareWithResearchAsOfDate BIGINT,
  shareWithPublicAsOfDate BIGINT
)
ROW FORMAT SERDE 'org.openx.data.jsonserde.JsonSerDe'
WITH SERDEPROPERTIES (
  'serialization.format' = '1'
)
LOCATION 's3://hainguyen/customer/landing/'
