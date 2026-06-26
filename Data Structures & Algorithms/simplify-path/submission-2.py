class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        i = 0
        while i < len(path):
            if path[i] != '/':
                curr = ''
                while i < len(path) and path[i] != '/':
                    curr += path[i]
                    i += 1
                if curr == ".":
                    continue
                elif curr == '..':
                    if stack:
                        stack.pop()
                else:
                    stack.append(curr)
            i += 1
        
        return "/" + "/".join(stack) 
            

