#!/usr/bin/python3
"""
doing with request
"""

from urllib import request, error
import sys
import importlib.util
import io
from pathlib import Path
import pytest

SCRIPT_PATH = Path(__file__).parent.resolve() / "3-error_code.py"

def _load_module_and_capture(urlopen_impl, argv):
    """
    Load the target script as a fresh module while:
    - setting sys.argv to argv
    - patching urllib.request.urlopen to urlopen_impl
    - capturing stdout
    Returns the captured stdout string.
    """
    # Backup originals
    orig_argv = sys.argv[:]
    orig_urlopen = request.urlopen

    # Unique module name to force fresh execution
    module_name = f"three_error_code_test_{id(argv)}"

    # Prepare capture
    captured = io.StringIO()
    try:
        # Patch argv and urlopen
        sys.argv = list(argv)
        request.urlopen = urlopen_impl

        # Load module from file path
        spec = importlib.util.spec_from_file_location(module_name, str(SCRIPT_PATH))
        module = importlib.util.module_from_spec(spec)

        # Capture stdout while executing module
        orig_stdout = sys.stdout
        sys.stdout = captured
        try:
            spec.loader.exec_module(module)
        finally:
            sys.stdout = orig_stdout

    finally:
        # Restore
        sys.argv = orig_argv
        request.urlopen = orig_urlopen
        # Remove module from sys.modules if present
        if module_name in sys.modules:
            del sys.modules[module_name]

    return captured.getvalue()

class FakeResponse:
    def __init__(self, data_bytes):
        self._data = data_bytes

    def read(self):
        return self._data

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc, tb):
        return False

def test_module_documentation():
    """Module is documented"""
    source = SCRIPT_PATH.read_text(encoding="utf-8")
    node = ast.parse(source)
    doc = ast.get_docstring(node)
    assert doc and doc.strip(), "Module should have a non-empty docstring"

def test_status_200_prints_body():
    """Correct output - case: request http://0.0.0.0:5050 with status code 200"""
    def urlopen_ok(url):
        return FakeResponse(b"Hello from test server")
    out = _load_module_and_capture(urlopen_ok, [str(SCRIPT_PATH), "http://0.0.0.0:5050"])
    assert "Hello from test server" in out

@pytest.mark.parametrize("code", [401, 500])
def test_error_codes_print_error(code):
    """Correct output - case: request http://0.0.0.0:5050 with status code {code}"""
    def urlopen_raise(url):
        raise error.HTTPError(url, code, "mocked error", hdrs=None, fp=None)
    out = _load_module_and_capture(urlopen_raise, [str(SCRIPT_PATH), "http://0.0.0.0:5050"])
    assert f"Error code: {code}" in out
