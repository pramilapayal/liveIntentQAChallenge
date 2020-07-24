import time,re
from pytest_bdd import (given, when, then, scenarios)
import requests ,logging
from src import commonfunctions
from src.commonfunctions import get_records, get_seeds
scenarios ('../Feature/readLiveStreamData.feature')
logging.basicConfig(level=logging.INFO, format="%(asctime)s'\n'%(message)s")
pattern = re.compile('[A-Za-z][^[-]\d][^\d[.]\d*]')
global time_stamp
time_stamp = time.time()

@given('livestream is up and running')
def check_live_stream_is_running(stream_name):
    commonfunctions.live_stream_is_up_and_running(stream_name)

@when('I send data in route for <seed_value> and validate <expected_results>')
def user_sends_data(get_route_api_url,seed_value,expected_results):
    get_route_api_url = ''.join([get_route_api_url,seed_value])
    response = requests.get(get_route_api_url)
    logging.info(''.join(["User sends the seeed value :",get_route_api_url]))
    logging.info("{}{}".format("Response status code is : ",response.status_code))
    assert str(response.status_code)==str(expected_results) , "Actual and Expected response code mismatch"

@then ('I should get data in <stream_name> depending on the <seed_value>')
def validate_stream_data(stream_name,seed_value,expected_results):
    if expected_results != '200':
        return
    records = get_records(stream_name, int(time_stamp))
    seeds = get_seeds(records)
    logging.info("{}{}".format("Received seed value from stream : ",seeds))
    assert int(seed_value) in seeds , "Actual and Expected seed value mismatch"
