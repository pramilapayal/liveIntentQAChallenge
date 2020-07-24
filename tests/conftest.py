import pytest ,boto3,configparser,logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s'\n'%(message)s")

@pytest.fixture()
def get_route_api_url():
    api_host_for_route = get_config_data().get('route', 'api_host_for_route')
    url = ''.join(["http://",api_host_for_route,"/route/"])
    return url

def get_kinesis_client():
    kineses_endpoint_url = get_config_data().get('kinesis', 'kinesis_end_point')
    aws_access_key_id = get_config_data().get('kinesis', 'aws_access_key_id')
    aws_secret_key = get_config_data().get('kinesis', 'aws_secret_key_id')
    kineses_endpoint_url = ''.join("http://" + kineses_endpoint_url)
    kinesis_client_connection = boto3.client('kinesis', region_name='us-east-1', aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_key, endpoint_url=kineses_endpoint_url)
    return kinesis_client_connection

def get_config_data():
    settings = configparser.RawConfigParser()
    settings._interpolation = configparser.ExtendedInterpolation()
    settings.read("config/config.ini")
    return settings
