# Minimal action schema definition

def validate_action(action):
    if not isinstance(action, dict):
        raise ValueError('Action must be a dict')
    if 'type' not in action:
        raise ValueError('Action must have a type')
    # Add more validation as needed
    return True

