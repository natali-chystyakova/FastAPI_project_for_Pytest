from src.candies.schemas import CandySchema
from src.candies.service import CandiesService

import pytest


@pytest.mark.usefixtures("empty_candies")
class TestCandies:
    def test_count_candies(self, candies):
        CandiesService.delete_all()

        for candy in candies:
            CandiesService.add(candy)
        assert CandiesService.count() == 3

    def test_list_candies(self, candies):

        for candy in candies:
            CandiesService.add(candy)
        # all_candies = CandiesService.list()
        # for added_candy in all_candies:
        #     assert added_candy in candies
        for added_candy in CandiesService.list():
            schema_candy = CandySchema(**added_candy)
            assert schema_candy in candies
