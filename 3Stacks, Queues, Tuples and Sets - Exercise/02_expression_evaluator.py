from collections import deque

strings = deque(x for x in input().split())

numbers = deque()
print(numbers)
for element in strings:
    if element in "+-*/":
        while len(numbers) > 1 :
            pass


string_expression = input().split()

numbers = deque()
print(numbers)
for element in string_expression:
    if element in "+-*/":
        while len(numbers) > 1:
            num_one = numbers.popleft()
            num_two = numbers.popleft()

            result = 0

            if element == "+":
                result = num_one + num_two
            elif element == "-":
                result = num_one - num_two
            elif element == "*":
                result = num_one * num_two
            else:
                result = num_one // num_two

            numbers.appendleft(result)

    else:
        numbers.append(int(element))

print(numbers.popleft())