import setuptools


with open("README.md") as f:
    long_description = f.read()


setuptools.setup(
    name="asl5000-utils",
    version="0.1",
    scripts=["asl.py"],
    author="deplanty",
    description="A toolbox to extract data from the ASL5000",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/deplanty/asl5000-utils",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Licence :: OSI Approved :: GNU General Public Licence v3 (GPLv3)",
        "Operating System :: OS Independent"
    ]
)
