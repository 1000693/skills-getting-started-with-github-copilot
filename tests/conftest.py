import copy

import pytest
from fastapi.testclient import TestClient

from src.app import app, activities as _activities


@pytest.fixture
def client():
    return TestClient(app)


@pytest.fixture(autouse=True)
def reset_activities():
    """Deep-copy and restore the global activities mapping to keep tests isolated."""
    original = copy.deepcopy(_activities)
    try:
        yield
    finally:
        # Restore original contents
        _activities.clear()
        _activities.update(original)
