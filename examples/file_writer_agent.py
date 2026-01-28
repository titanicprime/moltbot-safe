from engine.engine import AgentEngine
from engine.permissions import Permissions
import json

def main():
    with open('engine/permissions.json') as f:
        perms = Permissions(json.load(f))
    engine = AgentEngine(perms)
    action = {"type": "write", "target": "sandbox/hello.txt", "params": {"content": "sandboxed!"}}
    result = engine.execute(action)
    print(result)

if __name__ == "__main__":
    main()
