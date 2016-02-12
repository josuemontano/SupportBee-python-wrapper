import pytest

from ..models import Requester, Ticket


class TestRequester:
    def test_init(self):
        requester = Requester("John", "Smith")
        assert requester.name == "John"
        assert requester.email == "Smith"


class TestTicket:
    def test_init(self):
        requester = Requester("John", "Smith")
        ticket = Ticket(1, "Subject", "Content", requester)
        assert ticket.id == 1
        assert ticket.subject == "Subject"
        assert ticket.content == "Content"
        assert ticket.requester == requester
        assert ticket.starred == False
        assert ticket.spam == False

    def test_eq(self):
        ticket_a = Ticket(1, None, None, None)
        ticket_b = Ticket(1, None, None, None)

        assert ticket_a == ticket_b

    def test_not_eq(self):
        ticket_a = Ticket(1, None, None, None)
        ticket_b = Ticket(2, None, None, None)

        assert ticket_a != ticket_b
