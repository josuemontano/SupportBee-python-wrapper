import pytest

from ..models import Requester, Ticket
from ..supportbee.meta import SupportBeeAPIWrapper


@pytest.fixture
def supportbee_api_wrapper():
    return SupportBeeAPIWrapper('company', 'token_123')


@pytest.fixture
def ticket():
    requester = Requester('John', 'example@example.com')
    return Ticket(1, 'Subject', 'Content', requester)
