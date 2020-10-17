#!/usr/bin/env python

# Python
import os
import sys

# Setuptools
from setuptools import Command, setup
import setuptools.command.build_py as orig_build_py


class UnsupportedCommand(Command):

    description = 'This command is not supported'
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        sys.exit('This command is not supported!')


class BuildPyCommand(orig_build_py.build_py):

    def run(self):
        orig_build_py.build_py.run(self)
        self.copy_file('autodotenv.pth', os.path.join(self.build_lib, 'autodotenv.pth'), preserve_mode=False)


setup(
    options={
        'install': {  # Messes with other installs if set in setup.cfg.
            'single_version_externally_managed': '1',
            'root': '/',
        },
    },
    cmdclass={
        'build_py': BuildPyCommand,
        'unsupported': UnsupportedCommand,
    },
)
