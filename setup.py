import setuptools
from setuptools import version

setuptools.setup(
  name='crazy_joe',
  version="0.1.0",
  description='',
  packages=setuptools.find_packages('src'),
  package_dir={'': 'src'},
)