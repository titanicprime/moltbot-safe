import json

class PermissionSystem:
    def __init__(self, permissions_file):
        self.permissions_file = permissions_file
        self._load()

    def _load(self):
        try:
            with open(self.permissions_file, 'r') as f:
                self.permissions = json.load(f)
        except FileNotFoundError:
            self.permissions = {}

    def is_allowed(self, agent_id, action_type):
        allowed = self.permissions.get(agent_id, [])
        return action_type in allowed

