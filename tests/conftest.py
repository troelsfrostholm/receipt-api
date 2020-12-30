from receiptapi import server
from multiprocessing import Process
import time

serverProcess = Process(target=server.run, args=("receipts_test",))


def pytest_sessionstart(session):
    serverProcess.start()
    # Let the server start up before running the test
    time.sleep(0.5)


def pytest_sessionfinish(session, exitstatus):
    serverProcess.terminate()
