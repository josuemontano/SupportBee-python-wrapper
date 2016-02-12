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
        deserialized = result.data

        assert isinstance(deserialized, Requester)
        assert deserialized.name == 'John'
        assert deserialized.email == 'example@example.com'


class TestTicketSchema(object):
    def test_dump(self, ticket):
        schema = TicketSchema()
        result = schema.dump(ticket)

        assert result.data == { 'id': ticket.id,
                                'subject':ticket.subject,
                                'content': ticket.content,
                                'spam': False,
                                'starred': False,
                                'requester_email': ticket.requester.email,
                                'requester_name': ticket.requester.name }

    def test_load(self, ticket):
        schema = TicketSchema()
        payload = { 'id': ticket.id,
                    'subject':ticket.subject,
                    'content': ticket.content,
                    'spam': False,
                    'starred': False,
                    'requester': { 'name': ticket.requester.name, 'email': ticket.requester.email } }

        result = schema.load(payload)
        deserialized = result.data

        assert isinstance(deserialized, Ticket)
        assert deserialized.id == ticket.id
        assert deserialized.subject == ticket.subject
        assert deserialized.content == ticket.content
