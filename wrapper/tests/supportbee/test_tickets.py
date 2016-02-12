from wrapper.schema import TicketSchema
from wrapper.supportbee.tickets import TicketsClient


class TestTicketsClient(object):
    def test_init(self, company, api_token):
        client = TicketsClient(company, api_token)

        assert client.resource == 'tickets'
        assert isinstance(client.schema, TicketSchema)

    def test_get(self, company, api_token):
        client = TicketsClient(company, api_token)
        tickets = client.get()

        assert isinstance(tickets, list)
