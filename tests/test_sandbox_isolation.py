import pytest
import os
from engine.engine import AgentEngine
from engine.permissions import Permissions
import json

@pytest.fixture
def engine():
    with open('engine/permissions.json') as f:
        perms = Permissions(json.load(f))
    return AgentEngine(perms)

def test_file_write_in_sandbox(engine, tmp_path):
    action = {"type": "write", "target": "sandbox/test.txt", "params": {"content": "safe"}}
    result = engine.execute(action)
    assert result["allowed"]
    assert os.path.exists("sandbox/test.txt")


def test_file_write_outside_sandbox_denied(engine):
    action = {"type": "write", "target": "/tmp/evil.txt", "params": {"content": "bad"}}
    result = engine.execute(action)
    assert not result["allowed"]
    assert not os.path.exists("/tmp/evil.txt")
