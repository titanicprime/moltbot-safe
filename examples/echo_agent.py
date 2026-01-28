from engine.engine import AgentEngine
from engine.permissions import Permissions
import json

def main():
    with open('engine/permissions.json') as f:
        perms = Permissions(json.load(f))
    engine = AgentEngine(perms)
    action = {"type": "echo", "target": "", "params": {"message": "Hello, world!"}}
    result = engine.execute(action)
    print(result)

if __name__ == "__main__":
    main()
