# Data Engineering Platform for Scalable Data Processing

## Table of Contents
- Overview
- Background
- Requirement
- Architecture Overview
- Implementation
- Demonstrattion of functionality
- Key features
- Challenges encountered
- Lessons learned

## Overview
Predicting employee salaries is essential for HR departments to ensure fair compensation practices, effective budget planning, and enhanced employee satisfaction. This project showcases the design and implementation of a comprehensive data engineering platform for analyzing streaming data from the HR department. The platform integrates multiple components for data ingestion, storage, processing, aggregation, and visualization, providing real-time insights and supporting data-driven decision-making.

## Background
This repository contains the code and configuration files for a
scalable data engineering platform built using AWS services to develop the .
In modern data-driven organizations, the ability to efficiently
ingest, store, process, aggregate, and visualize large volumes of data
is critical. This project aims to design and implement a scalable data
engineering platform using AWS services to handle data sizes ranging
from 10MB to 100GB. The platform will enable real-time data ingestion,
scalable data storage, efficient data processing, and insightful data
visualization.

## Requirement
Design the high-level architecture of the data engineering platform, including the following components:
   - Data Ingestion
   - Data Storage
   - Data Processing
   - Data Aggregation
   - Data Visualization


## Architecture Overview
![Architecture Diagram](/Architechture-diagram.png)

### Design Components
#### Data Ingestion
- AWS Kinesis Data Streams: Used for real-time data ingestion from
various sources.
- AWS Firehose: Buffers and batches incoming data before storing it in AWS S3.

#### Data Storage
- AWS S3: Provides durable and scalable storage for raw and processed data.

#### Data Processing
- AWS Glue: A managed ETL service that processes and transforms data
stored in S3.

#### Data Aggregation
- AWS Redshift: A data warehouse that aggregates processed data for
fast querying and analysis.

#### Data Visualization
- AWS QuickSight: A BI service that provides interactive dashboards
and visualizations of aggregated data.


## Implementation
### Repository Structure - Code samples, scripts, and configuration files

- `ingestion/`: Code and configurations for data ingestion.
- `storage/`: S3 bucket configurations.
- `processing/`: AWS Glue job scripts.
- `aggregation/`: Redshift configurations and queries.
- `visualization/`: QuickSight dashboard configurations.

## Directory Structure

![DS](./images/directory_structure.JPG)

### Setup Instructions

#### Set up AWS Kinesis Data Streams and AWS Firehose for data ingestion.

- Refer the kinesis_stream_configuration.json and setup the AWS Kinesis Data Streams as below:
![Kenesis Data Stream](./images/kenesis_stream.JPG)

- Refer the firehose_stream_configuration.json and setup the AWS Kinesis Data Streams as below:
![Kenesis Firehose](./images/kenesis_stream.JPG)

2. Configure an S3 bucket for raw data storage as files.

- Refer the s3_bucket_acl.json, s3_bucket_location.json and  s3_bucket_policy.json and setup the AWS S3 bucket as below:
![Kenesis Firehose](./images/s3_bucket.JPG)


3. Set up AWS Glue for data processing, including creating Glue jobs for ETL 
    to trasform data from S3 to Redshift tables after processing cleaning.

- Refer the aws-glue-job-ade.py and setup the AWS Glue with Spark as below:
![Kenesis Firehose](./images/glue_studio.JPG)

4. Configure AWS Redshift for data aggregation and create necessary tables.

- Refer the redshift_cluster_properties.json and employee_info.sql and setup the AWS Redshift as below:
![Kenesis Firehose](./images/redshift_cluster.JPG)

- Redshift Editor
![Kenesis Firehose](./images/redshift_editor.JPG)

5. Set up AWS QuickSight for data visualization and create sample dashboards.
- Create an account in AWS Quicksight
- Select datasource as Redshift and select the Redshift clustername to load the data

## Model Development and Deployment
- Please refer the https://github.com/soumalyamondal-iitj/dataanalytics_aws/edit/main/SalaryAnalytics.py for the model implementation. We evaluated LinearRegression, DecisionTreeRegressor, RandomForestRegressor models and based on the RMSE values, RandomForest is determined as best fit model
- This model uses data from S3 which is stored through the data streaming
- Model is registered in MLFlow to track and log all the details of your machine learning experiments, including parameters, metrics, artifacts (such as models), and source code.

  ### Model Architecture and Deployment digaram:
  
  ![Model](./images/Model_Building_deployment_architecture.png)

  ### MLFlow - Tracking of model parameters
  
  ![Model](./images/HuggingFace.png)
  
  ### Deployment in Huggingface

  Public URL for model: https://huggingface.co/spaces/soumalya-iitj/HRAnalytics_PredictSalary
  
  ![Model](./images/HuggingFace.png)


## Demonstrattion of Data Visualization 

- [HR Analytics Visualization-QuickSight](./visualization/HRAnalytics-Visualization-QuickSight.pdf)
  ![QuickSight](./visualization/HRAnalytics-Visualization-QuickSight.png)


## Key Features
### Data Storage
- **Scalable Storage**:
  - AWS S3 for storing raw and processed data.

### Data Processing
- **ETL (Extract, Transform, Load)**:
  - AWS Glue for data transformation and processing.
  - Glue jobs for cleaning and enriching data.

### Data Aggregation
- **Data Warehousing**:
  - AWS Redshift for data aggregation and fast querying.
  - Optimized queries for performance.

### Data Visualization
- **Business Intelligence (BI)**:
  - AWS QuickSight for interactive dashboards and visualizations.

## Challenges encountered
- Acces issues for resources
    a. Setting correct IAM role for resources
    b. VPC and v-net setting
- Data type mismatch issue during data loading to Redshift
- Ensuring the platform can handle varying data sizes
efficiently.
- Structuring S3 buckets for efficient data management.
- Implementing robust validation and cleansing processes.
- Optimizing Redshift queries for large datasets.


## Lessons learned
- It's crucial to design the data flow to
handle peak loads without data loss.
- Properly configuring buffer sizes and
intervals in Kinesis Firehose can significantly improve performance.
- Structuring S3 data with appropriate
prefixes improves data retrieval efficiency.
- Well-designed Redshift queries are
essential for fast and efficient data aggregation.
- Creating responsive and interactive
dashboards in QuickSight enhances user experience.
- Implementing detailed IAM policies helps
in maintaining secure and controlled access to resources.
- Setting up proper logging and monitoring helps in troubleshooting the issue




