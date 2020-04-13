import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name = "CanvasPlus",
    version = "1.2.1",
    author = "Luke Zhang",
    author_email = "luke.zhang2004@gmail.com",
    description = "Improved Canvas widget for tkinter with more functionality to display graphical elements like lines or text. ",
    long_description = long_description,
    long_description_content_type = "text/markdown",
    url = "https://github.com/Luke-zhang-04/CanvasPlus",
    packages = setuptools.find_packages(),
    install_requires = [],
    classifiers = [
        'Development Status :: 5 - Production/Stable', # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Tcl",
        "Topic :: Multimedia :: Graphics",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires = '>=3.5',
)