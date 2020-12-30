from unittest import TestCase
import requests
from pymongo import MongoClient


class APITest(TestCase):
    def setUp(self):
        pass

    def testPostReceipt(self):
        files = {"image": open("tests/img/receipt-1.jpg", "rb")}
        response = requests.post("http://127.0.0.1:5000/receipts/", files=files)
        self.assertEqual(response.status_code, 201)

    def testGetReceipt(self):
        response = requests.get(
            "http://127.0.0.1:5000/receipts/5fe23235ace93fe3c000004d"
        )
        self.assertEqual(response.status_code, 200)

    def tearDown(self):
        mongo_client = MongoClient("mongodb://localhost:27017")
        mongo_client.drop_database("receipts_test")
