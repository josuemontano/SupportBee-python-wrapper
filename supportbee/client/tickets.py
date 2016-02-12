from .meta import SupportBeeAPIWrapper
from ..schema import TicketSchema


class TicketsClient(SupportBeeAPIWrapper):
    resource = 'tickets'
    schema = TicketSchema(many=True)

    def get_collection(self):
        """ Returns a list of tickets
        """
        query = self.build_get_query()
        return self.get(query)
