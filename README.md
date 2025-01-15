# Fibonacci Sequence Calculator with Memoization

This project implements a Fibonacci number calculator using memoization technique to optimize performance.

## Description

The `main.py` file contains two main components:

1. **Value Class**
   - Manages data persistence through a JSON file
   - Automatically loads and saves calculated results
   - Uses `value.json` as storage file

2. **fibo Function**
   - Calculates the nth number in the Fibonacci sequence
   - Uses memoization to avoid redundant calculations
   - Stores intermediate results in a JSON file

## How it Works

The program uses a recursive approach with memoization to calculate Fibonacci numbers. Previously calculated results are stored in a JSON file to avoid recalculating the same values in future executions.

## Usage

```python
from main import Value, fibo

# Create a Value instance for memoization
memory = Value()

# Calculate the 10th Fibonacci number
result = fibo(10, memory)

print(result)
```

This code will calculate the 10th Fibonacci number and display the result. Intermediate results will be stored in the `value.json` file for future use.