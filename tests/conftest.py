import time

import pytest
from src.database import Base

from src.config import Settings
from sqlalchemy import create_engine

import psycopg


@pytest.fixture(scope="session", autouse=True)  # скоуп session -один раз, на початку, autouse -запустити
def setup_db():
    settings = Settings(_env_file=".test.env")  # якщо в pytest.ini стоiть .env
    # подключаемся к postgres без имени базы
    conn = psycopg.connect(
        dbname="postgres",
        user=settings.POSTGRES_USER,
        password=settings.POSTGRES_PASSWORD,
        host=settings.POSTGRES_HOST,
        port=settings.POSTGRES_PORT,
        autocommit=True,
    )
    conn.autocommit = True
    cur = conn.cursor()

    # создаём базу, если её ещё нет
    cur.execute(f"SELECT 1 FROM pg_database WHERE datname='{settings.POSTGRES_DB}'")
    exists = cur.fetchone()
    if not exists:
        cur.execute(f'CREATE DATABASE "{settings.POSTGRES_DB}"')
        print(f"Создал тестовую БД: {settings.POSTGRES_DB}")

    cur.close()
    conn.close()
    test_engine = create_engine(settings.DATABASE_URL_psycopg, echo=True)
    print(f"Працюэбаза даних: {settings.POSTGRES_DB=}")
    # assert settings.MODE=="TEST"  #якщо нi то впаде фiкстура
    print("перед створенням бд")
    Base.metadata.drop_all(test_engine)  # видалити все
    Base.metadata.create_all(test_engine)  # зробити все знову
    yield  # вiддати керування пайтесту
    Base.metadata.drop_all(test_engine)  # видалити все
    print("пiсля створення бд")


def pytest_addoption(parser):
    # для вибору браузера
    parser.addoption("--browser", default="chrome", choices=("chrome", "firefox"))
    # для вибору запуску повiльних тестiв
    parser.addoption("--run-slow", default="true", choices=("true", "false"))


@pytest.fixture
def browser(request):
    return request.config.getoption("--browser")


def test_1(browser):
    print(f"Працюэ браузер {browser}")


# pytest tests/conftest.py -s --browser=chrome


@pytest.mark.skip(reason="Повiльний тест")  # пропускаем тест
def test_slow():
    time.sleep(3)


@pytest.mark.skipif('config.getoption("--run-slow")=="false"')  # якщо --run-slow")=="false", то пропустити
def test_slow1():
    time.sleep(3)


def test_fast():
    pass


def test_slow2():
    time.sleep(3)


def test_slow3():
    time.sleep(3)
