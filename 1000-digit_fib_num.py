def fibonacci():
    fibonacci_sequence = [0, 1]
    acc = 0
    while True:
        length = len(fibonacci_sequence)
        index_n_1 = length - 2
        index_n_2 = length - 1
        next_term = fibonacci_sequence[index_n_1] + fibonacci_sequence[index_n_2]
        fibonacci_sequence.append(next_term)

        if len(str(next_term)) >= 1000:
            return fibonacci_sequence.index(next_term)

print(fibonacci())