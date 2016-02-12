class TestSupportBeeAPIWrapper(object):
    def test_init(self, supportbee_api_wrapper):
        wrapper = supportbee_api_wrapper

        assert wrapper.base_url == 'https://company.supportbee.com'
        assert wrapper.api_token == 'token_123'

        assert wrapper.resource == None
        assert wrapper.schema == None

    def test_build_get_query(self, supportbee_api_wrapper):
        wrapper = supportbee_api_wrapper
        wrapper.resource = 'resource'

        basic_query = wrapper.build_get_query()
        assert basic_query == 'https://company.supportbee.com/resource?auth_token=token_123'

        options_query = wrapper.build_get_query(attr_a='value', attr_b=True)
        assert options_query == 'https://company.supportbee.com/resource?auth_token=token_123&attr_a=value&attr_b=true'
