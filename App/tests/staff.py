import unittest, pytest
from App.main import create_app
from App.database import db, create_db
from App.models import Staff
from App.controllers import create_staff, get_staff_by_id, login
from werkzeug.security import generate_password_hash

class StaffUnitTests(unittest.TestCase):

    def test_new_staff(self):
        staff = Staff("jane", "janepass", "Jane Doe")
        self.assertEqual(staff.name, "Jane Doe")
        self.assertEqual(staff.id, None)
        
    def test_staff_toJSON(self):
        staff = Staff("jane", "janepass", "Jane Doe")
        staff_json = staff.get_json()

        self.assertDictEqual(staff_json, {"id": None, "username": "jane"})
    
    def test_set_password(self):
        password = "janepass"
        staff = Staff("jane", password, "Jane Doe")
        assert staff.password != password

    def test_check_password(self):
        password = "janepass"
        staff = Staff("jane", password, "Jane Doe")
        assert staff.password != password
        assert staff.check_password(password)

@pytest.fixture(autouse=True, scope="module")
def empty_db():
    app = create_app({'TESTING': True, 'SQLALCHEMY_DATABASE_URI': 'sqlite:///test.db'})
    create_db()
    yield app.test_client()
    db.drop_all()

class StaffIntegrationTests(unittest.TestCase):
    def test_create_staff(self):
        staff = create_staff("jane", "janepass", "Jane Doe")

        assert staff.name == "Jane Doe"

    