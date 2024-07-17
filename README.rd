#Data Engineering Platform for Scalable Data Processing

## Background
This repository contains the code and configuration files for a
scalable data engineering platform built using AWS services.
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

![Architecture Diagram](./architecture-diagram.png)

###Design Components
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

### Setup Instructions

1. Set up AWS Kinesis Data Streams and AWS Firehose for data ingestion.
2. Configure an S3 bucket for raw data storage as files.
3. Set up AWS Glue for data processing, including creating Glue jobs for ETL 
    to trasform data from S3 to Redshift tables after processing cleaning.
4. Configure AWS Redshift for data aggregation and create necessary tables.
5. Set up AWS QuickSight for data visualization and create sample dashboards.


## Demonstrattion of functionality
###Data Ingestion
###Data Storage
###Data Processing
###Data Aggregation
###Data Visualization


##Key features
##Challenges encountered
##Lessons learned




