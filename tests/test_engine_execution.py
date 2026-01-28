import pytest
import os
from engine.engine import AgentEngine
from engine.permissions import Permissions
from engine.action_schema import validate_action
import json

@pytest.fixture
def engine():
    with open('engine/permissions.json') as f:
        perms = Permissions(json.load(f))
    return AgentEngine(perms)

def test_execution_allowed(engine, tmp_path):
    action = {"type": "echo", "target": "", "params": {"message": "hi"}}
    result = engine.execute(action)
    assert result["allowed"]
    assert result["status"] == "success"

def test_execution_denied(engine):
    action = {"type": "delete", "target": "/etc/passwd", "params": {}}
    result = engine.execute(action)
    assert not result["allowed"]
    assert result["status"] == "denied"
