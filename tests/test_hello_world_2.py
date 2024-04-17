import sys
import io
from src import hello_world_2

 
def test_hello_world_2():
    """Tests the hello_world function."""
    captured_output = io.StringIO()
    sys.stdout = captured_output
    hello_world_2.hello_world_2()
    sys.stdout = sys.__stdout__
    assert captured_output.getvalue() == "Hello, world!\n"