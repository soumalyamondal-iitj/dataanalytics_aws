# HR Analytics - Advance Data Engineering Platform in Cloud

## Contributor
- Soumalya Mondal (G23AI1042)

## Table of Contents
- Overview
- Background
- Requirement
- Architecture Overview
- Implementation
- Demonstrattion of functionality
- Key features
- Retention policy and lifecycle management
- Security best practices
- Cost optimization
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





