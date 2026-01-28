# moltbot-safe

A minimal, permissioned, sandboxed execution engine for AI agents.

## Purpose
moltbot-safe is a minimal, auditable, safety-first execution substrate for agentic systems. It enforces explicit permissions, isolates execution inside a sandbox, validates all actions, and logs every attempt. The system is minimal, predictable, and secure—no autonomous behavior, no implicit capabilities, no hidden side effects.

## Architecture
- **Engine**: Orchestrates action validation, permission checks, sandboxed execution, and audit logging.
- **Permission System**: Declarative, least-privilege JSON policy per agent.
- **Action Schema**: Strict validation of agent actions.
- **Audit Log**: Every action attempt is logged with timestamp and result.
- **Sandbox**: All agent actions occur in an isolated directory.

## Safety Principles
- Minimalism
- Explicitness
- Isolation
- Least Privilege
- Transparency
- Predictability
- Auditability

## Contributing
See [CONTRIBUTING.md](CONTRIBUTING.md) for safe contribution guidelines.

## Documentation
- [Architecture](docs/architecture.md)
- [Threat Model](docs/threat-model.md)
- [Roadmap](docs/roadmap.md)
- [Design Philosophy](docs/design-philosophy.md)

---

**moltbot-safe** is maintained to help the community build safer, more reliable agentic systems.


Implements the principle of **least privilege**.

### 📦 Action Schema
A standardized format for all actions an agent can request.  
Ensures actions are:

- validated  
- well-formed  
- safe to execute  

Prevents malformed or ambiguous operations.

### 📜 Audit Log
Every attempted action — allowed or denied — is recorded.  
This provides:

- transparency  
- traceability  
- debugging insight  
- accountability  

### Project Structure
```
project-root/
├── engine/
│   ├── engine.py
│   ├── permissions.py
│   ├── audit.py
│   ├── action_schema.py
│   ├── permissions.json
│   └── audit.log
├── sandbox/
└── README.md
```


## Safety Principles

### 1. Least Privilege
Agents only receive the minimum permissions required for their tasks.

### 2. Isolation
All execution occurs inside the sandbox directory, never the real filesystem.

### 3. Transparency
Every action is logged, including denied attempts.

### 4. Extensibility
The system is intentionally minimal but easy to extend with new action types, permission models, or sandbox strategies.

## Getting Started

1. Clone the repository:
git clone https://github.com/YOURNAME/moltbot-safe.git

2. Install Python 3.7+.
3. Review and customize `engine/permissions.json`.
4. Use the `AgentEngine` class to execute actions safely.

## Roadmap

- Add more granular permission scopes  
- Add optional network sandboxing  
- Add dry-run mode for previewing actions  
- Add example agents that use the engine  
- Add test suite for action validation and permission enforcement  

## Contributing

Contributions are welcome.  
Please open issues or pull requests to propose features, report bugs, or improve documentation.

All contributions should align with the project’s safety-first philosophy.

---

**moltbot-safe** is maintained to help the community build safer, more transparent, and more responsible agentic systems.
