import setuptools

with open("readme.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="itomate",
    version="0.2.8",
    author="Kamran Ahmed",
    author_email="kamranahmed.se@gmail.com",
    description="Automate your iTerm layouts and workflows",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/kamranahmedse/itomate",
    packages=setuptools.find_packages(),
    install_requires=[
        "iterm2>=1.1",
        "PyYAML>=5.3.1",

    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: MacOS",
    ],
    python_requires='>=3.7.0',
    license="MIT",
    entry_points="""
        [console_scripts]
        itomate=itomate:main
    """
)
