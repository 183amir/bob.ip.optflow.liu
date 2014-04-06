#!/usr/bin/env python
# vim: set fileencoding=utf-8 :
# Andre Anjos <andre.anjos@idiap.ch>
# Thu 20 Sep 2012 14:43:19 CEST

"""Bindings for Liu's optical flow
"""

from setuptools import setup, find_packages, dist
dist.Distribution(dict(setup_requires=['xbob.blitz']))
from xbob.blitz.extension import Extension

version = '1.2.0a0'

setup(

    name="xbob.ip.optflow.liu",
    version=version,
    description="Python bindings to the optical flow framework by C. Liu",
    license="GPLv3",
    author='Andre Anjos',
    author_email='andre.anjos@idiap.ch',
    long_description=open('README.rst').read(),
    url='https://github.com/bioidiap/xbob.ip.optflow.liu',

    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,

    namespace_packages=[
      "xbob",
      "xbob.ip",
      "xbob.ip.optflow",
      ],

    install_requires=[
      'setuptools',
      'xbob.blitz',
      'xbob.io',
      'xbob.ip.color',
    ],

    entry_points = {
      'console_scripts': [
        'xbob_of_liu.py = xbob.ip.optflow.liu.script.flow:main',
        ],
      },

    ext_modules = [
      Extension("xbob.ip.optflow.liu.version",
        [
          "xbob/ip/optflow/liu/version.cpp",
          ],
        version = version,
        ),
      Extension("xbob.ip.optflow.liu.sor",
        [
          "xbob/ip/optflow/liu/sor_based/OpticalFlow.cpp",
          "xbob/ip/optflow/liu/sor_based/GaussianPyramid.cpp",
          "xbob/ip/optflow/liu/sor_based/Stochastic.cpp",
          "xbob/ip/optflow/liu/sor_based/main.cpp",
          ],
        version = version,
        ),
      Extension("xbob.ip.optflow.liu.cg",
        [
          "xbob/ip/optflow/liu/cg_based/OpticalFlow.cpp",
          "xbob/ip/optflow/liu/cg_based/GaussianPyramid.cpp",
          "xbob/ip/optflow/liu/cg_based/main.cpp",
          ],
        version = version,
        ),
      ],

    classifiers = [
      'Development Status :: 4 - Beta',
      'Intended Audience :: Developers',
      'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
      'Natural Language :: English',
      'Programming Language :: Python',
      'Programming Language :: Python :: 3',
      'Topic :: Scientific/Engineering :: Artificial Intelligence',
      'Topic :: Scientific/Engineering :: Image Recognition',
      ],

    )
