from setuptools import setup, find_packages

setup(
  name="FastTools",
  version="1.0.0",
  author='CoolGamers',
  packages=find_packages(),
  install_requires=[
    'rich',
    'pytube'
  ],
  include_package_data=True,
  package_data={'': []}
)