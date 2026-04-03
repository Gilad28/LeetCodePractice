class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for ch in s:
            if ch == "[" or ch == "(" or ch == "{":
                stack.append(ch)
            if not stack:
                return False
            if ch == "]":
                if stack.pop() != "[":
                    return False 
            if ch == ")":
                if stack.pop() != "(":
                    return False 
            if ch == "}":
                if stack.pop() != "{":
                    return False 
        
        return len(stack) == 0
            

        