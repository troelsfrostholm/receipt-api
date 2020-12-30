"""
  End-to-end tests of the /receipt_images/ resource
"""

from unittest import TestCase
import requests
from pymongo import MongoClient
from conftest import dbname


def clearDb():
    """ Clears the database """

    mongo_client = MongoClient("mongodb://localhost:27017")
    mydb = mongo_client[dbname]
    mydb["receipt_images"].drop()


class ReceiptImagesGetTest(TestCase):
    """ Tests GET requests """

    def setUp(self):
        pass

    def testGetReceiptImage(self):
        """ Trying to GET a non-existing receipt_image yields a 404 'resource not found' response """

        response = requests.get(
            "http://127.0.0.1:5000/receipt_images/5fe23235ace93fe3c000004d"
        )
        self.assertEqual(response.status_code, 404)

    def tearDown(self):
        clearDb()


class ReceiptImagesPostTest(TestCase):
    """ Tests POST requests """

    def setUp(self):
        pass

    def testPostReceiptImage(self):
        """ POSTing a new vaild receipt_image with an image file yields a 201 'created' response"""

        files = {"image": open("tests/img/receipt-1.jpg", "rb")}
        response = requests.post("http://127.0.0.1:5000/receipt_images/", files=files)
        self.assertEqual(response.status_code, 201)

    def tearDown(self):
        clearDb()
