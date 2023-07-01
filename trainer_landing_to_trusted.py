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

# Script generated for node Step Trainer Landing
StepTrainerLanding_node1 = glueContext.create_dynamic_frame.from_options(
    format_options={"multiline": False},
    connection_type="s3",
    format="json",
    connection_options={
        "paths": ["s3://hainguyen/step_trainer/landing/"],
        "recurse": True,
    },
    transformation_ctx="StepTrainerLanding_node1",
)

# Script generated for node Customer Curated
CustomerCurated_node1688040374620 = glueContext.create_dynamic_frame.from_options(
    format_options={"multiline": False},
    connection_type="s3",
    format="json",
    connection_options={"paths": ["s3://hainguyen/customer/curated/"], "recurse": True},
    transformation_ctx="CustomerCurated_node1688040374620",
)

# Script generated for node Join by serialNumber
JoinbyserialNumber_node1688040432802 = Join.apply(
    frame1=StepTrainerLanding_node1,
    frame2=CustomerCurated_node1688040374620,
    keys1=["serialNumber"],
    keys2=["serialNumber"],
    transformation_ctx="JoinbyserialNumber_node1688040432802",
)

# Script generated for node Drop Fields
DropFields_node1688040544495 = DropFields.apply(
    frame=JoinbyserialNumber_node1688040432802,
    paths=[
        "`.serialNumber`",
        "birthDay",
        "shareWithPublicAsOfDate",
        "shareWithResearchAsOfDate",
        "registrationDate",
        "customerName",
        "email",
        "lastUpdateDate",
        "phone",
    ],
    transformation_ctx="DropFields_node1688040544495",
)

# Script generated for node Step Trainer Trusted
StepTrainerTrusted_node3 = glueContext.write_dynamic_frame.from_options(
    frame=DropFields_node1688040544495,
    connection_type="s3",
    format="json",
    connection_options={
        "path": "s3://hainguyen/step_trainer/trusted/",
        "partitionKeys": [],
    },
    transformation_ctx="StepTrainerTrusted_node3",
)

job.commit()
