import sys
try:
    filename = sys.argv[1]
    num_lines = int(sys.argv[2])
except IndexError:
    print('Usage: python capslock.py <inputfile> <numlines>')
else:
    index = 1
    with open(filename, 'r') as reader:
        for line in reader:
            print(line.strip().upper())
            if index >= num_lines:
                break
            index += 1
