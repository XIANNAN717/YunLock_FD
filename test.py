
def a():
    try:
        a = 1
        a+None
        return a
    except:
        return a
print(a())