from supportbee.models import Ticket
from supportbee.schema import TicketSchema
from supportbee.client.tickets import TicketsClient


class TestTicketsClient(object):
    def test_init(self, company, api_token):
        client = TicketsClient(company, api_token)

        assert client.resource == 'tickets'

    def test_get_collection(self, company, api_token):
        client = TicketsClient(company, api_token)
        tickets = client.get_collection()

        assert isinstance(tickets, list)

    def test_create(self, company, api_token, ticket):
        client = TicketsClient(company, api_token)
        created = client.create(ticket)

        assert isinstance(created, Ticket)
        assert created in client.get_collection()
