import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="PyInterrail",
    version="0.0.1",
    author="Daniel Turner Cebriá",
    author_email="daniel.turner.cebria@gmail.com",
    description="Python interface for Interrail API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/untalturner/PyInterrail",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache-2.0 License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)