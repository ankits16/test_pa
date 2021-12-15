import setuptools
from setuptools import setup, find_packages
# with open("README.md", "r", encoding="utf-8") as fh:
#     long_description = fh.read()

setup(
    name='ai_ankit_processing',
    package_dir={'': 'src'},
    packages=find_packages(where='src'),
    python_requires='>=3.5, <4',
    install_requires=[
    ],


)
