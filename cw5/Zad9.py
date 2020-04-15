def reverse(data):
    for index in range(0, len(data), 1):
        if(index %2 == 0):
            yield data[index]
ob = reverse("Szynka")
print(next(ob))
print(next(ob))
print(next(ob))