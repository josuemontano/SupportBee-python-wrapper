from .meta import SupportbeeClient
from ..schema import TicketSchema


class TicketsClient(SupportbeeClient):
    resource = 'tickets'
    schema = TicketSchema(many=True)

    def get_collection(self, **kwargs):
        """ Returns a list of tickets
        """
        query = self.build_get_url(**kwargs)
        return self.get(query)
