import calculator

def test_add():
    assert calculator.calculate(2, 3, "add") == 5

def test_divide():
    assert calculator.calculate(2, 2, "divide") == 1

def test_divide_zero():
    assert calculator.calculate(2,0, "divide") == "Cannot divide by zero"

def test_add_float():
    assert calculator.calculate(2,1.5, "add") == 3.5

   # Add more functional tests for subtract, multiply, and divide

def test_terminal_output(capsys):
    store_ans = calculator.calculate(10, 2, "multiply")
    print('Result:', store_ans)
    captured = capsys.readouterr()
    assert captured.out == "Result: 20\n"

def test_terminal_output2(capsys):
    store_ans = calculator.calculate(2,0, "multiply")
    print('Result:', store_ans)
    captured = capsys.readouterr()
    assert captured.out == "Result: 0\n"

def test_argument_passing(monkeypatch):
    monkeypatch.setattr("sys.argv", ["calculator.py", "6", "2", "divide"])
    assert calculator.calculate(6, 2, "divide") == 3.0

   # Add more tests to cover edge cases and negative scenarios

  