from setuptools import setup, find_packages

with open('README.md','r') as f:
	long_description = f.read()

setup(
    name='pgbackup',
    version='0.1.0',
    author='Jose Neto',
    author_email='jose.neto@gmx.com',
    description='A utility for backing up PostgreSQL databases',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/jos3neto/pgbackup',
    packages=find_packages('src')
)
    	