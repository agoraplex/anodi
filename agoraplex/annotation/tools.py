from backports import inspect
from agoraplex.annotation import annotated, empty

_typespecs = {}

class TypeSpec (object):
    def __init__ (self, typeobj):
        self.typeobj = typeobj
        if hasattr(self.typeobj, '__name__'):
            self.repr = self.typeobj.__name__
        else:
            if isinstance(self.typeobj, basestring):
                self.repr = self.typeobj
            else:
                self.repr = repr(self.typeobj)

    def __repr__ (self):
        return self.repr

def typespec (t):
    if not t in _typespecs:
        _typespecs[t] = TypeSpec(t)
    return _typespecs[t]

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
