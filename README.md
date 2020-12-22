# receipt-api
A RESTful web api for organizing and storing receipts. 

receipt-api is a demo project for OTH.IO job interview. 

Please note, this is not production code, and should not be used for anything serious whatsoever. Use at your own risk, and only while having fun!

## Installation

Install the following dependencies:

[Python 3](https://www.python.org/downloads/)

[Mongodb](https://docs.mongodb.com/manual/installation/#mongodb-community-edition-installation-tutorials "MongoDB")

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