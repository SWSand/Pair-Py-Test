import calculator
import sys
import subprocess

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
    # # monkeypatch.setattr("sys.argv", ["python3", "calculator.py", "6", "2", "divide"])
    # # print("test start")
    # result = subprocess.run(["python3" ,"calculator.py", '6', '2', "divide"], capture_output=True, text=True)
    # print(result.returncode)
    # print(result.stdout)
    # print(result.stderr)
    # # captured = capsys.readouterr()
    # # print(captured)
    # assert result.stdout == "Return: 3.0\n"
    # # assert calculator.calculate(6, 2, "divide") == 3.0
    # # num1 = float(calculator.sys.argv[1])
    # # num2 = float(calculator.sys.argv[2])
    # # operation = calculator.sys.argv[3]

    # # result = calculator.calculate(num1, num2, operation)
    # # print(f"Result: {result}")
    monkeypatch.setattr("sys.argv", ['python3',"calculator.py", "6", "2", "divide"]) 
    process = subprocess.run(sys.argv, capture_output=True, text=True)
    assert process.stdout == "Return: 3.0\n"

   # Add more tests to cover edge cases and negative scenarios

  