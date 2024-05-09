# Instructions
1. Write a program in `main.py` that takes a single integer as input from the user.
2. If the input number is completely divisible by 3, 5, or 7, it is considered a Magic Number.
   - If the number is completely divisible by both 3 and 5, it is a Special Magic Number.
   - Print `Abracadabra` for Special Magic Numbers.
   - Print `Magic Number` for Magic Numbers.
   - Print `Not Magic Number` if the number does not satisfy any of the conditions.

## Example Input and Output

### Example 1
#### Example Input #1
```plaintext
5
```
#### Example Output #1
```plaintext
Magic Number
```
_**Explanation:** 5 is completely divisible by 5 and hence is a magic number._

### Example 2
#### Example Input #2
```plaintext
13
```
#### Example Output #2
```plaintext
Not Magic Number
```
_**Explanation:** 13 is not completely divisible by 3, 5, or 7 and hence is not a magic number._

### Example 3
#### Example Input #3
```plaintext
15
```
#### Example Output #3
```plaintext
Abracadabra
```
_**Explanation:** 15 is completely divisible by 3 and 5, and hence is a special magic number._

## Hint
1. Use the modulo operator `%` to check if a number is completely divisible by another number.
   - `X % Y == 0` is true if X is completely divisible by Y.
   - `X % Y != 0` is true if X is not completely divisible by Y.
2. Implement conditional statements (`if`, `elif`, `else`) to handle the three scenarios mentioned.

## Test Your Code
### Running Tests
- To verify your program, run it and check if it provides the correct output based on the input.
   ![image](tests_tools.png)
- If the output is correct, and there are no errors, proceed to submit it.
   ![image](submit.png)

### Test Results
- If your code passes all the tests, you will see the following screen.
   ![image](pass.png)
- If any test case fails, analyze the `Results` section to identify the error and refine your code.
   ![image](fail_tests.png)
   ![image](results.png)

## Final Note
- Make sure your program correctly identifies whether a number is Magic, Special Magic, or Not Magic before submitting your fully verified implementation.
   ![image](submit.png)
