from setuptools import setup

setup(
    name="receiptapi",
    version="0.1",
    description="RESTful web api for storing receipts",
    url="https://github.com/troelsfrostholm/receipt-api",
    author="Troels Frostholm Mogensen",
    author_email="troelsfrostholm@gmail.com",
    license="GPLv3.0",
    packages=["receiptapi"],
    entry_points={
        "console_scripts": ["receiptapi=receiptapi.server:run"],
    },
    install_requires=[
        "eve",
    ],
    tests_requires= [
        "pytest",
    ]
    zip_safe=False,
)
