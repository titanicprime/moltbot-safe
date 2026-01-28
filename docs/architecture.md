# Architecture

moltbot-safe is a minimal, permissioned, sandboxed execution engine for AI agents.

## Components
- **Engine**: Orchestrates validation, permission checks, sandboxed execution, and audit logging.
- **Permission System**: Loads and enforces least-privilege JSON policy per agent.
- **Action Schema**: Strictly validates agent actions.
- **Audit Log**: Logs every action attempt with timestamp and result.
- **Sandbox**: All agent actions occur in an isolated directory.

## Execution Flow
1. Agent submits an action request.
2. Action is validated against the schema.
3. Permission system checks if the action is allowed.
4. If allowed, the action is executed in the sandbox; otherwise, it is denied.
5. All attempts are logged in the audit log.

## Extensibility
The system is modular and can be extended for new action types, permission models, or sandboxing strategies without compromising safety.
