from collections import deque

# Make a deque
deq = deque("abcdefg")

# Iterate over the deque's element
[item.upper() for item in deq]
# >>> deque(["A", "B", "C", "D", "E", "F", "G"])

# Add a new entry to right side
deq.append("h")
# >>> deque(["A", "B", "C", "D", "E", "F", "G", "h"])

# Add an new entry to the left side
deq.appendleft("I")
# >>> deque(["I", "A", "B", "C", "D", "E", "F", "G", "h"])

# Remove right most element
deq.pop()
# >>> "h"

# Remove leftmost element
deq.popleft()
# >>> "I"

# empty deque
deq.clear()
