import json
import datetime
import yfinance as yf
import time
import boto3
import pandas as pd



def lambda_handler(event, context):
    
    # TODO implement
    kinesis = boto3.client('kinesis','us-east-1')
    
    df = pd.DataFrame()
    listx=['FB','SHOP','BYND','NFLX','PINS','SQ','TTD','OKTA','SNAP','DD']
    for i in listx:
        data = yf.download(tickers = i, start='2021-05-11', end='2021-05-12',interval='5m',prepost=False)
        data['ts'] = data.index.astype(str)
        data['name'] = i
        df2 = data[['High','Low','ts','name']]
        df2.reset_index(drop=True, inplace=True)
        df = df.append(df2)
    
    
    x = df.to_dict(orient='records')
    
    data = json.dumps(x)
    kinesis.put_record(StreamName='STA97602021_stream1',Data=data,PartitionKey='partitionkey')

    return {
         'statusCode': 200,
         'body': data
    }
