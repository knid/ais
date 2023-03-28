# -*- coding: utf-8 -*-
import sys

from setuptools import find_packages, setup

import ais

tests_require = [
    "pytest",
]

dev_require = [
    *tests_require,
    "flake8",
    "pyyaml",
    "twine",
    "wheel",
]

install_requires = [
    "questionary==1.10.0",
    "requests==2.28.2",
    "rich==13.3.3",
    "setuptools",
]

extras_require = {
    "dev": dev_require,
    "test": tests_require,
}


def long_description():
    with open("README.md", encoding="utf-8") as f:
        return f.read()


setup(
    name="ais-cli",
    version=ais.__version__,
    description="Ais (ai shell) is interactive command line ai tool powered by ChatGPT (GPT-3.5)",
    long_description=long_description(),
    long_description_content_type="text/markdown",
    author=ais.__author__,
    author_email="sinan_kanidagli@hotmail.com",
    license=ais.__licence__,
    packages=find_packages(include=["ais", "ais.*"]),
    entry_points={
        "console_scripts": [
            "ais = ais.__main__:main",
        ],
    },
    python_requires=">=3.7",
    extras_require=extras_require,
    install_requires=install_requires,
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3 :: Only",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "License :: OSI Approved :: MIT License",
        "Topic :: Software Development",
        "Topic :: System :: Networking",
        "Topic :: Terminals",
        "Topic :: Text Processing",
        "Topic :: Utilities",
    ],
    project_urls={
        "GitHub": "https://github.com/knid/ais",
        "Twitter": "https://twitter.com/devknid",
        "Documentation": "https://github.com/knid/ais/README.md",
    },
)
