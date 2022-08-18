def matchingStrings(strings, queries):
    res = []

    for i in range(len(queries)):
        counter = 0
        for j in range(len(strings)):
            if queries[i] == strings[j]:
                counter += 1
        res.append(counter)
    return res
