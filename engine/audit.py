import json
import time

class AuditLog:
    def __init__(self, log_file):
        self.log_file = log_file

    def log(self, agent_id, action, allowed):
        entry = {
            'timestamp': time.time(),
            'agent_id': agent_id,
            'action': action,
            'allowed': allowed
        }
        with open(self.log_file, 'a') as f:
            f.write(json.dumps(entry) + '\n')

