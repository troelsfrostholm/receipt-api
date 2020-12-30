""" PyTest configuration """

from receiptapi import server
from multiprocessing import Process
import time

""" Name of test database """
dbname = "receipts_test"

serverProcess = Process(target=server.run, args=(dbname,))


def pytest_sessionstart(session):
    """ Callback runs before all tests """

    serverProcess.start()
    # Let the server start up before running the test
    time.sleep(0.5)


def pytest_sessionfinish(session, exitstatus):
    """ Callback runs after all tests finish """

    serverProcess.terminate()
