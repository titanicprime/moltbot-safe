import pytest
import json
from engine.permissions import Permissions

@pytest.fixture
def permissions():
    with open('engine/permissions.json') as f:
        return Permissions(json.load(f))

def test_allowed_action(permissions):
    action = {"type": "echo", "target": "", "params": {}}
    assert permissions.is_allowed(action)

def test_denied_action(permissions):
    action = {"type": "delete", "target": "/etc/passwd", "params": {}}
    assert not permissions.is_allowed(action)
