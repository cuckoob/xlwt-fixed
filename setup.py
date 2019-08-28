import os

from setuptools import find_packages, setup

DESCRIPTION = (
    'fix bitmap base on xlwt 1.3.0'
)

KEYWORDS = (
    'xls excel spreadsheet workbook worksheet pyExcelerator'
)

setup(
    name='xlwt-fixed',
    version='1.0.0',
    maintainer='Murray',
    maintainer_email='1063967330@qq.com',
    url='https://github.com/murray88/xlwt-fixed/',
    download_url='https://github.com/murray88/xlwt-fixed/',
    description=DESCRIPTION,
    long_description=open(os.path.join(
        os.path.dirname(__file__), 'README.md')
    ).read(),
    long_description_content_type="text/markdown",
    license='BSD',
    platforms='Platform Independent',
    keywords=KEYWORDS,
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    python_requires=">=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*",
    install_requires=[
        'six'
    ],
)
