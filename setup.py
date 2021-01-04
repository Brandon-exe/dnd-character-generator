#!/usr/bin/env python3

from setuptools import setup
from pathlib import Path

# Get the current directory.  __file__ is the current running file's path, but
# is often a relative directory, so we use absolute() to get the full path and
# its parent, which is the directory itself.
this_dir = Path(__file__).absolute().parent

# Use the Path's overloaded __div__ method to build a child path.  This is done
# because path separators are different on different OSes.  Hardcoded paths can
# be frustrating to keep portable if you don't use a proper Path abstraction.
readme_path = this_dir / 'README.md'

# Here we actually read the entire readme into a string.
with readme_path.open() as file:
    long_description = file.read()

setup(
    name='charactergenerator',
    version='0.0.1',
    author='Brandon Phillips',
    description='A simple Dungeons and Dragons character generator',
    long_description=long_description,
    long_description_content_type='text/markdown',
    license='MIT',
    keywords=['dnd', 'dungeons', 'dragons', 'rpg', 'game', 'utility'],
    url='https://gitlab.com/Brandon.exe/dnd-character-generator',
    entry_points=dict(
        console_scripts=[
            'charactergenerator = charactergenerator.__main__:main',
        ]
    ),
    packages=[
        'charactergenerator',
    ],
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: MIT License',
        'License :: OSI Approved :: MIT License',
        'Topic :: Utilities',
        'Topic :: Games/Entertainment',
        'Topic :: Games/Entertainment :: Role-Playing',
    ],
)
