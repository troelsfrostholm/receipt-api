""" PyTest configuration """

from receiptapi import server
from multiprocessing import Process
import time
import sys

""" Name of test database """
dbname = "receipts_test"


def run_server():
    sys.stdout = open("server-test.log", "w")
    sys.stderr = open("server-test-err.log", "w")
    server.run(dbname)


serverProcess = Process(target=run_server)


def pytest_sessionstart(session):
    """ Callback runs before all tests """

    serverProcess.start()
    # Let the server start up before running the test
    time.sleep(0.5)


def pytest_sessionfinish(session, exitstatus):
    """ Callback runs after all tests finish """

    serverProcess.terminate()
