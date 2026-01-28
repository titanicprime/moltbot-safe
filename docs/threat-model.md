# Threat Model

## Assets
- Host filesystem outside the sandbox
- User data and credentials
- Network access and external services
- System integrity
- Audit logs and permission configuration

## Actors
- **Agent**: Untrusted, may be buggy or adversarial
- **User**: Trusted but may misconfigure permissions
- **External Attacker**: Out of scope unless acting through the agent

## In-Scope Threats
- Privilege escalation by agent
- Sandbox escape via filesystem
- Action injection or malformed actions
- Audit log tampering
- Misconfigured or overly broad permissions

## Out-of-Scope Threats
- OS-level sandbox escapes
- Direct attacks on the host not mediated by the agent

## Mitigations
- Strict permission checks
- Directory-based sandboxing
- Action schema validation
- Append-only audit log

## Future Hardening
- OS-level sandboxing (containers)
- Digital signatures for audit logs
- Automated permission review tools
