import pytest
from engine.action_schema import validate_action

def test_valid_action():
    action = {"type": "echo", "target": "", "params": {}}
    assert validate_action(action)

def test_missing_type():
    action = {"target": "", "params": {}}
    with pytest.raises(ValueError):
        validate_action(action)

def test_ambiguous_action():
    action = {"type": "echo", "target": "", "params": {}, "extra": 123}
    with pytest.raises(ValueError):
        validate_action(action)
