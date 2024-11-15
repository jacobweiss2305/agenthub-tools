# packages/duckduckgo/setup.py
from setuptools import setup, find_namespace_packages

setup(
    packages=find_namespace_packages(
        where="../../",
        include=["aihive_tools.*"]
    ),
    package_dir={"": "../../"},
    namespace_packages=["aihive_tools"],
)