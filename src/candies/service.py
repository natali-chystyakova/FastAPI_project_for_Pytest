from pydantic import TypeAdapter
import sqlalchemy.exc
from src.candies.repository import CandiesRepository
from src.candies.schemas import CandySchema


class CandiesService:
    @classmethod
    def add(cls, candy: CandySchema):
        candy_dict = candy.to_dict_wo_id()
        new_candy = CandiesRepository.add(candy_dict)
        return TypeAdapter(CandySchema).dump_python(new_candy)

    @classmethod
    def get(cls, candy_id: int):
        try:
            candy = CandiesRepository.get(candy_id)
            return TypeAdapter(CandySchema).dump_python(candy)
        except sqlalchemy.exc.NoResultFound:
            return None

    @classmethod
    def list(
        cls,
        title: str | None = None,
        state: str | None = None,
        owner: str | None = None,
    ):
        filter_by = {k: v for k, v in {"title": title, "state": state, "owner": owner}.items() if v}
        candies = CandiesRepository.list(filter_by)
        return TypeAdapter(list[CandySchema]).dump_python(candies)

    @classmethod
    def count(cls) -> int:
        count = CandiesRepository.count()
        return count

    @classmethod
    def update(cls, candy_id: int, candy: CandySchema):
        candy_dict = candy.to_dict_wo_id()
        CandiesRepository.update(candy_id, candy_dict)

    @classmethod
    def finish(cls, candy_id: int):
        finish_dict = {"state": "eaten"}
        CandiesRepository.finish(candy_id, finish_dict)

    @classmethod
    def delete(cls, candy_id: int):
        CandiesRepository.delete(candy_id)

    @classmethod
    def delete_all(cls):
        CandiesRepository.delete_all()
