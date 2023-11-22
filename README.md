# Project-STEDI
Project Data
STEDI has three JSON data sources to use from the Step Trainer.

customer
step_trainer
accelerometer

### 1. Customer Records
This is the data from fulfillment and the STEDI website.

AWS S3 Bucket URI - s3://cd0030bucket/customers/
contains the following fields:

serialnumber
sharewithpublicasofdate
birthday
registrationdate
sharewithresearchasofdate
customername
email
lastupdatedate
phone
sharewithfriendsasofdate

### 2. Step Trainer Records
This is the data from the motion sensor.
AWS S3 Bucket URI - s3://cd0030bucket/step_trainer/
contains the following fields:

sensorReadingTime
serialNumber
distanceFromObject

### 3. Accelerometer Records
This is the data from the mobile app.
AWS S3 Bucket URI - s3://cd0030bucket/accelerometer/
contains the following fields:

timeStamp
user
x
y
z

## Project Instructions

Using AWS Glue, AWS S3, Python, and Spark, create or generate Python scripts to build a lakehouse solution in AWS that satisfies these requirements from the STEDI data scientists.

Refer to the flowchart below to better understand the workflow.
![image](https://github.com/HenryHai0407/Project-STEDI/assets/87645090/8fedebbb-cf06-479a-9256-25c5667fa6c2)

