from src.candies.schemas import CandySchema
from src.candies.service import CandiesService
from src.candies.enums import State
import pytest


@pytest.fixture
def candies():
    candies = [
        CandySchema(title="candy1", owner="Dan"),
        CandySchema(title="candy2", state=State.eaten),
        CandySchema(title="candy3", state=State.bitten),
    ]
    return candies


@pytest.fixture
def empty_candies():
    CandiesService.delete_all()
