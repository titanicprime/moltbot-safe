# Security Policy

moltbot-safe is security-first: minimal, explicit, isolated, and auditable by design.

## Security Posture
- **Least Privilege**: Agents can only perform actions explicitly allowed in `permissions.json`.
- **Isolation**: All agent actions are sandboxed; no access outside the sandbox.
- **Transparency**: Every action—allowed or denied—is logged.
- **No Implicit Capabilities**: No inferred or default permissions.
- **No Autonomous Expansion**: The engine cannot grant itself new abilities.

## Threat Model Boundaries
- **In Scope**: Malicious or buggy agents, misconfigured permissions, audit log tampering.
- **Out of Scope**: OS-level sandbox escapes, external attackers not acting through the agent.

## Responsible Disclosure
If you discover a vulnerability, open a private security advisory or contact the maintainers. Do not disclose vulnerabilities publicly until resolved. Provide details, steps to reproduce, and suggested mitigations if possible.

The engine should never grant an agent more access than explicitly defined in `permissions.json`.

### 2. Isolation by Default
All agent actions must occur inside the sandbox directory.  
No direct filesystem access outside the sandbox is permitted.

### 3. Transparent Execution
Every attempted action—allowed or denied—must be logged in `audit.log`.

### 4. No Implicit Capabilities
The engine must never infer or assume permissions.  
All capabilities must be explicitly declared.

### 5. No Autonomous Expansion
The engine must not add new abilities, escalate privileges, or modify its own permissions without human intervention.

---

## Threat Model (High-Level)

**moltbot-safe** assumes the following:

### In-Scope Threats
- Malicious or buggy agent requests  
- Attempts to escape the sandbox  
- Attempts to access unauthorized files  
- Attempts to perform network operations without permission  
- Attempts to modify permissions or audit logs  
- Malformed or adversarial action schemas  

### Out-of-Scope Threats
- Host OS compromise  
- Kernel-level attacks  
- Hardware-level attacks  
- Supply-chain attacks outside this repository  

This project focuses on **application-level safety**, not full system hardening.

---

## Security Roadmap

- Add optional network sandboxing  
- Add permission scopes for subprocesses  
- Add integrity checks for audit logs  
- Add test suite for sandbox escape attempts  
- Add fuzz testing for action schema validation  

---

## Responsible Use

This project is intended to help developers build safer agentic systems.  
It should not be used to grant unrestricted system access to autonomous agents.

Use responsibly, and always review permissions before deploying.

---

Thank you for helping keep **moltbot-safe** secure.
