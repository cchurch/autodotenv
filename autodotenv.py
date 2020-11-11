__version__ = '0.1.3'

import warnings

try:
    from dotenv import load_dotenv, find_dotenv
    load_dotenv(find_dotenv(usecwd=True))
except ImportError as exc:
    warnings.warn('autodotenv failed to load python-dotenv: {}'.format(exc))
except Exception as exc:
    warnings.warn('autodotenv failed to read env: {}'.format(exc))
