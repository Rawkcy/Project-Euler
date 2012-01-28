# find sum of even numbered elem of fibonacci sequence under 4 mil

# generate fibonacci sequence
# during the generation, check if it is over 4 mil
# if yes then break
# also check if the element is even
# if yes then add to sum

even_sum = 2
fib_sequence = [1, 2]
while (next_entry <= 4000000):
    next_entry = 0
    for i in fib_sequence[-2:]:
        next_entry += i
    if (next_entry%2 == 0):
        even_sum += next_entry
    fib_sequence.append(next_entry)
print even_sum
