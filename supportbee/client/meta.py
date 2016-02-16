import requests
import json
from urllib.parse import urlencode

TIMEOUT = 15


class SupportbeeClient(object):
    """ Base SupportBee API client
    """
    schema = None
    root = 'https://{0}.supportbee.com'

    def __init__(self, company, api_token, resource):
        if api_token is None:
            raise Error('You must provide an API token')

        self.base_url = self.root.format(company)
        self.api_token = api_token
        self.resource = resource

    def build_get_url(self, **kwargs):
        """ Add GET params to base URL

        :param kwargs: Dictionary containing requested params to be added
        :return: string with updated URL
        """
        params = dict(map(bool_to_string, kwargs.items()))
        params['auth_token'] = self.api_token

        query = '{0}/{1}?'.format(self.base_url, self.resource)
        query += urlencode(params)
        return query

    def get(self, url):
        """ Makes a GET request and returns the deserialized response.
        """
        try:
            ans = requests.get(url, timeout=TIMEOUT)
        except (ConnectionError, TimeoutError) as e:
            raise e
        else:
            payload = json.loads(ans.text).get(self.resource)
            return self.schema.load(payload).data


def bool_to_string(item):
    """
    Returns a tuple identical to the given one, unless its second term
    is a boolean. In that case this is turned to a lowercase string.
    """
    key, value = item
    return (key, str(value).lower() if isinstance(value, bool) else value)
