from distutils.core import setup

setup(
    name='qlang',
    version='0.2.0',
    author='James K. Pringle',
    author_email='jpringle@jhu.edu',
    url='http://www.pma2020.org',
    packages=[
        'qlang',
    ],
    license='LICENSE.txt',
    description='Generate files for quick translation to and from XLSForm',
    long_description=open('README.rst').read(),
    install_requires=[
        'XlsxWriter>=0.7.0',
        'xlrd==1.2.0'
    ],
)
