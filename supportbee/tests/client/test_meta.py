class TestSupportbeeClient(object):
    def test_init(self, supportbee_client):
        wrapper = supportbee_client

        assert wrapper.base_url == 'https://company.supportbee.com'
        assert wrapper.api_token == 'token_123'

        assert wrapper.resource == None
        assert wrapper.schema == None

    def test_build_get_url(self, supportbee_client):
        wrapper = supportbee_client
        wrapper.resource = 'resource'

        basic_query = wrapper.build_get_url()
        assert basic_query == 'https://company.supportbee.com/resource?auth_token=token_123'

        options_query = wrapper.build_get_url(attr_a='value a', attr_b=True)
        assert options_query == 'https://company.supportbee.com/resource?attr_a=value+a&attr_b=true&auth_token=token_123'
