from engine.engine import AgentEngine
from engine.permissions import Permissions
import json

def main():
    with open('engine/permissions.json') as f:
        perms = Permissions(json.load(f))
    engine = AgentEngine(perms)
    allowed_action = {"type": "echo", "target": "", "params": {}}
    denied_action = {"type": "delete", "target": "/etc/passwd", "params": {}}
    print("Allowed:", engine.execute(allowed_action))
    print("Denied:", engine.execute(denied_action))

if __name__ == "__main__":
    main()
