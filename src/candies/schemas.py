from pydantic import ConfigDict

from pydantic import BaseModel, Field
from src.candies.enums import State


class CandySchema(BaseModel):
    id: int | None = Field(default=1)
    title: str = Field(default="Конфета")
    # state: str = Field(default="full")
    owner: str = Field(default="teacher")
    state: State = Field(default=State.full)

    model_config = ConfigDict(from_attributes=True)

    def __eq__(self, other):
        if not isinstance(other, type(self)):
            return False
        for attr in ["title", "state", "owner"]:
            if getattr(self, attr) != getattr(other, attr):
                return False
        return True

    def to_dict_wo_id(self) -> dict:
        return self.model_dump(exclude={"id"})
