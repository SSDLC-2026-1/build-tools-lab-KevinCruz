import unittest
from src.validator import validate_attendee

class TestValidator(unittest.TestCase):

    def test_valid_attendee(self):
        attendee = {
            "name": "Sara Palacios",
            "email": "sara@example.com",
            "age": 25,
            "ticket_type": "vip",
            "registration_code": "EV-1234"
        }
        self.assertEqual(validate_attendee(attendee), [])

    def test_invalid_email(self):
        attendee = {
            "name": "Juan",
            "email": "juanexample.com",
            "age": 20,
            "ticket_type": "general",
            "registration_code": "EV-5678"
        }
        self.assertIn("Invalid email", validate_attendee(attendee))

    def test_underage_attendee(self):
        attendee = {
            "name": "Ana",
            "email": "ana@example.com",
            "age": 16,
            "ticket_type": "student",
            "registration_code": "EV-9012"
        }
        self.assertIn("Attendee must be 18 or older", validate_attendee(attendee))

    def test_invalid_id(self):
        attendee = {
            "name": "Carlos",
            "email": "carlos@example.com",
            "age": 20,
            "ticket_type": "general",
            "registration_code": "AB-1234"
        }
        self.assertIn("Invalid registration identifier", validate_attendee(attendee))

    def test_missing_id(self):
        attendee = {
            "name": "Maria",
            "email": "maria@example.com",
            "age": 22,
            "ticket_type": "vip"
        }
        self.assertIn("Invalid registration identifier", validate_attendee(attendee))

if __name__ == "__main__":
    unittest.main()