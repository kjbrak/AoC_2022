data = open('day06/in6', 'r').read()


def find_marker(data, sig_len):
    for i,s in enumerate(data):
        if i>=sig_len-1:
            sample = data[i-(sig_len-1):i+1]
            if len(set(sample)) == len(sample):
                return i+1

    return None


print(f"Result1: {find_marker(data, 4)}")
print(f"Result2: {find_marker(data, 14)}")

