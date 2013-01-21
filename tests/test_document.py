from agoraplex.annotation import annotated, returns, empty
from agoraplex.annotation.tools import document, typename

class TestDocumentationDecorator (object):
    def test_without_params_without_annotations_with_docstring (self):
        @document
        @annotated
        def nop ():
            """This is nop."""
            pass

        assert nop.__doc__ == """nop ()

This is nop."""

    def test_without_params_without_annotations_with_indented_docstring (self):
        @document
        @annotated
        def nop ():
            """
            This is nop.
            """
            pass

        print(repr(nop.__doc__))
        assert nop.__doc__ == """            nop ()


            This is nop.
            """

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


class TesttypenameHelper (object):
    def test_cache (self):
        assert typename(str) == typename(str)
        assert typename(str) != typename(unicode)

    def test_str (self):
        assert repr(typename(str)) == 'str'

    def test_unicode (self):
        assert repr(typename(unicode)) == 'unicode'

    def test_callable (self):
        assert repr(typename(callable)) == 'callable'

    def test_iter (self):
        assert repr(typename(iter)) == 'iter'

    def test_string (self):
        assert repr(typename("test")) == "test"

    def test_none (self):
        assert repr(typename(None)) == "None"
