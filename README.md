## Finance Data with AWS Lambda

Purpose of this data is to consume, manipulate, store and dump data to be further used in high level queries. Data goes through the process of a Transformer, Collector and Analyzer. I leveraged AWS Lambda (serverless computing platform) to gather data. The data is feed through a Kinesis stream into S3 buckets where our data is saved. Lastly I utilized Athena Glue and Crawler to create table schema from our data in S3 to be used with ad-hoc interactive queries. 

This project touched my soul because I learned the full ETL data processing on the worlds most powerful cloud computing service AWS.
