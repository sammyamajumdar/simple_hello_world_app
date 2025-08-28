from main import main, add_two_numbers

def test_main():
    assert main() == "hello world"

def test_add_two_numbers(): 
    assert add_two_numbers(6,10) == 16
