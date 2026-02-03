from config import AGE_MIN, AGE_MAX, EMAIL_REQUIRED_SYMBOL

def validate_record(record):
    errors = []

    name = record.get("name", "").strip()
    if not name:
        errors.append("Name missing")

    try:
        age = int(record.get("age", ""))
        if age < AGE_MIN or age > AGE_MAX:
            errors.append("Age out of range")
    except ValueError:
        errors.append("Age not integer")

    email = record.get("email", "")
    if EMAIL_REQUIRED_SYMBOL not in email:
        errors.append("Invalid email")

    return errors
