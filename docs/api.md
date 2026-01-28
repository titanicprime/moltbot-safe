# API Reference

## AgentEngine

### Initialization
```
from engine.engine import AgentEngine
from engine.permissions import Permissions
import json

with open('engine/permissions.json') as f:
    perms = Permissions(json.load(f))
engine = AgentEngine(perms)
```

### Methods

#### execute(action: dict) -> dict
- Validates the action schema
- Checks permissions
- Executes the action in the sandbox if allowed
- Logs the attempt and result
- Returns a dict with status, allowed, and result/error

#### Permissions
- `Permissions.is_allowed(action: dict) -> bool`: Returns True if the action is permitted by the current policy.
- Loads from a JSON policy file.

#### Action Validation
- `validate_action(action: dict) -> bool`: Raises ValueError if the action is malformed or ambiguous.

#### Audit Logging
- All actions (allowed or denied) are logged to `engine/audit.log` with timestamp, action, result, and metadata.

## Safety Model
- No method bypasses validation, permission checks, or sandboxing.
- All interfaces are minimal, explicit, and auditable.
