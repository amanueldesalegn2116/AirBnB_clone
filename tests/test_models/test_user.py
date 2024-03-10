#!/usr/bin/python3

""" 
This script contains unit tests for the User class.
"""
from tests.test_models.test_base_model import test_basemodel
from models.user import User


class test_User(test_basemodel):
    """ 
    Test suite for the User class.
    """

    def __init__(self, *args, **kwargs):
        """ 
        Initialize the test suite with necessary attributes.
        """
        super().__init__(*args, **kwargs)
        self.name = "User"
        self.value = User

    def test_first_name(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.first_name), str)

    def test_last_name(self):
        """ 
        Test if first_name attribute is of type string.
        """
        new = self.value()
        self.assertEqual(type(new.last_name), str)

    def test_email(self):
        """ 
        Test if last_name attribute is of type string.
        """
        new = self.value()
        self.assertEqual(type(new.email), str)

    def test_password(self):
        """
        Test if password attribute is of type string.
        """
        new = self.value()
        self.assertEqual(type(new.password), str)
