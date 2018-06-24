# Count
Count the number of ways message can be decoded

# Problem
Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, count the number of ways it can be decoded.
For example, the message '111' would give 3, since it could be decoded as 'aaa', 'ka', and 'ak'.

# Approach
- If message is empty considered as one count
- If message length is 1 considered as one count
- Else as we knows highest number is 26 i.e. z, so we need to process numbers in combination of 1 and 2 digits.

# Run
Change directory to count folder and execute <br>
```python3 run.py 121```
<br> <img src="https://i.imgur.com/luKsxEf.png">

# Test
Change directory to count folder and execute <br>
```python3 -m unittest tests/run_tests.py -v```
<br><br> <img src="https://i.imgur.com/gvCAF4Z.png">
