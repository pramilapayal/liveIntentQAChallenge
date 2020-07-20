from pytest_bdd import (given, when, then, scenarios)
import requests ,sys
from tests.conftest import getEvenShardIterator, getOddShardIterator
from src import commonfunctions
from src.commonfunctions import livestreamisupandrunning
scenarios ('../Feature/readLiveStreamData.feature')
global evenShardIterator, oddShardIterator
oddShardIterator = getOddShardIterator()
evenShardIterator = getEvenShardIterator()
import re
pattern = re.compile ( "[A-Za-z]+" )


def getDataForShardIterator(seedvalue):
    if len(seedvalue)==0 or pattern.fullmatch(seedvalue):
        seedvalue = seedvalue
        return
    elif int(seedvalue) % 2 == 0:
        return evenShardIterator
    else:
        return oddShardIterator


@given('livestream is up and running')
def checkLiveStreamIsUpAndRunning(getKinesisUrl):
    livestreamisupandrunning (getKinesisUrl)

@when('I send data in route for <seedvalue> and validate <expectedResults>')
def userSendSeedValue(getAPIUrl, seedvalue,expectedResults):
    response = requests.get (getAPIUrl + seedvalue)
    print("------------------------------------------------------------")
    print("User sends seed value :" +str(getAPIUrl + seedvalue))
    print("------------------------------------------------------------")
    assert str(response.status_code)== str(expectedResults) , "Actual and Expected results mismatch"


@then ('I should get data in li-stream-even stream when even number is passed as seedvalue and li-stream-odd stream when odd number is passed as <seedvalue>')
def dataValidation(getKinesisUrl, seedvalue):
    if len(seedvalue)==0 or pattern.fullmatch(seedvalue):
        seedvalue = seedvalue
        return
    shardIteratorValue = getDataForShardIterator (seedvalue)
    data = commonfunctions.getRecordsfromStream (getKinesisUrl, shardIteratorValue)
    print("------------------------------------------------------------")
    print("Data Received from the data stream" )
    print("------------------------------------------------------------")
    print(data)
    print("------------------------------------------------------------")
    getRecordData = getRecordData = data['Records'][0]['Data']
    import json
    dataInStream = json.loads (getRecordData)
    dataInStream = dataInStream['seed']
    assert str(dataInStream) == str(seedvalue)
    print("------------------------------------------------------------")
    print("User has sent the seed value : " +str(seedvalue))
    print("------------------------------------------------------------")
    print("Data stored in the stream : " +str(dataInStream))
    print("------------------------------------------------------------")
