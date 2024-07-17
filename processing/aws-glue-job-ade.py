import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from recipe_transforms import *
from awsglue.dynamicframe import DynamicFrame
from awsglue import DynamicFrame

# Generated recipe steps for DataPreparationRecipe_node1721136708296
def applyRecipe_node1721136708296(inputFrame, glueContext, transformation_ctx):
    frame = inputFrame.toDF()
    gc = glueContext
    df0 = frame
    return DynamicFrame.fromDF(df0, gc, transformation_ctx)

args = getResolvedOptions(sys.argv, ['JOB_NAME'])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# Script generated for node Amazon-S3-Glue-ade
AmazonS3Glueade_node1721135816219 = glueContext.create_dynamic_frame.from_options(format_options={"multiline": False}, connection_type="s3", format="json", connection_options={"paths": ["s3://s3-kinesis-etl-bucket-ade"], "recurse": True}, transformation_ctx="AmazonS3Glueade_node1721135816219")

# Script generated for node Data Preparation Recipe
# Adding configuration for certain Data Preparation recipe steps to run properly
spark.conf.set("spark.sql.legacy.timeParserPolicy", "LEGACY")
# Recipe name: DataPreparationRecipe_node1721136708296
DataPreparationRecipe_node1721136708296 = applyRecipe_node1721136708296(
    inputFrame=AmazonS3Glueade_node1721135816219,
    glueContext=glueContext,
    transformation_ctx="DataPreparationRecipe_node1721136708296")

# Script generated for node Amazon-Redshift-Glue-Ade
AmazonRedshiftGlueAde_node1721136079028 = glueContext.write_dynamic_frame.from_options(frame=DataPreparationRecipe_node1721136708296, connection_type="redshift", connection_options={"postactions": "BEGIN; MERGE INTO dev.employee_info_glue USING dev.employee_info_glue_temp_p33cbo ON employee_info_glue.employeeid = employee_info_glue_temp_p33cbo.employeeid WHEN MATCHED THEN UPDATE SET unnamed: 0 = employee_info_glue_temp_p33cbo.unnamed: 0, employeeid = employee_info_glue_temp_p33cbo.employeeid, age = employee_info_glue_temp_p33cbo.age, gender = employee_info_glue_temp_p33cbo.gender, department = employee_info_glue_temp_p33cbo.department, yearsofexperience = employee_info_glue_temp_p33cbo.yearsofexperience, educationlevel = employee_info_glue_temp_p33cbo.educationlevel, salary = employee_info_glue_temp_p33cbo.salary, performancerating = employee_info_glue_temp_p33cbo.performancerating, worklifebalance = employee_info_glue_temp_p33cbo.worklifebalance, employeesatisfaction = employee_info_glue_temp_p33cbo.employeesatisfaction, traininghours = employee_info_glue_temp_p33cbo.traininghours, yearsincurrentrole = employee_info_glue_temp_p33cbo.yearsincurrentrole, yearssincelastpromotion = employee_info_glue_temp_p33cbo.yearssincelastpromotion, yearswithcurrentmanager = employee_info_glue_temp_p33cbo.yearswithcurrentmanager, attrition = employee_info_glue_temp_p33cbo.attrition, projectinvolvement = employee_info_glue_temp_p33cbo.projectinvolvement, skills = employee_info_glue_temp_p33cbo.skills, trainingeffectiveness = employee_info_glue_temp_p33cbo.trainingeffectiveness, certification = employee_info_glue_temp_p33cbo.certification, lasttrainingdate = employee_info_glue_temp_p33cbo.lasttrainingdate WHEN NOT MATCHED THEN INSERT VALUES (employee_info_glue_temp_p33cbo.unnamed: 0, employee_info_glue_temp_p33cbo.employeeid, employee_info_glue_temp_p33cbo.age, employee_info_glue_temp_p33cbo.gender, employee_info_glue_temp_p33cbo.department, employee_info_glue_temp_p33cbo.yearsofexperience, employee_info_glue_temp_p33cbo.educationlevel, employee_info_glue_temp_p33cbo.salary, employee_info_glue_temp_p33cbo.performancerating, employee_info_glue_temp_p33cbo.worklifebalance, employee_info_glue_temp_p33cbo.employeesatisfaction, employee_info_glue_temp_p33cbo.traininghours, employee_info_glue_temp_p33cbo.yearsincurrentrole, employee_info_glue_temp_p33cbo.yearssincelastpromotion, employee_info_glue_temp_p33cbo.yearswithcurrentmanager, employee_info_glue_temp_p33cbo.attrition, employee_info_glue_temp_p33cbo.projectinvolvement, employee_info_glue_temp_p33cbo.skills, employee_info_glue_temp_p33cbo.trainingeffectiveness, employee_info_glue_temp_p33cbo.certification, employee_info_glue_temp_p33cbo.lasttrainingdate); DROP TABLE dev.employee_info_glue_temp_p33cbo; END;", "redshiftTmpDir": "s3://aws-glue-assets-381492295267-ap-south-1/temporary/", "useConnectionProperties": "true", "dbtable": "dev.employee_info_glue_temp_p33cbo", "connectionName": "Redshift connection", "preactions": "CREATE TABLE IF NOT EXISTS dev.employee_info_glue (unnamed: 0 INTEGER, employeeid INTEGER, age INTEGER, gender VARCHAR, department VARCHAR, yearsofexperience INTEGER, educationlevel INTEGER, salary INTEGER, performancerating INTEGER, worklifebalance INTEGER, employeesatisfaction INTEGER, traininghours INTEGER, yearsincurrentrole INTEGER, yearssincelastpromotion INTEGER, yearswithcurrentmanager INTEGER, attrition VARCHAR, projectinvolvement VARCHAR, skills VARCHAR, trainingeffectiveness INTEGER, certification VARCHAR, lasttrainingdate VARCHAR); DROP TABLE IF EXISTS dev.employee_info_glue_temp_p33cbo; CREATE TABLE dev.employee_info_glue_temp_p33cbo (unnamed: 0 INTEGER, employeeid INTEGER, age INTEGER, gender VARCHAR, department VARCHAR, yearsofexperience INTEGER, educationlevel INTEGER, salary INTEGER, performancerating INTEGER, worklifebalance INTEGER, employeesatisfaction INTEGER, traininghours INTEGER, yearsincurrentrole INTEGER, yearssincelastpromotion INTEGER, yearswithcurrentmanager INTEGER, attrition VARCHAR, projectinvolvement VARCHAR, skills VARCHAR, trainingeffectiveness INTEGER, certification VARCHAR, lasttrainingdate VARCHAR);"}, transformation_ctx="AmazonRedshiftGlueAde_node1721136079028")

job.commit()