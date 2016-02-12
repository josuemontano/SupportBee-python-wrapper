class SupportBeeAPIWrapper(object):
    """ Initialize the API client
    """
    root = 'https://{0}.supportbee.com'

    def __init__(self, company, api_token):
        if api_token is None:
            raise Error('You must provide an API token')

        self.base_url = self.root.format(company)
        self.api_token = api_token

    def build_get_query(self, resource):
        return '{0}/{1}?auth_token={2}'.format(self.base_url, resource, self.api_token)
