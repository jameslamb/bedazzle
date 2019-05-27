# borrowed liberally from https://github.com/uber/h3-py/blob/master/setup.py
import os
import subprocess
from setuptools import setup, find_packages
from setuptools.command.build_ext import build_ext
from setuptools.dist import Distribution
from setuptools.extension import Extension


def install_bedazzle_c():
    os.chdir("../")
    subprocess.call(['bazel', 'build', '//src/lib:libadd_one.so'])
    os.chdir("py-pkg")
    subprocess.call(['rm', '-rf', 'bedazzle/data'])
    subprocess.call(['mkdir', '-p', 'bedazzle/data'])
    subprocess.call(['cp', '../bazel-bin/src/lib/libadd_one.so', 'bedazzle/data/.'])


class CustomBuildExtCommand(build_ext):
    """Overload build_ext command class run method"""
    def run(self):
        install_bedazzle_c()


class BinaryDistribution(Distribution):
    def __init__(self, attrs=None):
        Distribution.__init__(self, attrs)
        # The values used for the name and sources in the Extension below are
        # not important, because we override the build_ext command above.
        # The normal C extension building logic is never invoked, and is
        # replaced with our own custom logic. However, ext_modules cannot be
        # empty, because this signals to other parts of distutils that our
        # package contains C extensions and thus needs to be built for
        # different platforms separately.
        self.ext_modules = [Extension('bedazzle', [])]


setup(
    name="bedazzle",
    version="0.0.1",
    description="literally the best thing ever written dont @ me",
    packages=['bedazzle'],  # find_packages(exclude=['tests', 'tests.*']),
    install_requires=[],
    cmdclass={
        'build_ext': CustomBuildExtCommand,
    },
    package_data={'bedazzle': ['data/*.so']},
    license='hands off internal only you fools',
    distclass=BinaryDistribution
)
