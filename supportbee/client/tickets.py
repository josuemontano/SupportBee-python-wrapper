from .meta import SupportBeeAPIWrapper
from ..schema import TicketSchema


class TicketsClient(SupportBeeAPIWrapper):
    resource = 'tickets'
    schema = TicketSchema(many=True)

    def get_collection(self, **kwargs):
        """ Returns a list of tickets
        """
        query = self.build_get_query(**kwargs)
        return self.get(query)
