import subprocess
import json
import xmltodict
import functools
import os

import pam
import jwt

from flask import request
from flask_restful import abort


TOKEN_KEY = 'ClusterAPI'


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
        if func.__name__ == "register":
            return func(*args, **kwargs)
        root = '/'.join(os.path.dirname(__file__).split('/')[:-1])
        token_path = "%s/api_token_entries.store" % root
        if not os.path.exists(token_path):
            abort(401)
        with open(token_path, 'r') as f:
            data = json.loads(f.read())
            token_orig = data["token"]
        token_from_request = request.headers.get("Authenticate")
        if token_from_request and \
           token_from_request.startswith("Token "):
            token_from_request = token_from_request[6:]
            if token_from_request != token_orig:
                abort(401)
        else:
            abort(401)
        return func(*args, **kwargs)
    return wrapper


def check_pam(username, password):
    p = pam.pam()
    return p.authenticate(username, password)


def create_token(username):
    token = jwt.encode({'username': username, 'expiration': 'one year'}, TOKEN_KEY)
    return to_ascii(token)
