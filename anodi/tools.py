from backports import inspect
from anodi import annotated, empty
import re

_typenames = {}

class TypeName (object):
    """
    Expose a `__repr__` around `typeobj` to return a (best-effort)
    "meaningful" name (e.g., for writing function signatures).
    """
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

def typename (t):
    """
    Caching wrapper around :class:`TypeName`.
    """
    if not t in _typenames:
        _typenames[t] = TypeName(t)
    return _typenames[t]

_re_function_repr = re.compile(r"""
<[^\>]*
function \s+
(?P<name>[^\s\>]+)
[^\>]* \>""", re.UNICODE | re.VERBOSE)

_re_leading_ws = re.compile(r"^ (?P<indent> [ \t]+) [^\s]+",
                            re.UNICODE | re.VERBOSE | re.MULTILINE)

def document (func):
    """
    Decorator to insert an annotated function signature into the
    docstring.
    """

    # the backported ``inspect.signature`` does the "right thing"
    # with our annotations
    sig = inspect.signature(func)
    sigstr = "%s %s" % (func.__name__, sig)

    # but its stringification does the wrong thing with defaults when
    # they're functions... (at least, according to me.)
    sigstr = _re_function_repr.sub(r"\g<name>", sigstr)


    if func.__doc__ is None:
        func.__doc__ = ""
    else:
        # look at the first non-empty line to determine whether or not
        # the docstring has leading space (i.e., indentation). We want
        # to preserve that in the signature line.

        m = _re_leading_ws.search(func.__doc__)
        if m:
            sigstr = m.group('indent') + sigstr

    # insert the function signature into the docstring
    func.__doc__ = sigstr + "\n\n" + func.__doc__

    return func
