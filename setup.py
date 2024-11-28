from setuptools import setup, find_packages
import os

classifiers = [
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Developers',
    'Operating System :: OS Independent',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
    'Programming Language :: Python :: 3.10',
    'Programming Language :: Python :: 3.11',
]

# Get the long description from the README and CHANGELOG files
here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

with open(os.path.join(here, 'CHANGELOG.txt'), encoding='utf-8') as f:
    changelog = f.read()

setup(
    name='vokal',  # Library name
    version='1.0.2',  # Initial release version
    description='A Python library for separating vocals and instruments from audio using Demucs.',
    long_description=long_description + '\n\n' + changelog,
    long_description_content_type='text/markdown',
    url='https://github.com/Meet2147/vokal',  # Replace with your actual GitHub repo URL
    author='Meet Jethwa',
    author_email='meetjethwa3@gmail.com',
    license='MIT',
    classifiers=classifiers,
    keywords='vocal separation, music processing, audio tools',
    packages=find_packages(),
    install_requires=[
        # Add dependencies here if any
    ],
    include_package_data=True,
    package_data={
        "demucs"
        # Specify additional package data here if necessary
    },
)