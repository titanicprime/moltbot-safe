import os
import json
from .permissions import PermissionSystem
from .action_schema import validate_action
from .audit import AuditLog

class AgentEngine:
    def __init__(self, sandbox_dir, permissions_file, audit_log_file):
        self.sandbox_dir = sandbox_dir
        self.permissions = PermissionSystem(permissions_file)
        self.audit_log = AuditLog(audit_log_file)
        os.makedirs(sandbox_dir, exist_ok=True)

    def execute_action(self, agent_id, action):
        validate_action(action)
        if not self.permissions.is_allowed(agent_id, action['type']):
            self.audit_log.log(agent_id, action, allowed=False)
            raise PermissionError(f"Action {action['type']} not allowed for agent {agent_id}")
        # Minimal stub: just log the action
        self.audit_log.log(agent_id, action, allowed=True)
        return {'status': 'executed', 'action': action['type']}

