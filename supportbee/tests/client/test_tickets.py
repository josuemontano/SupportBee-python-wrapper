from supportbee.schema import TicketSchema
from supportbee.client.tickets import TicketsClient


class TestTicketsClient(object):
    def test_init(self, company, api_token):
        client = TicketsClient(company, api_token)

        assert client.resource == 'tickets'
        assert isinstance(client.schema, TicketSchema)

    def test_get_collection(self, company, api_token):
        client = TicketsClient(company, api_token)
        tickets = client.get_collection()

        assert isinstance(tickets, list)
