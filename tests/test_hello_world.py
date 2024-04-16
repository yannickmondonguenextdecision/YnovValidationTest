import sys
import io
from src import hello_world

 
def test_hello_world():
    """Tests the hello_world function."""
    captured_output = io.StringIO()
    sys.stdout = captured_output
    hello_world.hello_world()
    sys.stdout = sys.__stdout__
    assert captured_output.getvalue() == "Hello, world!\n"