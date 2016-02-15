from supportbee.models import Requester, Ticket


class TestRequester(object):
    def test_init(self):
        requester = Requester('John', 'example@example.com')
        assert requester.name == 'John'
        assert requester.email == 'example@example.com'


class TestTicket(object):
    def test_init(self, ticket):
        # Test initial values
        assert ticket.id == 1
        assert ticket.subject == 'Subject'
        assert ticket.content == {'html': 'HTML content', 'text': 'Text content'}
        assert ticket.summary == ''

        assert ticket.starred == False
        assert ticket.spam == False
        assert ticket.unanswered == True
        assert ticket.archived == False

        assert ticket.replies_count == 0
        assert ticket.comments_count == 0

        assert isinstance(ticket.requester, Requester)
        assert ticket.requester.name == 'John'
        assert ticket.requester.email == 'example@example.com'

    def test_eq(self):
        ticket_a = Ticket(1, None, None, {})
        ticket_b = Ticket(1, None, None, {})

        assert ticket_a == ticket_b

    def test_not_eq(self):
        ticket_a = Ticket(1, None, None, {})
        ticket_b = Ticket(2, None, None, {})

        assert ticket_a != ticket_b
