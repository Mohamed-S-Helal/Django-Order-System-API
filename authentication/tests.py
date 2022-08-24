from rest_framework.test import APITestCase
from django.urls import reverse
import json
from django.contrib.auth.models import User

class InvalidUserRegistrationApiViewTest(APITestCase):
	url = reverse('auth:auth_register')
	def test_invalid_password(self):
		user_data = {
			"username": 'testuser',
			'email': 'test@example.com',
			'password': 'itsstrongpassword',
			'password2': 'anotherpassword',
			'first_name': 'test',
			'last_name': 'test'
		}
		response = self.client.post(self.url, user_data)
		self.assertEqual(400, response.status_code)
		self.assertTrue("password1" in json.loads(response.content))

	def test_username_exist(self):
		user_data1 = {
			"username": 'testuser',
			'email': 'test@example.com',
			'password': 'itsstrongpassword',
			'password2': 'itsstrongpassword',
			'first_name': 'test',
			'last_name': 'test'
		}
		response = self.client.post(self.url, user_data1)
		self.assertEqual(201, response.status_code)
		user_data2 = {
			"username": 'testuser',
			'email': 'test@example.com',
			'password': 'itsstrongpassword',
			'password2': 'itsstrongpassword',
			'first_name': 'test',
			'last_name': 'test'
		}
		response = self.client.post(self.url, user_data2)
		self.assertEqual(400, response.status_code)

	def test_common_password(self):
		user_data = {
			"username": 'testuser',
			'email': 'test@example.com',
			'password': 'password',
			'password2': 'password',
			'first_name': 'test',
			'last_name': 'test'
		}
		response = self.client.post(self.url, user_data)
		self.assertEqual(400, response.status_code)

	def test_length_less_than_8(self):
		user_data = {
			"username": 'testuser',
			'email': 'test@example.com',
			'password': 'testus',
			'password2': 'testus',
			'first_name': 'test',
			'last_name': 'test'
		}
		response = self.client.post(self.url, user_data)
		self.assertEqual(400, response.status_code)



	def test_empty_first_name(self):
		user_data = {
			"username": 'testuser',
			'email': 'test@example.com',
			'password': 'testus',
			'password2': 'testus',
			'first_name': "",
			'last_name': 'test'
		}
		response = self.client.post(self.url, user_data)
		self.assertEqual(400, response.status_code)
	
	def test_empty_last_name(self):
		user_data = {
			"username": 'testuser',
			'email': 'test@example.com',
			'password': 'testus',
			'password2': 'testus',
			'first_name': "test",
			'last_name': ''
		}
		response = self.client.post(self.url, user_data)
		self.assertEqual(400, response.status_code)
	def test_empty_username(self):
		user_data = {
			"username": '',
			'email': 'test@example.com',
			'password': 'testus',
			'password2': 'testus',
			'first_name': "",
			'last_name': 'test'
		}
		response = self.client.post(self.url, user_data)
		self.assertEqual(400, response.status_code)
	def test_empty_password(self):
		user_data = {
			"username": 'testuser',
			'email': 'test@example.com',
			'password': '',
			'password2': '',
			'first_name': "test",
			'last_name': 'test'
		}
		response = self.client.post(self.url, user_data)
		self.assertEqual(400, response.status_code)

	def test_empty_email(self):
		user_data = {
			"username": 'testuser',
			'email': '',
			'password': 'testuser',
			'password2': 'testuser',
			'first_name': "test",
			'last_name': 'test'
		}
		response = self.client.post(self.url, user_data)
		self.assertEqual(400, response.status_code)

