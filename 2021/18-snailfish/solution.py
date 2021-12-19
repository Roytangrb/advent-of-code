import sys
import json
from math import floor, ceil
from typing import Union
    
class Pair:
    left: Union["Pair", int]
    right: Union["Pair", int]
    
    def __init__(self, l, r):
        if isinstance(l, (int, Pair)):
            self.left = l
        else:
            self.left = Pair(l[0], l[1])
        if isinstance(r, (int, Pair)):
            self.right = r
        else:
            self.right = Pair(r[0], r[1])
    
    def __repr__(self) -> str:
        return f"[{self.left}, {self.right}]"
    
    def add_to_left(self, val):
        if isinstance(self.left, int):
            self.left += val
        else:
            self.left.add_to_left(val)
    
    def add_to_right(self, val):
        if isinstance(self.right, int):
            self.right += val
        else:
            self.right.add_to_right(val)
        

def add(a, b):
    new_root = Pair(a, b)
    
    def dfs(root: Union["Pair", int], depth: int):
        if isinstance(root, int):
            return root, None, None
        else:
            if depth == 4:
                return 0, root.left, root.right
            else:
                new_l, l_l, l_r = dfs(root.left, depth+1)
                if l_r is not None:
                    root.left = new_l
                    if isinstance(root.right, int):
                        root.right = root.right + l_r
                    else:
                        root.right.add_to_left(l_r)
                
                new_r, r_l, r_r = dfs(root.right, depth+1)
                if r_l is not None:
                    root.right = new_r
                    if isinstance(root.left, int):
                        root.left = root.left + r_l
                    else:
                        root.left.add_to_right(r_l)
                
                # handle split, after above explode steps, if current depth is 3,
                # left and right should int
                if isinstance(root.left, int) and root.left >= 10:
                    if depth == 3:
                        root.left = floor(root.left/2)
                        root.right += ceil(root.left/2)
                    else:
                        root.left = Pair(floor(root.left/2), ceil(root.left/2))
        
                if isinstance(root.right, int) and root.right >= 10:
                    if depth == 3:
                        root.left += floor(root.right/2)
                        root.right = ceil(root.right/2)
                    else:
                        root.right = Pair(floor(root.right/2), ceil(root.right/2))
                return root, l_l, r_r
                
    dfs(new_root, 0)
    return new_root
    

with open(sys.argv[1], 'r') as f:
    left, right = json.loads(f.readline().strip())
    root = Pair(left, right)
    
    for line in f:
        left, right = json.loads(line.strip())
        to_add = Pair(left, right)
        root = add(root, to_add)
    print(root)
        