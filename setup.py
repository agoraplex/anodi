from setuptools import setup

requirements = {
    'install': [
        'distribute',
        ],
    'extras': {
        'docs': [
            'sphinx>=1.1',
            'agoraplex.themes.sphinx>=0.1.3',
            ],
        'tests': [
            'nose>=1.2.1',
            'coverage>=3.6',
            'pinocchio>=0.3.1',
            'xtraceback>=0.3.3',
            ],
        },
    }


# write requirements for Travis and ReadTheDocs to use...
with open("reqs/travis.txt", "w") as travis:
    travis.write('\n'.join(requirements['extras']['tests']) + '\n')

with open("reqs/rtfd.txt", "w") as rtfd:
    rtfd.write('\n'.join(requirements['extras']['docs']) + '\n')

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
    install_requires=requirements.get('install', None),
    tests_require=requirements.get('extras', {}).get('tests', None),
    extras_require=requirements.get('extras', None),
)
