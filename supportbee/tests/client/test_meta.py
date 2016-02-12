class TestSupportbeeClient(object):
    def test_init(self, supportbee_client):
        client = supportbee_client

        assert client.base_url == 'https://company.supportbee.com'
        assert client.api_token == 'token_123'
        assert client.resource == 'resource'
        assert client.schema == None

    def test_build_get_url(self, supportbee_client):
        client = supportbee_client

        basic_query = client.build_get_url()
        assert basic_query == 'https://company.supportbee.com/resource?auth_token=token_123'

        options_query = client.build_get_url(attr_a='value a', attr_b=True)
        assert options_query == 'https://company.supportbee.com/resource?attr_a=value+a&attr_b=true&auth_token=token_123'
