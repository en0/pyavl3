# pyavl3

A python dictionary alternative implemented with an AVL Tree.

# Quick Start

```bash
pip install pyavl3
```

```python
from pyavl3 import AVLTree

a = AVLTree()
a["a"] = "Hello"
a["b"] = "world"

print(", ".join(a))
```

## Why?

Python dictionaries are implemented on hashmaps. Hashmaps, besides being awesome, are a balancing
act between efficiency and memory utilization. Python's builtin algorithm is solid and probably the
correct choice 99 times out 100. Not really a supprise. But, hashmaps suffers from the need to
resize and resizing is pretty expensive. For those few cases where resizing large in-memory blocks
of sequentional memory is not going to work, AVLTrees might be a better option. Oh, and AVLTrees are
effectivly sorted. So, iterators are deterministic and always in order.

This table compairs the runtime characteristics of Hashtables and AVLTrees

|        	| Hashtable 	| Hashtable(worst case) 	| AVLTree 	| AVLTree(worst case) 	|
|--------	|-----------	|-----------------------	|---------	|---------------------	|
| Space  	| O(n)      	| O(n)                  	| O(n)    	| O(n)                	|
| Search 	| O(1)      	| O(n)                  	| O(logn) 	| O(logn)             	|
| Insert 	| O(1)      	| O(n)                  	| O(logn) 	| O(logn)             	|
| Delete 	| O(1)      	| O(n)                  	| O(logn) 	| O(logn)             	|
| Resize 	| O(n)      	| O(n)                  	| N/A     	| N/A                 	|
