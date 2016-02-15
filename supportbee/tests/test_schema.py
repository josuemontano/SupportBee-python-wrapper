from supportbee.models import Requester, Ticket
from supportbee.schema import RequesterSchema, TicketSchema


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
                                'summary': '',
                                'spam': False,
                                'starred': False,
                                'unanswered': True,
                                'archived': False,
                                'requester_email': ticket.requester.email,
                                'requester_name': ticket.requester.name,
                                'comments_count': 0,
                                'replies_count': 0 }

    def test_load(self):
        schema = TicketSchema()
        payload = { 'id': 10,
                    'subject': 'Subject',
                    'content': dict(html='HTML<br>', text='Text\n'),
                    'summary': 'Summary content',
                    'spam': True,
                    'starred': True,
                    'unanswered': False,
                    'archived': True,
                    'requester': { 'name': 'Example', 'email': 'example@example.com' },
                    'comments_count': 0,
                    'replies_count': 0 }

        result = schema.load(payload)
        deserialized = result.data

        assert isinstance(deserialized, Ticket)
        assert deserialized.id == 10
        assert deserialized.subject == 'Subject'
        assert deserialized.content == {'html': 'HTML<br>', 'text': 'Text\n'}
        assert deserialized.summary == 'Summary content'

        assert isinstance(deserialized.requester, Requester)
        assert deserialized.requester.name == 'Example'
        assert deserialized.requester.email == 'example@example.com'

        assert deserialized.spam == True
        assert deserialized.starred == True
        assert deserialized.unanswered == False
        assert deserialized.archived == True

        assert deserialized.comments_count == 0
        assert deserialized.replies_count == 0
