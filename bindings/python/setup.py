#!/usr/bin/env python
 
from setuptools import setup
from setuptools.extension import Extension
import os, sys, platform
from distutils.command.build_ext import build_ext
from setuptools import Command

def get_libdir():
    if not platform.architecture()[0].startswith("64"):
        return "lib"
    dist = platform.dist()[0].lower()
    distdict = dict(suse="lib64", redhat="lib64")
    return distdict.get(dist, "lib")

ARCHLIBDIR = get_libdir()

class libpsf_build_ext(build_ext):
    """
    """
    user_options = build_ext.user_options + \
            [("boost=", None, "Prefix for boost_python installation location"),
	     ("libpsf=", None, "Prefix for libpsf installation location"),
	     ]

    def initialize_options(self):
        """
	Overload to enable custom settings to be picked up
	"""
        build_ext.initialize_options(self)
	self.boost = "/usr"
        self.libpsf = os.path.dirname(__file__)

    def finalize_options(self):
        """
	Overloaded build_ext implementation to append custom library
        include file and library linking options
	"""
        build_ext.finalize_options(self)

	boostlibdir = os.path.join(self.boost, ARCHLIBDIR)
	boostincdir = os.path.join(self.boost, "include")

        libpsflibdir = os.path.join(self.libpsf, "lib")
        libpsfincdir = os.path.join(self.libpsf, "include")

        for dirname in [boostlibdir, libpsflibdir]: 
            if dirname not in self.library_dirs:
                self.library_dirs += [dirname]

        for dirname in [boostincdir, libpsfincdir]: 
            if dirname not in self.include_dirs:
                self.include_dirs += [dirname]


libpsf_ext = Extension(name = "libpsf", 
                       sources = ["psfpython.cc"],
                       libraries = ["boost_python", "psf"])

import numpy
libpsf_ext.include_dirs.append(numpy.get_include())

setup(
    name="libpsf",
    ext_modules=[libpsf_ext],
    package_dir = {"" : "."},
    packages=["tests"],
    #tests_require=["mock"],
    test_suite="tests",
    cmdclass={"build_ext": libpsf_build_ext}
    )
