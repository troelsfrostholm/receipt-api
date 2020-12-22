receipts_schema = {"image": {"type": "media"}}

receipts = {
    "item_title": "receipt",
    "resource_methods": ["GET", "POST"],
    "schema": receipts_schema,
}

DOMAIN = {"receipts": receipts}
MONGO_HOST = "localhost"
MONGO_PORT = 27017

# Skip this block if your db has no auth. But it really should.
# MONGO_USERNAME = "<your username>"
# MONGO_PASSWORD = "<your password>"
# Name of the database on which the user can be authenticated,
# needed if --auth mode is enabled.
# MONGO_AUTH_SOURCE = "<dbname>"

MONGO_DBNAME = "apitest"

# Enable reads (GET), inserts (POST) and DELETE for resources/collections
# (if you omit this line, the API will default to ['GET'] and provide
# read-only access to the endpoint).
RESOURCE_METHODS = ["GET", "POST", "DELETE"]

# Enable reads (GET), edits (PATCH), replacements (PUT) and deletes of
# individual items  (defaults to read-only item access).
ITEM_METHODS = ["GET", "PATCH", "PUT", "DELETE"]
