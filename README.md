# Data Engineering Project 3: Marvan Think Tank Covid-19 Multinational Data Catalog

This project was completed as part of a group assignment for the NSS Data Engineering Bootcamp.

### Team:

- [Michael Galo](https://github.com/MichaelGalo)
- [Alex Berka](https://github.com/alexberka)

### Additional Repositories that Work in Tandem with This Project
[Exploratory Data Analysis](https://github.com/siwa-p/marvan_project_eda)

[API for User Access](https://github.com/siwa-p/marvan_research_covid_api)

### Introduction

This project provides a unified catalog of national-level open datasets related to the Covid-19 pandemic for the United States, United Kingdom, and Canada. The catalog is designed to help researchers and analysts efficiently discover, filter, and access authoritative data sources containing keywords such as `Covid-19`, `SARS-CoV-2`, or `Coronavirus`. All datasets are sourced directly from federal or national repositories to ensure reliability and consistency.

## Technical Overview

### Architecture

- **Cloud Object Storage:** Raw datasets are ingested and stored in MinIO (S3-compatible) for scalable, secure access.
- **Data Warehouse:** Snowflake is used for centralized storage, with schemas for raw, staged, and cleaned data.
- **Orchestration:** Apache Airflow automates the ELT workflow, scheduling extraction, loading, and transformation tasks.
- **Transformation:** dbt (Data Build Tool) manages SQL-based data modeling and transformation, ensuring reproducibility and modularity.
- **API Layer:** A Python-based API enables programmatic access to curated datasets for downstream analytics and research.
- **Testing & Quality:** Unit tests and static analysis are integrated for code reliability and maintainability.
- **Containerization:** Docker and VS Code Dev Containers provide reproducible development environments.

### Workflow

1. **Data Acquisition:** Datasets are sourced from official government portals via API or direct download.
2. **Raw Storage:** Files are uploaded to MinIO and cataloged for pipeline processing.
3. **ELT Pipeline:** Airflow DAGs orchestrate extraction from MinIO, loading into Snowflake (RAW schema), and transformation via dbt.
4. **Data Modeling:** dbt SQL models standardize and enrich data, moving it through STAGED and CLEANED schemas.
5. **API Access:** Researchers query curated datasets using the Python API.
6. **Continuous Integration:** Automated tests and linting ensure code correctness and data quality.

### Key Technologies

- **Python**: Data extraction, API development, and pipeline scripting
- **MinIO**: Cloud object storage for raw data
- **Snowflake**: Scalable data warehouse
- **Airflow**: Workflow orchestration
- **dbt**: SQL-based data transformation and modeling
- **Docker**: Containerized development and deployment

### Extensibility

The modular design supports easy integration of new data sources, countries, or analytical workflows. All components are cloud-ready and can be scaled or adapted for additional domains.
