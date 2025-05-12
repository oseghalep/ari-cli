from setuptools import setup, find_packages

setup(
    name="ari-cli",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[
        "paramiko",
    ],
    entry_points={
        "console_scripts": [
            "ari=ari_cli.ari:main",
        ],
    },
)