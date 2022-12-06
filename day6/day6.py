data = open('day6/in6', 'r').read()


def find_markers(data, sig_len):
    markers = []
    for i,s in enumerate(data):
        if i>=sig_len-1:
            sample = data[i-(sig_len-1):i+1]
            if len(set(sample)) == len(sample):
                markers.append(i+1) # 1-indexed
    return markers


print(f"Result1: {find_markers(data, 4)[0]}")
print(f"Result2: {find_markers(data, 14)[0]}")