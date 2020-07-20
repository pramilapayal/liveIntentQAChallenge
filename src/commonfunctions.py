import boto3
import sys

def getRecordsfromStream(kinesisEndPointUrl,getShardIterator):
    kinesisClientConnection = boto3.client('kinesis', region_name='us-east-1', aws_access_key_id='liveintent', aws_secret_access_key='liveintent', endpoint_url=kinesisEndPointUrl)
    record_response = kinesisClientConnection.get_records(ShardIterator=getShardIterator)
    return record_response

def livestreamisupandrunning(kinesisEndPointUrl):
    kinesisClientConnection = boto3.client ('kinesis', region_name='us-east-1', aws_access_key_id='liveintent', aws_secret_access_key='liveintent', endpoint_url=kinesisEndPointUrl)
    getStreamDetails = kinesisClientConnection.list_streams()
    streamNames = getStreamDetails['StreamNames']
    try:
        assert streamNames == ['li-stream-even', 'li-stream-odd']
        print("------------------------------")
        print("Live Stream is up and running")
        print("------------------------------")
    except AssertionError:
        sys.exit()
