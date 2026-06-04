# core/validator.py

from core.command_registry import is_valid_command

CONFIDENCE_THRESHOLD = 0.80


def validate_command(command: str) -> bool:
    """
    Check if command exists in registry.
    """
    return is_valid_command(command)


def validate_confidence(confidence: float) -> bool:
    """
    Check if confidence is above threshold.
    """
    return confidence >= CONFIDENCE_THRESHOLD


def validate_request(command: str, confidence: float) -> tuple:
    """
    Validate both command and confidence.
    Returns:
        (True, "Valid Request")
        (False, "Invalid Command")
        (False, "Low Confidence")
    """

    if not validate_command(command):
        return False, "Invalid Command"

    if not validate_confidence(confidence):
        return False, "Low Confidence"

    return True, "Valid Request"