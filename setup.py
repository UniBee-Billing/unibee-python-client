# coding: utf-8
"""
UniBee Python SDK

A Python SDK for interacting with the UniBee billing API.
"""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

NAME = "unibee"
VERSION = "1.1.0"
PYTHON_REQUIRES = ">=3.8"

REQUIRES = [
    "urllib3>=1.25.3,<3.0.0",
    "python-dateutil>=2.5.3",
]

# Optional dependencies for development
EXTRAS_REQUIRE = {
    "dev": [
        "pytest>=7.0.0",
        "pytest-cov>=4.0.0",
        "black>=23.0.0",
        "isort>=5.12.0",
        "mypy>=1.0.0",
        "flake8>=6.0.0",
    ],
}

setup(
    name=NAME,
    version=VERSION,
    description="UniBee Python SDK - Billing API client for SaaS businesses",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="UniBee",
    author_email="support@unibee.dev",
    url="https://github.com/UniBee-Billing/unibee-python-client",
    project_urls={
        "Documentation": "https://docs.unibee.dev/",
        "Source": "https://github.com/UniBee-Billing/unibee-python-client",
        "Bug Tracker": "https://github.com/UniBee-Billing/unibee-python-client/issues",
    },
    keywords=[
        "unibee",
        "billing",
        "subscription",
        "payment",
        "saas",
        "invoice",
        "api",
        "sdk",
    ],
    install_requires=REQUIRES,
    extras_require=EXTRAS_REQUIRE,
    python_requires=PYTHON_REQUIRES,
    packages=find_packages(exclude=["test", "tests", "docs", "openapi_client"]),
    include_package_data=True,
    license="Apache-2.0",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Office/Business :: Financial :: Accounting",
    ],
    package_data={"unibee": ["py.typed"]},
)
