## Finance Data with AWS Lambda

Purpose of this data is to consume, manipulate, store and dump data to be further used in high level queries. Data goes through the process of a Transformer, Collector and Analyzer. I leveraged AWS Lambda (serverless computing platform) to gather data. The data is feed through a Kinesis stream into S3 buckets where our data is saved. Lastly I utilized Athena Glue and Crawler to create table schema from our data in S3 to be used with ad-hoc interactive queries. 

#### Streaming Yahoo finance data from May 11,2021 intervals of 5 minutes to AWS Kinesis using AWS Lambda for interactive query on AWS Athena

Stocks Involved:
- Facebook (FB)
- Shopify (SHOP)
- Beyond Meat (BYND)
- Netflix (NFLX)
- Pinterest (PINS)
- Square (SQ)
- The Trade Desk (TTD)
- Okta (OKTA)
- Snap (SNAP)
- Datadog (DDOG)

1. Set up AWS Kinesis data stream and data firehose delivery system.
2. Create S3 bucket as the data destination for the firehose delivery stream.
3. Specify buffer conditions on delivery system (5 minutes)
4. Provision AWS Lambda to transform and stream yahoo finance data
5. In AWS Lambda, create lambda layer to use yfinance module and other python dependencies
6. create lambda function (data_transformer.py) to get stock data from yfinance and transform each record to json object, ultimately push data to AWS Kinesis
      json object {
                      "high": 53.5, 
                      "low": 51.61, 
                      "ts": "2020-05-11 09:30:00-04:00", 
                      "name": "SNAP"
                  }
7. Configure AWS Glue and Athena to query directly from S3 bucket using SQL.
