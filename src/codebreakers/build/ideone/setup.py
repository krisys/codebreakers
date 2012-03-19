import os
from setuptools import setup

f = open(os.path.join(os.path.dirname(__file__), 'README.rst'))
readme = f.read()
f.close()

VERSION = "0.1.4"

setup(
    name = "ideone",
    version = VERSION,
    author = "Joe Schafer",
    author_email = "joe@jschaf.com",
    url = "http://github.com/jschaf/ideone-api/",
    description = "A Python binding to the Ideone (Online Compiler) API.",
    license = "BSD",
    platforms = ["any"],
    keywords = "API, ideone, codepad",
    packages = ['ideone'],
    long_description=readme,
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: BSD License",
    ],
    install_requires=['suds'],
)
