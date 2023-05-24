import unittest
from datetime import datetime
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):
    """
    Unit tests for the BaseModel class.
    """

    def setUp(self):
        """
        Set up a new instance of BaseModel for each test.
        """
        self.base_model = BaseModel()

    def test_attributes(self):
        """
        Test the attributes of the BaseModel instance.
        """
        self.assertIsInstance(self.base_model.id, str)
        self.assertIsInstance(self.base_model.created_at, datetime)
        self.assertIsInstance(self.base_model.updated_at, datetime)

    def test_save(self):
        """
        Test the save method of the BaseModel instance.
        """
        prev_updated_at = self.base_model.updated_at
        self.base_model.save()
        self.assertNotEqual(prev_updated_at, self.base_model.updated_at)

    def test_to_dict(self):
        """
        Test the to_dict method of the BaseModel instance.
        """
        obj_dict = self.base_model.to_dict()

        self.assertIsInstance(obj_dict, dict)
        self.assertEqual(obj_dict['__class__'], 'BaseModel')
        self.assertEqual(obj_dict['id'], self.base_model.id)
        self.assertEqual(obj_dict['created_at'], self.base_model.created_at.isoformat())
        self.assertEqual(obj_dict['updated_at'], self.base_model.updated_at.isoformat())

    def test_str(self):
        """
        Test the __str__ method of the BaseModel instance.
        """
        expected_str = f"[BaseModel] ({self.base_model.id}) {self.base_model.__dict__}"
        self.assertEqual(str(self.base_model), expected_str)

if __name__ == '__main__':
    unittest.main()

