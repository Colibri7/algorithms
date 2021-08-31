def palimdrom(text):
    if text==text[::-1]:
        return True
    return False

a = input()
print(palimdrom(a))