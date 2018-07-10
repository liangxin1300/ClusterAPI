
def get_cib_data(scope=None):
    def inner(fn):
        g = fn.__globals__
        g['cib_data'] = "cib data from testing"
        return fn
    return inner
