import setuptools
from setuptools import setup

setup(name='sam-tool',
      version='0.1',
      description='Sam Client Helper',
      url='http://github.com/reiktar/sam-tool',
      author='Markus Jonsson',
      author_email='reiktar@gmail.com',
      license='MIT',
      packages= setuptools.find_packages(),
#      packages=['sam_tool'],
      scripts=['bin/sam-tool'],
      install_requires=['watchdog'],
      zip_safe=False)
