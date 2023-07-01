import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job

args = getResolvedOptions(sys.argv, ["JOB_NAME"])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args["JOB_NAME"], args)

# Script generated for node Accelerometer Landing
AccelerometerLanding_node1 = glueContext.create_dynamic_frame.from_options(
    format_options={"multiline": False},
    connection_type="s3",
    format="json",
    connection_options={
        "paths": ["s3://hainguyen/accelerometer/landing/"],
        "recurse": True,
    },
    transformation_ctx="AccelerometerLanding_node1",
)

# Script generated for node Customer Trusted
CustomerTrusted_node1688037897101 = glueContext.create_dynamic_frame.from_options(
    format_options={"multiline": False},
    connection_type="s3",
    format="json",
    connection_options={"paths": ["s3://hainguyen/customer/trusted/"], "recurse": True},
    transformation_ctx="CustomerTrusted_node1688037897101",
)

# Script generated for node Join Customer
JoinCustomer_node1688038215899 = Join.apply(
    frame1=AccelerometerLanding_node1,
    frame2=CustomerTrusted_node1688037897101,
    keys1=["user"],
    keys2=["email"],
    transformation_ctx="JoinCustomer_node1688038215899",
)

# Script generated for node Accelerometer Customer Curated
AccelerometerCustomerCurated_node3 = glueContext.write_dynamic_frame.from_options(
    frame=JoinCustomer_node1688038215899,
    connection_type="s3",
    format="json",
    connection_options={
        "path": "s3://hainguyen/accelerometer/curated/",
        "partitionKeys": [],
    },
    transformation_ctx="AccelerometerCustomerCurated_node3",
)

job.commit()
