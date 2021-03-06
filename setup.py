from setuptools import find_packages, setup

with open("README.md") as f:
    long_description = f.read()

setup(
    name="teext",
    version="0.2.0.dev1",
    author="PAL",
    author_email="info@predictive-analytics-lab.com",
    description="Typing extensions extensions",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/predictive-analytics-lab/teext",
    license="Apache License 2.0",
    packages=find_packages(exclude=["tests.*", "tests"]),
    package_data={"teext": ["py.typed"]},
    python_requires=">=3.6",
    install_requires=[],
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Typing :: Typed",
    ],
    keywords=["typing", "python"],
)
