from backports import inspect
from agoraplex.annotation import annotated, empty

def document (func):
    # the backported ``inspect.signature`` does the "right thing"
    # with our annotations
    sig = inspect.signature(func)
    sigstr = "%s %s" % (func.__name__, sig)

    # insert the function signature into the docstring
    if func.__doc__ is None:
        func.__doc__ = ""
    func.__doc__ = sigstr + "\n\n" + func.__doc__

    return func
