import requests
import json

TIMEOUT = 15


class SupportBeeAPIWrapper(object):
    """ Initialize the API client
    """
    resource = None
    schema = None

    root = 'https://{0}.supportbee.com'

    def __init__(self, company, api_token):
        if api_token is None:
            raise Error('You must provide an API token')

        self.base_url = self.root.format(company)
        self.api_token = api_token

    def build_get_query(self, **kwargs):
        """ Appends to root the resource and auth token
        """
        # TODO: Use a library and escape kwargs
        query = '{0}/{1}?auth_token={2}'.format(self.base_url, self.resource, self.api_token)
        for name, value in kwargs.items():
            query += '&{0}={1}'.format(str(name).lower(), str(value).lower())

        return query

    def get(self, query):
        """ Makes a GET request and returns the deserialized response
        """
        try:
            ans = requests.get(query, timeout=TIMEOUT)
        except (ConnectionError, TimeoutError) as e:
            raise e
        else:
            payload = json.loads(ans.text).get(self.resource)
            return self.schema.load(payload).data
