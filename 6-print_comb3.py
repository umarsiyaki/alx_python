for i in range(10):
    for j in range(i + 1, 10):
        print(f'{i}{j:02d}', end=', ')
print()  # To add a newline after the last combination
