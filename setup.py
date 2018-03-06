from setuptools import setup, find_packages

with open('README.rst', encoding='UTF-8') as f:
    readme = f.read()


setup(
    name="pgbackup",
    version="0.1.0",
    description="Database backs up locally or on AWS",
    long_description=readme,
    author='Swapnasheel',
    author_email='swar.1318@gmail.com',
    install_requires=[],
    packages=find_packages('src'),
    package_dir={'':'src'}
)

