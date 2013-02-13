from distribute_setup import use_setuptools
use_setuptools()

from setuptools import setup


setup(
    name='agoraplex.annotation',
    version='0.0.0',
    author='Tripp Lilley',
    author_email='tripplilley@gmail.com',
    packages=['agoraplex.annotation'],
    namespace_packages=['agoraplex'],
    url='',
    license='BSD',
    description='',
    long_description=open('README.rst').read(),
    tests_require=['nose'],
)
