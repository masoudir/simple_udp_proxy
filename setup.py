import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="simple_udp_proxy", # Replace with your own username
    version="0.0.4",
    author="Masoud Iranmehr",
    author_email="masoud.iranmehr@gmail.com",
    description="This package creates a bidirectional bridge between new udp connections to a unique udp port by creating a proxy for each new connection.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/masoudir/simple_udp_proxy",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
