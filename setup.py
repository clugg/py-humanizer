import os
import re

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

PACKAGE_NAME = "humanizepy"

HERE = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(HERE, "README.md")) as fp:
    README = fp.read()
with open(os.path.join(HERE, PACKAGE_NAME, "__init__.py")) as fp:
    VERSION = re.search("__version__ = \"([^\"]+)\"", fp.read()).group(1)

setup(
    name=PACKAGE_NAME,
    version=VERSION,
    author="James \"clug\"",
    author_email="pip@clug.xyz",
    maintainer="James \"clug\"",
    maintainer_email="pip@clug.xyz",
    url="https://github.com/clugg/humanizepy",
    description=("Humanize values that are readable only for developers."),
    long_description=README,
    classifiers=["Development Status :: 5 - Production/Stable",
                 "Environment :: Console",
                 "Intended Audience :: Developers",
                 "License :: OSI Approved :: MIT License",
                 "Natural Language :: English",
                 "Operating System :: OS Independent",
                 "Programming Language :: Python",
                 "Programming Language :: Python :: 2.7",
                 "Programming Language :: Python :: 3.3",
                 "Programming Language :: Python :: 3.4",
                 "Programming Language :: Python :: 3.5",
                 "Topic :: Utilities"],
    license="MIT",
    keywords="humanize values roman numeral binary",
    packages=[PACKAGE_NAME]
)