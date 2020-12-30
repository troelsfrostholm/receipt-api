from eve import Eve

receipts_schema = {"image": {"type": "media"}}

receipts = {
    "item_title": "receipt_image",
    "resource_methods": ["GET", "POST"],
    "schema": receipts_schema,
}

my_settings = {
    "DOMAIN": {"receipt_images": receipts},
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


def run(dbname=None):
    if dbname:
        my_settings["MONGO_DBNAME"] = dbname
    app = Eve(settings=my_settings)
    app.run()


if __name__ == "__main__":
    run()
