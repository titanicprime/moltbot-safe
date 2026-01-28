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

def test_audit_log_entry(engine):
    action = {"type": "echo", "target": "", "params": {"message": "logme"}}
    engine.execute(action)
    with open('engine/audit.log') as f:
        logs = f.read()
    assert 'logme' in logs

def test_denied_action_logged(engine):
    action = {"type": "delete", "target": "/etc/passwd", "params": {}}
    engine.execute(action)
    with open('engine/audit.log') as f:
        logs = f.read()
    assert 'delete' in logs and 'denied' in logs
