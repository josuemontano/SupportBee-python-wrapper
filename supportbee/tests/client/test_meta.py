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

        assert wrapper.build_get_query() == 'https://company.supportbee.com/resource?auth_token=token_123'
