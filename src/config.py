from pydantic_settings import BaseSettings, SettingsConfigDict


# Всегда загружаем обычное окружение
# load_dotenv(".env")
#
# # Если тестовый режим включён → перегружаем .test.env
# if os.getenv("TESTING") == "1" and os.path.exists(".test.env"):
#     load_dotenv(".test.env", override=True)


# env_path = Path(".test.env") if os.getenv("TESTING") == "1" else Path(".env")
# load_dotenv(dotenv_path=env_path)


class Settings(BaseSettings):
    MODE: str
    POSTGRES_HOST: str
    POSTGRES_PORT: int

    POSTGRES_DB: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str

    # DB_HOST: str
    # DB_PORT: int
    # DB_USER: str
    # DB_PASS: str
    # DB_NAME: str

    @property
    def DATABASE_URL_asyncpg(self):
        return (
            f"postgresql+asyncpg://{self.POSTGRES_USER}:"
            f"{self.POSTGRES_PASSWORD}@{self.POSTGRES_HOST}:"
            f"{self.POSTGRES_PORT}/{self.POSTGRES_DB}"
        )

    @property
    def DATABASE_URL_psycopg(self):
        # DSN
        # postgresql+psycopg://postgres:postgres@localhost:5432/na
        return (
            f"postgresql+psycopg://{self.POSTGRES_USER}:"
            f"{self.POSTGRES_PASSWORD}@{self.POSTGRES_HOST}:"
            f"{self.POSTGRES_PORT}/{self.POSTGRES_DB}"
        )

    model_config = SettingsConfigDict(env_file=".env")
    # model_config = SettingsConfigDict(env_file=".test.env")
    # class Config:
    #     env_file = ".test.env"
    # model_config = SettingsConfigDict(env_file=str(env_path))


settings = Settings()
