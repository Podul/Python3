

def checkio(data):
    list2 = []
    count = 0
    for x in data:
        for y in data:
            if x == y:
                count += 1
        if count >= 2:
            list2.append(x)
        count = 0
    print(list2)
    return data


checkio([1, 2, 3, 4, 5])