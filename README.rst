|Build Status| |PyPI Version| |Python Versions|

AutoDotEnv
==========

AutoDotEnv is a simple tool to automatically set environment variables from a
``.env`` file when running any Python command.

Usage
-----

1. ``pip install AutoDotEnv``
2. Install your Python-based tools of choice that can be configured via environment variables (e.g. ``awscli``, ``ansible``).
3. Create a ``.env`` file in the current directory values set to configure the installed tools.
4. Run your installed tools and environment variables will be set automatically from the ``.env`` file.

Roadmap
-------

* Configure AutoDotEnv options via environment variables.
* Configure AutoDotEnv options via a config file.
* Load variables from file patterns other than ``.env``.
* Load variables only for certain Python scripts/tools.


.. |Build Status| image:: http://img.shields.io/travis/cchurch/autodotenv.svg
   :target: https://travis-ci.org/cchurch/autodotenv
.. |PyPI Version| image:: https://img.shields.io/pypi/v/autodotenv.svg
   :target: https://pypi.python.org/pypi/autodotenv
.. |Python Versions| image:: https://img.shields.io/pypi/pyversions/autodotenv.svg
   :target: https://pypi.python.org/pypi/autodotenv
