from setuptools import setup


with open("README.md") as f:
    long_description = f.read()


setup(
    name="asl5000-utils",
    version="0.1.0",
    author="deplanty",
    description="A toolbox to extract data from the ASL5000",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/deplanty/asl5000_utils",
    packages=["asl5000_utils"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent"
    ]
)
