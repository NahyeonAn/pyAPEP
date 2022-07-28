from __future__ import absolute_import
from setuptools import setup

setup(
    name='pyapep',
    version='1.0',
    description='Python package for PSA simulation',
    url='https://github.com/NahyeonAn/rtd-test',
    # download_url='https://github.com/CorySimon/pyIAST/tarball/master',
    install_requires=['numpy', 'scipy', 'pandas>=0.24.0', 'matplotlib','time'],
    extras_require={'pre-commit': [
        "pre-commit==1.14.4",
        "yapf==0.26.0",
    ]},
    keywords='adsorption simulation',
    author='Nahyeon An',
    author_email='anna@kitech.re.kr',
    license='KITECH',
    packages=['pyapep'],
    zip_safe=False)