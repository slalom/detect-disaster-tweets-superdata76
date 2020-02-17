import subprocess

def test_default_CLI_options():
    rc = subprocess.check_call(['./main.py'])
    assert 0 == rc

def test_help_option():
    result = subprocess.check_output(['./main.py', '-h'])
    assert 'usage: main.py' in str(result)
