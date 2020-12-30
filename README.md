# receipt-api
A RESTful web api for organizing and storing receipts. 

receipt-api is a demo project for a job interview with [OTH.IO](http://www.oth.io/ "OTH.IO")

Please note, this is **not production code**, and **should not be used for anything serious** whatsoever. Use at your own risk, and only while having fun!

## Installation

Install the following dependencies:

[Python 3](https://www.python.org/downloads/)

[MongoDB](https://docs.mongodb.com/manual/installation/#mongodb-community-edition-installation-tutorials "MongoDB")

Install receipt-api:
```bash
pip3 install git+https://github.com/troelsfrostholm/receipt-api.git
```

## Run the tests (optional)
Unit tests are based on pytest and executed using tox. In order to run the tests, the repository must be cloned. 
```bash
git clone git://github.com/troelsfrostholm/receipt-api.git
cd receipt-api
tox
```

## Start the api server
Installing with pip installs the following command to start the server, which can be invoked from anywhere.

```bash
$ receiptapi

 * Serving Flask app "eve" (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```

## Example usage

The receipt api is used for uploading an image of a receipt. The receipt is scanned for data, including the name of the store, the items bought and their prices, and the grand total. 

A typical usage example could be the following: 

POST a new receipt image:
```bash
curl -F "image=@./tests/img/receipt-1.jpg" http://127.0.0.1:5000/receipt_images
```

```json
{
  "_updated": "Wed, 30 Dec 2020 15:33:16 GMT",
  "_created": "Wed, 30 Dec 2020 15:33:16 GMT",
  "_etag": "609c0a718a41becc4f3186baa9cc0142c616d37d",
  "_id": "5fec9dbc65ccf59ec6bc8b90",
  "_links": {
    "self": {
      "title": "receipt_image",
      "href": "receipt_images/5fec9dbc65ccf59ec6bc8b90"
    }
  },
  "_status": "OK"
}
```

Behind the scenes, a receipt resource has been created. It can be retrieved with a GET request:
```bash
curl -i http://127.0.0.1:5000/receipts/where={"receipt_image": "5fec9dbc65ccf59ec6bc8b90"}
```

```json
{
    "receipt_image_id": "5fec9dbc65ccf59ec6bc8b90",
    "store": "Brugsen",
    "items":  [ {"title": "Milk", "price": 37.50} ],
    "total": 37.50,
    "currency": "DKK",
    "_id": "50acfba938345b0978fccad7",
    "_updated": "Wed, 30 Dec 2020 15:33:16 GMT",
    "_created": "Wed, 30 Dec 2020 15:33:16 GMT",
    "_etag": "28995829ee85d69c4c18d597a0f68ae606a266cc",
    "_links": {
        "self": {"href": "receipts/50acfba938345b0978fccad7", "title": "receipt"},
        "parent": {"href": "/", "title": "home"},
        "collection": {"href": "receipts", "title": "receipts"}
    }
}
```

## Documentation

The full API documentation can be found [here](DOCUMENTATION.md)