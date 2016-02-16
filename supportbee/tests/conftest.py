import pytest

from supportbee.models import Requester, Ticket
from supportbee.client.meta import SupportbeeClient


@pytest.fixture
def supportbee_client():
    return SupportbeeClient('company', 'token_123', 'resource')


@pytest.fixture
def ticket():
    requester = Requester('John', 'example@example.com')
    return Ticket(1, 'Subject', dict(text='Text content', html='HTML content'), requester)


@pytest.fixture
def company():
   return 'demo'


@pytest.fixture
def api_token():
    # Replace with an actual token to test against SB
    return ''
