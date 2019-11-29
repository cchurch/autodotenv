# Python
import json
import os
import subprocess
import sys
import unittest

# Python-DotEnv
from dotenv import find_dotenv, set_key, unset_key


class TestAutoDotEnv(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        subprocess.check_call(['pip', 'install', '.'])

    def setUp(self):
        if not os.path.exists(os.path.join(os.getcwd(), '.env')):
            with open(os.path.join(os.getcwd(), '.env'), 'w+'):
                pass
        self.dotenv_file = find_dotenv(usecwd=True)
        self.env_var = 'AUTODOTENV_TEST'

    def get_env_var_from_subprocess(self, var=None):
        var = var or self.env_var
        new_env = dict(os.environ.items())
        new_env.pop(var, None)
        result = subprocess.check_output([
            sys.executable,
            '-c',
            "import json, os; print(json.dumps(os.environ.get('{}')))".format(var),
        ], env=new_env)
        return json.loads(result.decode().strip())

    def test_imported(self):
        result = subprocess.check_output([
            sys.executable,
            '-c',
            "import sys; print(sys.modules.get('autodotenv'))",
        ])
        self.assertNotEqual(result.decode().strip(), 'None')

    def test_unset_var(self):
        unset_key(self.dotenv_file, self.env_var)
        result = self.get_env_var_from_subprocess()
        self.assertEqual(result, None)

    def test_set_var(self):
        set_key(self.dotenv_file, self.env_var, '{}'.format(os.getpid()))
        result = self.get_env_var_from_subprocess()
        self.assertEqual(result, '{}'.format(os.getpid()))

    def test_no_dot_env(self):
        if os.path.exists(self.dotenv_file):
            os.remove(self.dotenv_file)
        result = self.get_env_var_from_subprocess()
        self.assertEqual(result, None)


suite = unittest.TestLoader().loadTestsFromTestCase(TestAutoDotEnv)
