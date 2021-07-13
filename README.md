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
