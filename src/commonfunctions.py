import sys,logging
from tests.conftest import  get_kinesis_client
logging.basicConfig(level=logging.INFO, format="%(asctime)s'\n'%(message)s")

def live_stream_is_up_and_running(stream_name):
    kinesis_client_connection= get_kinesis_client()
    get_stream_details = kinesis_client_connection.list_streams()
    stream_names = get_stream_details['StreamNames']
    try:
        assert stream_name in stream_names
        logging.info("{}{}".format (stream_name,' : stream is up and running'))
    except AssertionError:
        sys.exit()

def get_records_from_shard_iterator(get_shard_iterator):
    kinesis_client_connection= get_kinesis_client()
    record_response = kinesis_client_connection.get_records(ShardIterator=get_shard_iterator, Limit=10)
    return record_response

def get_records(stream_name, time_stamp):
    records = []
    kinesis_client_connection= get_kinesis_client()
    get_stream_details = kinesis_client_connection.describe_stream(StreamName=stream_name)
    shards = get_stream_details['StreamDescription']['Shards']
    for shard in shards:
        get_shard_id = shard['ShardId']
        get_shard_iterator = kinesis_client_connection.get_shard_iterator(StreamName=stream_name,ShardId=get_shard_id,ShardIteratorType="AT_TIMESTAMP", Timestamp=time_stamp)
        get_shard_iterator_val = get_shard_iterator['ShardIterator']
        shard_records = get_records_from_shard_iterator (get_shard_iterator_val)
        for record in shard_records['Records']:
            records.append(record['Data'])
    return records


def get_seeds(records):
    seeds = []
    import json
    for record in records:
        stream_data = json.loads ( record )
        seeds.append(stream_data['seed'])
    return seeds