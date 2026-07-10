import re
from inflect import engine
from .messages import Message

inflector = engine()

VALID = (True, None)
# => wrapper method for validating inputs
def get_validated_input(is_valid=lambda _: (True, None), input_function=None):
    if input_function is None:
        input_function = input
        
    def validate_function(prompt=' '):
        while True:
            user_entry = input_function(prompt)

            valid, error = is_valid(user_entry)
            if valid: return user_entry
            prompt = error or ''

    return validate_function


def name_validator(name):
    is_valid = not re.search(r'[^A-Z\s-]', name, re.IGNORECASE) and name

    return VALID if is_valid else (False, Message.verify_name())


def verify_name_integrity(prompt):
    return get_validated_input(name_validator)(prompt)


def get_valid_choice(choices, prompt='', case_sensitive=False):
    if not choices:
        raise ValueError("choices must not be empty")

    error_message = f"Please enter {inflector.join(choices, conj='or')}: "
    normalized = set(choices) if case_sensitive else {c.lower() for c in choices}

    def validator(choice):
        entry = choice if case_sensitive else choice.lower()

        return VALID if entry in normalized else (False, error_message)

    return get_validated_input(validator)(prompt)
