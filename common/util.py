import subprocess
import json
import xmltodict


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
    def inner(fn):
        g = fn.__globals__
        g['cib_data'] = xml_to_json(get_cib_data_raw(scope))
        return fn
    return inner
