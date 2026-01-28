from engine.engine import AgentEngine
from engine.permissions import Permissions
import json

def main():
    with open('engine/permissions.json') as f:
        perms = Permissions(json.load(f))
    engine = AgentEngine(perms)
    action = {"type": "delete", "target": "/etc/passwd", "params": {}}
    result = engine.execute(action)
    print(result)
    print("Check engine/audit.log for denied entry.")

if __name__ == "__main__":
    main()
