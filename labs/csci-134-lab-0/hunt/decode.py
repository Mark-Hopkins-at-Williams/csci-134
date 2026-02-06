def encode(s):
    return ''.join([chr(ord(ch)+3) for ch in s])


def decode(s):
    return ''.join([chr(ord(ch)-3) for ch in s])


if __name__ == '__main__':
    import sys
    try:
        filename = sys.argv[1]
    except IndexError:
        print("Please provide a filename!")
    else:
        with open(filename) as reader:
            for line in reader:
                print(decode(line))
