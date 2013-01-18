from agoraplex.annotation import annotated, returns, empty
from agoraplex.annotation.tools import document, typespec

# ___TODO:___ use one of the structural comparison packages to
# validate the output (__defaults__, __annotations__) declaratively,
# instead of hardcoding the assertions in each test.

# ___TODO:___ check for non-tuples in default params on an @annotated
# function

class TestAnnotatedDecorater (object):
    def test_without_params_without_annotations (self):
        @annotated
        def nop (): pass

        # ``__defaults__`` should be None
        assert nop.__defaults__ is None

        # ``__annotations__`` should exist, but be empty
        assert len(nop.__annotations__) == 0

    def test_with_params_without_annotations (self):
        @annotated
        def nop (a, b): pass

        # ``__defaults__`` should be None
        assert nop.__defaults__ is None

        # ``__annotations__`` should exist, but be empty
        assert len(nop.__annotations__) == 0

    def test_with_params_without_defaults_empty_annotations (self):
        @annotated
        def nop (a=(empty,), b=(empty,)): pass

        # ``__defaults__`` should be None
        assert nop.__defaults__ is None

        # ``__annotations__`` should exist, but be empty
        assert len(nop.__annotations__) == 0

    def test_with_params_with_defaults_empty_annotations (self):
        @annotated
        def nop (a=(empty,42), b=(empty,'beta')): pass

        # the elements of ``__defaults__`` should match the positional
        # parameters supplied for ``a`` and ``b``.
        assert len(nop.__defaults__) == 2
        assert nop.__defaults__[0] == 42
        assert nop.__defaults__[1] == 'beta'

        # ``__annotations__`` should exist, but be empty
        assert len(nop.__annotations__) == 0

    def test_with_params_without_defaults_with_annotations (self):
        @annotated
        def nop (a=(int,), b=(unicode,)): pass

        # ``a`` and ``b`` should have correct annotations
        assert len(nop.__annotations__) == 2
        assert nop.__annotations__['a'] is int
        assert nop.__annotations__['b'] is unicode

        # ``__defaults__`` should be ``None``
        assert nop.__defaults__ is None

    def test_with_params_with_defaults_with_annotations (self):
        @annotated
        def nop (a=(int, 42), b=(unicode, 'beta')): pass

        # ``a`` and ``b`` should have correct annotations
        assert len(nop.__annotations__) == 2
        assert nop.__annotations__['a'] is int
        assert nop.__annotations__['b'] is unicode

        # ``__defaults__`` should have two members, as above
        assert len(nop.__defaults__) == 2
        assert nop.__defaults__[0] == 42
        assert nop.__defaults__[1] == 'beta'

    def test_return_annotation_without_params_without_annotations (self):
        @annotated(returns=int)
        def nop (): pass

        # ``__defaults__`` should be ``None``
        assert nop.__defaults__ is None

        # there should be only one annotation: ``return``
        assert len(nop.__annotations__) == 1
        assert nop.__annotations__['return'] is int

    def test_return_annotation_with_params_without_annotations (self):
        @annotated(returns=int)
        def nop (a, b): pass

        # ``__defaults__`` should be ``None``
        assert nop.__defaults__ is None

        # there should be only one annotation: ``return``
        assert len(nop.__annotations__) == 1
        assert nop.__annotations__['return'] is int

    def test_return_annotation_with_params_without_defaults_with_empty_annotations (self):
        @annotated(returns=int)
        def nop (a=(empty,), b=(empty,)): pass

        # ``__defaults__`` should be ``None``
        assert nop.__defaults__ is None

        # there should be only one annotation: ``return``
        assert len(nop.__annotations__) == 1
        assert nop.__annotations__['return'] is int

    def test_return_annotation_with_params_with_defaults_with_empty_annotations (self):
        @annotated(returns=int)
        def nop (a=(empty,42), b=(empty,'beta')): pass

        # ``__defaults__`` should have two members, as above
        assert len(nop.__defaults__) == 2
        assert nop.__defaults__[0] == 42
        assert nop.__defaults__[1] == 'beta'

        # there should be only one annotation: ``return``
        assert len(nop.__annotations__) == 1
        assert nop.__annotations__['return'] is int

    def test_return_annotation_with_params_without_defaults_with_annotations (self):
        @annotated(returns=int)
        def nop (a=(int,), b=(unicode,)): pass

        # ``__defaults__`` should be None
        assert nop.__defaults__ is None

        # there should be annotations for ``return``, ``a``, and ``b``
        assert len(nop.__annotations__) == 3
        assert nop.__annotations__['return'] is int
        assert nop.__annotations__['a'] is int
        assert nop.__annotations__['b'] is unicode


class TestReturnsDecorator (object):
    def test_return_annotation_without_params (self):
        @returns(int)
        def nop (): pass

        # there should be only one annotation: ``return``
        assert len(nop.__annotations__) == 1
        assert nop.__annotations__['return'] is int

    def test_return_annotation_with_params (self):
        @returns(int)
        def nop (a, b): pass

        # ``__defaults__`` should be None
        assert nop.__defaults__ is None

        # there should be only one annotation: ``return``
        assert len(nop.__annotations__) == 1
        assert nop.__annotations__['return'] is int

    def test_return_annotation_with_params_with_defaults (self):
        @returns(int)
        def nop (a=42, b='beta'): pass

        # ``__defaults__`` should have two members, as above
        assert len(nop.__defaults__) == 2
        assert nop.__defaults__[0] == 42
        assert nop.__defaults__[1] == 'beta'

        # there should be only one annotation: ``return``
        assert len(nop.__annotations__) == 1
        assert nop.__annotations__['return'] is int

    def test_return_empty_annotation_without_params (self):
        @returns(empty)
        def nop (): pass

        # ``__defaults__`` should be None
        assert nop.__defaults__ is None

        # __annotations__ should exist, but be empty
        assert len(nop.__annotations__) == 0

    def test_return_empty_annotation_with_params (self):
        @returns(empty)
        def nop (a, b): pass

        # ``__defaults__`` should be None
        assert nop.__defaults__ is None

        # ``__annotations__`` should exist, but be empty
        assert len(nop.__annotations__) == 0


class TestDocstringDecorater (object):
    def test_without_params_without_annotations_with_docstring (self):
        @document
        @annotated
        def nop ():
            """This is nop."""
            pass

        assert nop.__doc__ == """nop ()

This is nop."""

    def test_without_params_without_annotations (self):
        @document
        @annotated
        def nop (): pass

        assert nop.__doc__.startswith("""nop ()

""")

    def test_with_params_without_annotations (self):
        @document
        @annotated
        def nop (a, b): pass

        assert nop.__doc__.startswith("""nop (a, b)

""")

    def test_with_params_without_defaults_empty_annotations (self):
        @document
        @annotated
        def nop (a=(empty,), b=(empty,)): pass

        assert nop.__doc__.startswith("""nop (a, b)

""")

    def test_with_params_with_defaults_empty_annotations (self):
        @document
        @annotated
        def nop (a=(empty,42), b=(empty,'beta')): pass

        assert nop.__doc__.startswith("""nop (a=42, b='beta')

""")

    def test_with_params_without_defaults_with_annotations (self):
        @document
        @annotated
        def nop (a=(int,), b=(unicode,)): pass

        assert nop.__doc__.startswith("""nop (a:int, b:unicode)

""")

    def test_with_params_with_defaults_with_annotations (self):
        @document
        @annotated
        def nop (a=(int, 42), b=(unicode, 'beta')): pass

        assert nop.__doc__.startswith("""nop (a:int=42, b:unicode='beta')

""")

    def test_return_annotation_without_params_without_annotations (self):
        @document
        @annotated(returns=int)
        def nop (): pass

        assert nop.__doc__.startswith("""nop () -> int

""")

    def test_return_annotation_with_params_without_annotations (self):
        @document
        @annotated(returns=int)
        def nop (a, b): pass

        assert nop.__doc__.startswith("""nop (a, b) -> int

""")

    def test_return_annotation_with_params_without_defaults_with_empty_annotations (self):
        @document
        @annotated(returns=int)
        def nop (a=(empty,), b=(empty,)): pass

        assert nop.__doc__.startswith("""nop (a, b) -> int

""")

    def test_return_annotation_with_params_with_defaults_with_empty_annotations (self):
        @document
        @annotated(returns=int)
        def nop (a=(empty,42), b=(empty,'beta')): pass

        assert nop.__doc__.startswith("""nop (a=42, b='beta') -> int

""")

    def test_return_annotation_with_params_without_defaults_with_annotations (self):
        @document
        @annotated(returns=int)
        def nop (a=(int,), b=(unicode,)): pass

        assert nop.__doc__.startswith("""nop (a:int, b:unicode) -> int

""")

    def test_with_function_as_return_annotation (self):
        def dummy (): pass

        @document
        @annotated(returns=dummy)
        def nop (): pass

        assert nop.__doc__.startswith("""nop () -> dummy

""")

    def test_with_function_as_annotation (self):
        def dummy (): pass

        @document
        @annotated
        def nop (f=(dummy,)): pass

        assert nop.__doc__.startswith("""nop (f:dummy)

""")

    def test_with_function_as_default (self):
        def dummy (): pass

        @document
        @annotated
        def nop (f=(empty,dummy)): pass

        assert nop.__doc__.startswith("""nop (f=dummy)

""")


class TesttypespecHelper (object):
    def test_cache (self):
        assert typespec(str) == typespec(str)
        assert typespec(str) != typespec(unicode)

    def test_str (self):
        assert repr(typespec(str)) == 'str'

    def test_unicode (self):
        assert repr(typespec(unicode)) == 'unicode'

    def test_callable (self):
        assert repr(typespec(callable)) == 'callable'

    def test_iter (self):
        assert repr(typespec(iter)) == 'iter'

    def test_string (self):
        assert repr(typespec("test")) == "test"

    def test_none (self):
        assert repr(typespec(None)) == "None"
