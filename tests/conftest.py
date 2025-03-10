import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.database.connection import get_db, Base
from src.api.main import app
from src.repositories.user_repository import UserRepository
from src.services.user_service import UserService


TEST_DATABASE_URL = "sqlite:///test_api.db"
engine = create_engine(TEST_DATABASE_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

@pytest.fixture(scope="module", autouse=True)
def setup_database():
    Base.metadata.create_all(bind=engine)
    yield
    Base.metadata.drop_all(bind=engine)

def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db

client = TestClient(app)


@pytest.fixture()
def db_session():
    session = TestingSessionLocal()
    yield session
    session.close()

@pytest.fixture()
def user_service(db_session):
    repo = UserRepository(db_session)
    return UserService(repo)
