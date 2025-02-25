from setuptools import setup

setup(
    name="sarcastic-commit",
    version="1.0",
    py_modules=["sarcastic_commit", "messages"],
    install_requires=[],
    entry_points={
        "console_scripts": [
            "sarcastic-commit=sarcastic_commit:main",
        ],
    },
)
