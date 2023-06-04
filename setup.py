from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='anybattle',
    version='0.0.1',
    packages=find_packages(),
    install_requires=[
        'guidance',
        'rich',
    ],
    entry_points={
        'console_scripts': [
            "letsfight = anybattle.CLI.main:cli"
        ],
    },
    author='GandalfsDad',
    author_email='Rhian.McClelland@Outlook.com',
    description='A GPT based battle simulator',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/GandalfsDad/anybattle',
)