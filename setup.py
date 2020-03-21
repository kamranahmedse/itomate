import setuptools

with open("readme.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="itomate",
    version="0.0.1",
    author="Kamran Ahmed",
    author_email="kamranahmed.se@gmail.com",
    description="Automate your iTerm layouts and workflows",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/kamranahmedse/itomate",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: MacOS",
    ],
    python_requires='>=3.0',
)
