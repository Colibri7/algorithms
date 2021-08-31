class HappyNumber:
    def isHappy(self, n: int) -> bool:
        if n == 1:
            return True
        elif n == 4:
            return False
        else:
            return self.isHappy(sum(list(map(lambda x: int(x) ** 2, list(str(n))))))

