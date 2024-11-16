from setuptools import find_packages, setup

setup(
    name='FinBot',
    version='0.0.1',
    author='Rama',
    author_email='rama3017krishna@gmail.com',
    packages=find_packages(),
    install_requires=['langchain','langchain-openai','langchain-astradb','datasets','pypdf','flask','python-dotenv']

)