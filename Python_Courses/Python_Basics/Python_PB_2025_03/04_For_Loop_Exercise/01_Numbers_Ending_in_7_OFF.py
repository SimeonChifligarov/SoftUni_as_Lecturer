with open('test_01.py', 'w') as f:
    for number in range(7, 1001, 10):  # [7, 17, 27, ... 997]
        f.write(f'print({number})\n')
