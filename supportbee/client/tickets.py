from .meta import SupportbeeClient
from ..schema import TicketSchema


class TicketsClient(SupportbeeClient):
    def __init__(self, company, api_token):
        super(TicketsClient, self).__init__(company, api_token, 'tickets')

    def get_collection(self, **kwargs):
        """ Returns a list of tickets
        """
        url = self.build_get_url(**kwargs)
        return self.get(url, TicketSchema(many=True))

    def create(self, ticket):
        """ Posts data to /tickets
        """
        url = '{0}/{1}'.format(self.base_url, self.resource)
        return self.post(url, ticket, TicketSchema())
