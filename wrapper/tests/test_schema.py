from ..models import Requester, Ticket
from ..schema import RequesterSchema, TicketSchema


class TestRequestSchema(object):
    def test_dump(self):
        schema = RequesterSchema()
        requester = Requester('John', 'example@example.com')

        result = schema.dump(requester)
        assert result.data == { 'name': 'John', 'email': 'example@example.com' }

    def test_load(self):
        schema = RequesterSchema()
        payload = { 'name': 'John', 'email': 'example@example.com' }

        result = schema.load(payload)
        assert isinstance(result.data, Requester)


class TestTicketSchema(object):
    def test_dump(self, ticket):
        schema = TicketSchema()
        result = schema.dump(ticket)

        assert result.data == { 'id': ticket.id,
            'subject':ticket.subject,
            'content': ticket.content,
            'requester_email': ticket.requester.email,
            'requester_name': ticket.requester.name }

    def test_load(self, ticket):
        schema = TicketSchema()
        payload = { 'id': ticket.id,
            'subject':ticket.subject,
            'content': ticket.content,
            'requester_email': ticket.requester.email,
            'requester_name': ticket.requester.name }

        result = schema.load(payload)
        assert isinstance(result.data, Ticket)
