class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        num = []
        left = 0
        right = 0
        sol = 0

        if not tokens:
                return 0

        for char in tokens:
            if char == "+" or char == "-" or char == "*" or char == "/":
                right = num.pop()
                left = num.pop()
                if char == "+":
                    sol = int(left) + int(right)
                    num.append(sol)
                if char == "-":
                    sol = int(left) - int(right)
                    num.append(sol)
                if char == "*":
                    sol = int(left) * int(right)
                    num.append(sol)
                if char == "/":
                    sol = int((left) / int(right))
                    num.append(sol)
            else:
                num.append(int(char))

        return num[0]
                
