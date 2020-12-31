"""
    REST API definition and server application

"""

from eve import Eve

"""
  Receipt images
"""

receipt_images_schema = {"image": {"type": "media"}}

receipt_images = {
    "item_title": "receipt_image",
    "resource_methods": ["GET", "POST"],
    "schema": receipt_images_schema,
}

"""
  Receipt data
"""

receipts_schema = {
    "receipt_image_id": {
        "type": "objectid",
        "data_relation": {"resource": "receipt_images", "field": "_id"},
    },
    "store": {
        "type": "string",
        "minlength": 1,
        "maxlength": 255,
    },
    "items": {
        "type": "list",
    },
    "total": {"type": "float"},
    "currency": {"type": "string", "minlength": 3, "maxlength": 3},
}

receipts = {
    "item_title": "receipt",
    "resource_methods": ["GET"],
    "schema": receipts_schema,
}

"""
    Server settings
"""

settings = {
    "DOMAIN": {"receipt_images": receipt_images, "receipts": receipts},
    "MONGO_HOST": "localhost",
    "MONGO_PORT": 27017,
    # To simplify this demo, authorization on MongoDB is disabled
    # It should of course be enabled in actual use
    # MONGO_USERNAME : "<your username>"
    # MONGO_PASSWORD : "<your password>"
    # MONGO_AUTH_SOURCE : "<dbname>"
    "MONGO_DBNAME": "receipt_images",
    # Enable reads (GET), inserts (POST) and DELETE for resources/collections
    # (if you omit this line, the API will default to ['GET'] and provide
    # read-only access to the endpoint).
    "RESOURCE_METHODS": ["GET", "POST", "DELETE"],
    # Enable reads (GET), edits (PATCH), replacements (PUT) and deletes of
    # individual items  (defaults to read-only item access).
    "ITEM_METHODS": ["GET", "PATCH", "PUT", "DELETE"],
}


def extractReceiptFrom(imageId, image):
    """ Extracts receipt data from an image """

    return {
        "receipt_image_id": imageId,
        "store": "Dagli' Brugsen",
        "items": {
            "COOP KAKAO PULVER": 20.95,
            "ØKO DARK CHOKOLADE": 20.95,
            "ØKO DARK CHOKOLADE": 20.95,
            "RABAT": -2.90,
            "ØKO THISE JERSEY LET": 29.90,
            "RABAT": -7.90,
            "WIENERSTANG": 40.00,
            "RABAT": -15.00,
        },
        "total": 106.95,
        "currency": "DKK",
    }


def receipt_images_inserted(items):
    """
    Callback function for after image items have been inserted into the database

    Extracts receipt data from the imae and inserts it into the database

    """

    global app

    for item in items:
        receiptJson = extractReceiptFrom(item["_id"], item["image"])
        app.data.insert("receipts", [receiptJson])


def run(dbname=None):
    """ Starts the server """

    global app

    if dbname:
        settings["MONGO_DBNAME"] = dbname

    app = Eve(settings=settings)
    app.on_inserted_receipt_images += receipt_images_inserted
    app.run()


if __name__ == "__main__":
    run()
