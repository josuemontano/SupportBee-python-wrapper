import requests
import json

from .meta import SupportBeeAPIWrapper
from ..schema import TicketSchema


TIMEOUT = 10

class TicketsClient(SupportBeeAPIWrapper):
    resource = 'tickets'
    schema = TicketSchema(many=True)

    def get(self):
        """ Returns a list of tickets
        """
        try:
            ans = requests.get(self.build_get_query(self.resource), timeout=TIMEOUT)
        except (ConnectionError, TimeoutError) as e:
            raise e
        else:
            payload = json.loads(ans.text).get('tickets')
            return self.schema.load(payload).data
