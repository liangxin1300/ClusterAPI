import subprocess
import json
import xmltodict
import functools
import os

from flask_restful import abort


def xml_to_json(xml_data):
    return json.dumps(xmltodict.parse(xml_data))


def json_find(j_data, path):
    kv = json.loads(j_data)
    paths = path.split("/")
    for key in paths:
        kv = kv[key]
    return kv


def to_ascii(s):
    '''
    Convert the bytes string to a ASCII string
    Usefull to remove accent (diacritics)
   
    From crmsh.utils
    '''
    if s is None:
        return s
    if isinstance(s, str):
        return s
    try:
        return str(s, 'utf-8')
    except UnicodeDecodeError:
        import traceback
        traceback.print_exc()
        return s


def get_stdout_stderr(cmd, input_s=None, shell=True):
    '''
    Run a cmd, return (rc, stdout, stderr)

    From crmsh.utils
    '''
    proc = subprocess.Popen(cmd,
                            shell=shell,
                            stdin=input_s and subprocess.PIPE or None,
                            stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE)
    stdout_data, stderr_data = proc.communicate(input_s)
    return proc.returncode, to_ascii(stdout_data), to_ascii(stderr_data)


def get_cib_data_raw(scope=None):
    get_cib_cmd = "/usr/sbin/cibadmin -Q -l"
    if scope:
        get_cib_cmd += " -o %s" % scope
    ret, out, err = get_stdout_stderr(get_cib_cmd)
    return out


def get_cib_data(scope=None):
    def decorator(func):
        def inner(*args, **kwargs):
            g['cib_data'] = xml_to_json(get_cib_data_raw(scope))
            return func(*args, **kwargs)

        g = func.__globals__
        return inner
    return decorator


def check_login(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        root = '/'.join(os.path.dirname(__file__).split('/')[:-1])
        if not os.path.exists("root/api_token_entries.store"):
            abort(401)
        return func(*args, **kwargs)
    return wrapper
