import pytest

from ..supportbee.meta import SupportBeeAPIWrapper


@pytest.fixture
def supportbee_api_wrapper():
    return SupportBeeAPIWrapper('company', 'token_123')
