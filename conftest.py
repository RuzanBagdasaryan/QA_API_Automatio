from utils.api_client import ApiClient
from config.settings import BASE_URL
import pytest

@pytest.fixture
def client():
    """Возвращает экземпляр ApiClient для API тестов"""
    return ApiClient(base_url=BASE_URL)


