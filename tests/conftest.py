import pytest
import boto3
import configparser

@pytest.fixture()
def getAPIUrl():
    apiHostForRoute = getConfiData().get('apiHost', 'apiHostForRoute')
    url = "http://" + apiHostForRoute + "/route/"
    print(url)
    return url

@pytest.fixture()
def getKinesisUrl():
    kinesisEndPointUrl = getConfiData().get('kinesisHost', 'kinesisEndPoint')
    kinesisEndPointUrl = "http://" + kinesisEndPointUrl
    return kinesisEndPointUrl

def getOddShardIterator():
    return getNextShardIterator('li-stream-odd')

def getEvenShardIterator():
    return getNextShardIterator('li-stream-even')


def getConfiData():
        # This is used to define the config parser
        settings = configparser.RawConfigParser ()
        # this is used to differentiate the config based in sections
        settings._interpolation = configparser.ExtendedInterpolation ()
        # This is used to call the config file
        settings.read("../config/config.ini")
        return settings


def getNextShardIterator(streamName):
    kinesisEndPointUrl = getConfiData ().get ('kinesisHost', 'kinesisEndPoint')
    kinesisEndPointUrl = "http://" + kinesisEndPointUrl
    kinesisClientConnection = boto3.client('kinesis', region_name='us-east-1', aws_access_key_id='liveintent', aws_secret_access_key='liveintent', endpoint_url=kinesisEndPointUrl)
    # Decribe the stream details
    getStreamDetails = kinesisClientConnection.describe_stream(StreamName=streamName)
    # # Get the shard id
    getShardIDOfStream = getStreamDetails['StreamDescription']['Shards'][0]['ShardId']
    # # Get the shard iterator
    getShardIteratorFromShardID = kinesisClientConnection.get_shard_iterator(StreamName=streamName,ShardId=getShardIDOfStream,ShardIteratorType='LATEST')
    # print ("This is getNextShardIterator function value"+str(getShardIteratorFromShardID))
    getShardIterator = getShardIteratorFromShardID['ShardIterator']
    return getShardIterator

