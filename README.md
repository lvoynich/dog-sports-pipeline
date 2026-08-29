# Cloud Data Pipeline: Dog Sports Performance & Budget Tracker

An end-to-end data pipeline that extracts tracking metrics and financial costs from local environments, loads them securely to a Cloud Data Warehouse, and models clean dimensions for analytics.

## 🏗️ Architecture Overview

1. Local Python Script: Decrypts private keys and extracts data.
2. Snowflake Cloud Data Warehouse: Stores raw staging layers securely.
3. dbt Core: Compiles SQL transformations and models data layers.

## 🛠️ Tech Stack & Core Skills
* Language: Python (Pandas, Snowflake Connector, Cryptography)
* Data Warehouse: Snowflake (Virtual Warehouses, Multi-schema separation)
* Transformation: dbt Core (Advanced Snowflake SQL / Star-schema design)
* Quality Testing: Automated schema assertions (Null validation tests)
* Data Security: 2048-bit RSA Key-Pair User Authentication

## 📂 Project Directory Map
* load_to_snowflake.py: Python script streaming local data points to the cloud.
* dog_sports_dbt/: The standard development directory for dbt assets.
* fct_trial_performance.sql: SQL transformation model optimizing metrics.
* schema.yml: Testing schema file ensuring pipeline reliability.

## 🚀 Execution Instructions

### 1. Data Ingestion
Run the script to stream raw data points straight to Snowflake:
python load_to_snowflake.py

### 2. Transformation & Quality Testing
Run these commands to build tables and trigger validation tests:
cd dog_sports_dbt
dbt run
dbt test
