#!/usr/bin/env python

# Python
import os
import sys
from distutils import sysconfig

# Setuptools
from setuptools import Command, setup

relative_site_packages = os.path.relpath(
    sysconfig.get_python_lib(), sys.prefix,
)


class BaseTwineCommand(Command):
    '''Run twine on distribution files.'''

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
    '''Check distribution files with twine.'''

    twine_subcommand = 'check'


class TwineUploadCommand(BaseTwineCommand):
    '''Upload distribution files with twine.'''

    twine_subcommand = 'upload'


setup(
    data_files=[(relative_site_packages, ['autodotenv.pth'])],
    options={
        'install': {  # Messes with other installs if set in setup.cfg.
            'single_version_externally_managed': '1',
            'root': '/',
        },
    },
    cmdclass={
        'twine_check': TwineCheckCommand,
        'twine_upload': TwineUploadCommand,
        #'upload'
    },
)
