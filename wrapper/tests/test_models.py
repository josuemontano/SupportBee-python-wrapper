import pytest

from ..models import Requester


class TestRequester:
    def test_init(self):
        requester = Requester("John", "Smith")
        assert requester.name == "John"
        assert requester.email == "Smith"
