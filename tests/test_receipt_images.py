"""
  End-to-end tests of the /receipt_images/ resource
"""

from unittest import TestCase
import requests
import conftest
from datetime import datetime, timezone
import re
import base64


class ReceiptImagesPostTest(TestCase):
    """ Tests POST requests """

    def setUp(self):
        pass

    def testPostReceiptImage(self):
        """ POSTing a new vaild receipt_image with an image file"""

        files = {"image": open("tests/img/receipt-1.jpg", "rb")}

        now = datetime.now(timezone.utc).strftime("%a, %d %b %Y %H:%M:%S GMT")
        response = requests.post("http://127.0.0.1:5000/receipt_images/", files=files)

        # yields a 201 'created' response
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.encoding, "utf-8")

        # with a json body
        json = response.json()

        # with OK status
        self.assertEqual(json["_status"], "OK")

        # created now
        self.assertEqual(json["_created"], now)
        self.assertEqual(json["_updated"], now)

        # with an id and an etag
        self.assertEqual(len(json["_id"]), 24)
        r = re.compile(r"[a-z0-9]")
        self.assertTrue(r.match(json["_id"]))
        self.assertTrue(r.match(json["_etag"]))

        # and a link to the new image resource
        self.assertEqual(
            json["_links"],
            {
                "self": {
                    "title": "receipt_image",
                    "href": "receipt_images/" + json["_id"],
                }
            },
        )

        # HTTP response link headers are empty
        self.assertEqual(response.links, {})
        self.assertEqual(response.next, None)

        # The image has been inserted into the database
        imageDoc = conftest.db["receipt_images"].find_one()
        self.assertEqual(str(imageDoc["_id"]), json["_id"])

    def tearDown(self):
        conftest.clearDb()


class ReceiptImagesGetTest(TestCase):
    """ Tests GET requests """

    def setUp(self):
        """ POST an image that can be used to test GETing """
        self.imageFilename = "tests/img/receipt-1.jpg"
        with open(self.imageFilename, "rb") as imageFile:
            files = {"image": imageFile}
            response = requests.post(
                "http://127.0.0.1:5000/receipt_images/", files=files
            )
        self.imageId = response.json()["_id"]

    def testGetMissingReceiptImage(self):
        """ Trying to GET a non-existing receipt_image"""

        response = requests.get(
            "http://127.0.0.1:5000/receipt_images/5fe23235ace93fe3c000004d"
        )

        # yields a 404 'resource not found' response
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.encoding, "utf-8")

        # with a json body
        json = response.json()

        # with ERR status
        self.assertEqual(json["_status"], "ERR")

        # and an error with code 404
        self.assertTrue("_error" in json)
        self.assertEqual(json["_error"]["code"], 404)

        # HTTP response link headers are empty
        self.assertEqual(response.links, {})
        self.assertEqual(response.next, None)

    def testGetReceiptImage(self):
        """ GETting an existing receipt_image """

        response = requests.get("http://127.0.0.1:5000/receipt_images/" + self.imageId)

        #  yields a 200 'OK' response
        self.assertEqual(response.status_code, 200)

        # of content type json
        self.assertEqual(response.headers["content-type"], "application/json")

        # with the body a json document
        json = response.json()

        # with the requested id
        self.assertEqual(json["_id"], self.imageId)

        # and the correct image data
        imageData = json["image"]

        with open(self.imageFilename, "rb") as imageFile:
            expectedImageData = base64.b64encode(imageFile.read())
            expectedImageData = str(expectedImageData, "utf-8")

        self.assertEqual(expectedImageData, imageData)

    def testGetReceiptImages(self):
        """ GETting an existing receipt_image """

        response = requests.get("http://127.0.0.1:5000/receipt_images/")

        #  yields a 200 'OK' response
        self.assertEqual(response.status_code, 200)

        # of content type json
        self.assertEqual(response.headers["content-type"], "application/json")

        # with the body a json document
        json = response.json()

        # it has one item
        self.assertEqual(len(json["_items"]), 1)

        # which contains the inserted id
        self.assertEqual(json["_items"][0]["_id"], self.imageId)

        # and the correct image data
        imageData = json["_items"][0]["image"]

        with open(self.imageFilename, "rb") as imageFile:
            expectedImageData = base64.b64encode(imageFile.read())
            expectedImageData = str(expectedImageData, "utf-8")

        self.assertEqual(expectedImageData, imageData)

    def tearDown(self):
        conftest.clearDb()


class ReceiptImagesDeleteTest(TestCase):
    """ Tests DELETE requests """

    def setUp(self):
        """ POST an image that can be used to test DELETE """
        self.imageFilename = "tests/img/receipt-1.jpg"
        with open(self.imageFilename, "rb") as imageFile:
            files = {"image": imageFile}
            response = requests.post(
                "http://127.0.0.1:5000/receipt_images/", files=files
            )
        self.imageId = response.json()["_id"]
        self.imageEtag = response.json()["_etag"]

    def testDeleteReceiptImage(self):
        """ DELETEing an existing image """

        headers = {"if-match": self.imageEtag}
        url = "http://127.0.0.1:5000/receipt_images/" + self.imageId
        response = requests.delete(url, headers=headers)

        # yields a 204 'NO CONTENT' response
        self.assertEqual(response.status_code, 204)

        # with an empty body
        self.assertEqual(response.text, "")

        # and the image has been removed from the database
        imageDoc = conftest.db["receipt_images"].find()
        imageDoc = list(imageDoc)
        self.assertEqual(imageDoc, [])

    def tearDown(self):
        conftest.clearDb()
