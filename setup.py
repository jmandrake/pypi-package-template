from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

# Search for your proposed package name https://pypi.org
PACKAGE_NAME = ""
YOUR_NAME = ""
EMAIL = ""
VERSION = "0.0.10"
DESCRIPTION = ""
LONG_DESCRIPTION = ""

# Setting up
# Classifiers: https://pypi.org/classifiers/
# Note: you need to customize the install_requires, keywords, and classifiers fields below.
setup(
    name=PACKAGE_NAME,
    version=VERSION,
    author=YOUR_NAME,
    author_email=f"<{EMAIL}>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    install_requires=["python-whois", "py-thesaurus", "random-proxies"],
    keywords=["keyword", "anotherkeyword", "keyword2", "another keyword"],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ],
)
