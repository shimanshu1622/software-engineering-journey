# Python internal working (memory, references, and garbage collection)

> Python hides most of the memory management from the programmer, but understanding references, objects, and memory behavior is essential for writing correct python code and for interviews.

### 1. Everything is an object
- every value in python is stored as an object in memory.
- exp: int->object, float->object, list->object, etc.
- variables do not contain the actual data.
- they only contain a reference (address) to an object.
```
score = 10
             +----+
score -----> | 10 |
             +----+
```
### 2. multiple variables can reference the same object
```
score = 10
another_score = 10
```
- python may optimize memory by making both variables point to the same object in memory.
```text
        score ------
                   |
                   v
                +----+
                | 10 |
                +----+
                   ^
                   |
another_score ------
```

### 3. reference count
- every object in python has a reference count, which keeps track of how many variables are referencing that object.
- when a new reference is created, the reference count is incremented.
- when a reference is deleted, the reference count is decremented.
- when the reference count reaches zero, the object is eligible for garbage collection.
```
a = 10
b = a
```
- reference count of object 10 is 2 (a and b are referencing it).
> if one reference is removed: a = 'python', the reference count of object 10 becomes 1 (only b is referencing it).

### 4. garbage collection
- python automatically frees memory for objects that are no longer referenced.
```
a = 'python'
                            +------+
                     a ---> |python|
                            +------+

a = 'java'
                            +------+
                     a ---> | java |
                            +------+

                          +------+
                          |python|     <--- no references
                          +------+ 

```

> The object 'python' has no references and will eventually be removed by python's garbage collector.

### 5. Numbers and strings are optimized
- Python treats numbers and strings differently from mutable objects like lists.
- Instead of immediately deleting unused numbers or strings, python may keep them in memory for a while because they are immutable and can be reused.
> From above example, the object 'python' may not be immediately deleted from memory, and if we create another variable with the same value, it may point to the same object in memory.

### 6. Data type belongs to the object
- beginners often think: variable has a type, but in python, 
```
Object has a type
variable only stores a reference
```
> Immutable objects create new objects when modified, while mutable objects can be modified in place.

### 7. Mutable objects
- lists behave differently because they are mutable.
```
list1 = [1,2,3]
list2 = list1
```
Memory:
```
list1 -----+
           |
           v
        +-----+
        | 1 2 3|
        +-----+
           ^
           |
list2 -----+
```
> both list1 and list2 point to the same list object in memory. If we modify the list using either variable, the change will be reflected in both.

- modifying a shared list:
```
list1[0] = 33 
```
- modifying the first list will reflect in the second list as well, because both variables refer to the same mutable list object.
> Now,

```
p1 = [1,2,3]
p2 = p1  # here p2 is referencing the same list object as p1

p2 = [1,2,3] # but here p2 is now referencing a new list object.
```
> Although the content are the same, these are different objects in memory. The first list object is still referenced by p1, while p2 now points to a new list object.
- changing the content of p2 will not affect p1, and vice versa.

### == vs is
- `==` checks whether values are equal. (compares content)
- `is` checks whether both variables refer to the same object in memory. (compares references)
```
m = [1,2,3]
n = m

m == n  # True, same value
m is n  # True, same object in memory
```

```
p = [1,2,3]
q = [1,2,3]

p == q  # True, values are equal
p is q  # False, different objects in memory
```  
## Summary
- Every value is stored as an object.
- variables store references, not data.
- Objects maintain a reference count.
- garbage collection removes unreferenced objects.
- numbers and strings receive additional memory optimization.
- objects have types, not variables.
- immutable objects create new objects when changed.
- mutable objects can be modified in place.
- use slicing `([:])` or `copy.copy()` to create independent list copies.
- use `==` to compare values and `is` to compare references. 



