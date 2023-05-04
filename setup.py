from setuptools import setup, find_packages
import os
import mathematique

setup(
    name="pkg_test_mathematique_testpi",
    version=mathematique.__version__,
    classifiers=["Topic :: Education", "Topic :: Documentation"],
    packages=["mathematique"],
    description="demonstration de creation d'un package Python",
    long_description=open(os.path.join(os.path.dirname(__file__), "README.txt")).read(),
    license="GPL V3",
    platforms="ALL",
)
