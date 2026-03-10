import re

VALID_TICKETS = {"general", "vip", "student"}

def is_valid_email(email: str) -> bool:
    pattern = r"^[^@\s]+@[^@\s]+\.[^@\s]+$"
    return re.match(pattern, email) is not None

def is_valid_id(id_str: str):
    if len(id_str) != 7:
        return False
    if id_str[:3] != "EV-":
        return False
    if not id_str[3:].isdigit():
        return False
    return True

def validate_attendee(attendee: dict) -> list:
    errors = []

    if not attendee.get("name") or not attendee["name"].strip():
        errors.append("Invalid name")

    if not is_valid_email(attendee.get("email", "")):
        errors.append("Invalid email")

    age = attendee.get("age")
    if not isinstance(age, int) or age < 18:
        errors.append("Attendee must be 18 or older")

    if attendee.get("ticket_type") not in VALID_TICKETS:
        errors.append("Invalid ticket type")

    if not attendee.get("ID") or not is_valid_id(attendee["ID"]):
        errors.append("Invalid registration identifier")

    return errors