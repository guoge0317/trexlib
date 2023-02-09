import setuptools

VERSION = "0.0.1"

setuptools.setup(
    name="trexlib",
    version=VERSION,
    description="Python API libs for TRex STL Client ver 4.8",
    author="cisco trex team",
    author_email="trex.tgen@gmail.com",
    url="https://trex-tgn.cisco.com/trex/doc",
    license="TRex 2.87",
    packages=setuptools.find_packages(".\\"),
    keywords=["trex", "api", "traffic-generator", "test-automation"],
    install_requires=[
          "pyzmq>=25.0.0",
          "simpy>=4.0.1",
          "texttable>=1.6.7",
          "PyYAML>=6.0",
          "scapy>=2.4.5",
    ],
    python_requires=">=3.9",
)
