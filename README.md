# receipt-api
A RESTful web api for organizing and storing receipts. 

receipt-api is a demo project for a job interview with [OTH.IO](http://www.oth.io/ "OTH.IO")

Please note, this is not production code, and should not be used for anything serious whatsoever. Use at your own risk, and only while having fun!

## Installation

Install the following dependencies:

[Python 3](https://www.python.org/downloads/)

[MongoDB](https://docs.mongodb.com/manual/installation/#mongodb-community-edition-installation-tutorials "MongoDB")

Install receipt-api:
```bash
pip3 install git+https://github.com/troelsfrostholm/receipt-api.git
```

## Run the tests
Unit tests are based on pytest and executed using tox. 
```bash
cd receipt-api
tox
```

## Start the api server

```bash
receiptapi
```

Try it out with a few calls, for instance using curl. 

Send a POST request to /receipts with an image of a receipt to add it. 
```bash
curl -F "image=@./test/img/receipt-1.jpg" http://127.0.0.1:5000/receipts
```

```json
{"_updated": "Tue, 22 Dec 2020 17:51:49 GMT", "_created": "Tue, 22 Dec 2020 17:51:49 GMT", "_etag": "e49e481e9c9af5a3657d7c14fa8a991a7e539d4d", "_id": "5fe23235ace93fe3c000004d", "_links": {"self": {"title": "receipt", "href": "receipts/5fe23235ace93fe3c000004d"}}, "_status": "OK"}
```

And get it back with a GET request.Remember to replace the id with the one you got back above. 
```bash
curl -i http://127.0.0.1:5000/receipts/5fe23235ace93fe3c000004d
```