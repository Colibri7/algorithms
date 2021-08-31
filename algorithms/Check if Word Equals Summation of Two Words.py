class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:

        arr1 = []
        arr2 = []
        arr3 = []
        for i in firstWord:
            arr1.append(str(ord(i) - 97))
        for i in secondWord:
            arr2.append(str(ord(i) - 97))
        for i in targetWord:
            arr3.append(str(ord(i) - 97))

        res1 = int(''.join(arr1))
        res2 = int(''.join(arr2))
        res3 = int(''.join(arr3))
        if res1 + res2 == res3:
            return True
        else:
            return False

