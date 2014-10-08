from setuptools import setup, find_packages
import os
import sys

SRC_FOLDER = "src"

ENTRY_POINTS = { "console_scripts":[ "ntlm_example_simple=ntlm_examples.simple:main",
                                     "ntlm_example_extended=ntlm_examples.extended:main",] }

setup(name='python-ntlm',
      version='1.1.0',
      description='Python library that provides NTLM support, including an authentication handler for urllib2. Works with pass-the-hash in additon to password authentication.',
      long_description="""
      This package allows Python clients running on any operating
      system to provide NTLM authentication to a supporting server.
      
      python-ntlm is probably most useful on platforms that are not
      Windows, since on Windows it is possible to take advantage of
      platform-specific NTLM support.

      This is also useful for passing hashes to servers requiring
      ntlm authentication in instances where using windows tools is 
      not desirable.""",
      author='Matthijs Mullender',
      author_email='info@zopyx.org',
      maintainer='Joshua Fialkoff',
      maintainer_email='joshua.fialkoff@gmail.comm',
      url="https://github.com/jfialkoff/python-ntlm/",
      packages=["ntlm",],
      zip_safe=False,
      entry_points = ENTRY_POINTS,
      )
