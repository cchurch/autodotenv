#!/usr/bin/env python

# Python
import os
import sys

# Setuptools
from setuptools import Command, setup
import setuptools.command.build_py as orig_build_py


class BaseTwineCommand(Command):

    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        self.run_command('sdist')
        self.get_finalized_command('sdist')
        self.run_command('bdist_wheel')
        self.get_finalized_command('bdist_wheel')
        dist_files = [df[2] for df in self.distribution.dist_files]
        self.spawn(['twine', self.twine_subcommand] + dist_files)

    sub_commands = [
        ('sdist', lambda self: True),
        ('bdist_wheel', lambda self: True),
    ]


class TwineCheckCommand(BaseTwineCommand):

    description = 'Check distribution files with twine'
    twine_subcommand = 'check'


class TwineUploadCommand(BaseTwineCommand):

    description = 'Upload distribution files with twine'
    twine_subcommand = 'upload'


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
        'twine_check': TwineCheckCommand,
        'twine_upload': TwineUploadCommand,
        'unsupported': UnsupportedCommand,
    },
)
