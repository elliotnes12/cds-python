from _version import __version__
from setuptools import setup, find_packages

setup(
        name='cds-config-services',
        version=__version__,
        author='NSO AntMan Team',
        author_email=None,
        url=None,
        description='NSO Cds Config Service',
        long_description='NSO Cds Config Service',
        license='(c) Nielsen 2019',
        python_requires='>=3.6',
        packages=find_packages()
)