from unittest import TestCase
import requests
import conftest


class ReceiptsGetTest(TestCase):
    """ Tests GET requests """

    def assertIsExpectedReceipt(self, receiptData):
        """ Asserts that the receipt data corresponds to the expected receipt """
        self.assertEqual(receiptData["receipt_image_id"], self.imageId)
        self.assertEqual(receiptData["store"], "Dagli' Brugsen")
        self.assertEqual(
            receiptData["items"],
            {
                "COOP KAKAO PULVER": 20.95,
                "ØKO DARK CHOKOLADE": 20.95,
                "ØKO DARK CHOKOLADE": 20.95,
                "RABAT": -2.90,
                "ØKO THISE JERSEY LET": 29.90,
                "RABAT": -7.90,
                "WIENERSTANG": 40.00,
                "RABAT": -15.00,
            },
        )

        self.assertEqual(receiptData["total"], 106.95)
        self.assertEqual(receiptData["currency"], "DKK")

    def setUp(self):
        """ POST an image from which a receipt is extracted """
        self.imageFilename = "tests/img/receipt-1.jpg"
        with open(self.imageFilename, "rb") as imageFile:
            files = {"image": imageFile}
            response = requests.post(
                "http://127.0.0.1:5000/receipt_images/", files=files
            )
        self.imageId = response.json()["_id"]

    def testGetAllReceipts(self):
        """ GETting all receipts """

        response = requests.get("http://127.0.0.1:5000/receipts/")

        #  yields a 200 'OK' response
        self.assertEqual(response.status_code, 200)

        # of content type json
        self.assertEqual(response.headers["content-type"], "application/json")

        # with the body a json document
        json = response.json()

        # it has one item
        self.assertEqual(len(json["_items"]), 1)

        # with the receipt data
        self.assertIsExpectedReceipt(json["_items"][0])

    def tearDown(self):
        conftest.clearDb()
