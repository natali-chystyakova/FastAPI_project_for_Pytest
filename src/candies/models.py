from src.database import Base
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Enum
from src.candies.enums import State


class Candies(Base):
    __tablename__ = "candies"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str | None] = mapped_column(String(200), nullable=True)
    # state: Mapped[str] = mapped_column(String(20), nullable=False, server_default="full")
    owner: Mapped[str] = mapped_column(String(100), nullable=False, server_default="teacher")
    state: Mapped[State] = mapped_column(Enum(State), nullable=False, server_default="full")
