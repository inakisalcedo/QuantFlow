from setuptools import setup, find_packages

setup(
    name="quantflow",
    version="0.1.0",
    author="Iñaki Salcedo",
    description="Library for crypto-market analysis and macro metrics",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/inakisalcedo/QuantFlow",
    packages=find_packages(),
    install_requires=[
        "pandas",
        "ccxt",
        "pandas-datareader",
        "yfinance",
        "fear-and-greed-crypto",
        "requests"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
)
