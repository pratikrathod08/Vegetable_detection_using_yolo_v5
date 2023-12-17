# End-to_End-Vegetable-Object-Detection-Using-Yolo-v5 

## Workflows

1. constants
2. entity
3. components
4. pipelines
5. app.py

## Data Ingestion process 

1. logging
- create logging file for log purpose .
2. exception
- reate exception file for except errors during trainin and overall project.
3. constant/training_pipeline/init
- Give dir names and download url.
4. entity/config_entity
- config for data ingestion 
5. entity/artifacts_entity
- Make data ingestion artifacts class.
6. components
- create data ingestion class.
- make method for download data give zip file path.
- create method for extract zip file return feature store path where we store all extracted files from zip.
- make method for data ingestion process return data ingstion artifacts
7. pipeline/training_pipeline
- create method start data ingestion make object of data ingestion class which do overall process and return data ingestion artifacts.  
- make run method to run training pipelines start data ingestion method.

## Data Validation workflow

1. content/training_pipeline/init
- give dir name and required all files.
2. entity/config_entity 
- add data validation config
3. entity/artifacts_entity
- add data validation artifact class.
4. components/data_validation
- methods for data validation 
5. pipeline/training_pipeline
- add start data validation method
- add method to run pipeline.

