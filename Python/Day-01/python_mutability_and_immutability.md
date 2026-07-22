1. If strings are immutable, then why does this works?
username = "shadow"
username = "super"

- It looks like the string changed, but it didn't. The varibale changed it reference, not the string object.

2. Everything in python is an Object, Python treats almost everything as an object.
* int, float, string, list, dict -> objects
* Variables do not store the actual value, variables store reference(addresses) to objects.

3. How Python stores Data
username = "shadow"
- Python stores the string "shadow" in memory and the variable username holds a reference to that
now:
username = "super"
- python does not modify "shadow" in memory, instead it creates a new string object "super" and updates the reference of the variable username to point to the new string object. 
- The "shadow"  object remain unchanged. if nothing references it anymore, Python's garbage colletor removes it later.

so, when you assign a new value to a variable that holds an immutable object, Python creates a new object and updates the reference of the variable to point to the new object. The original object remains unchanged in memory until it is no longer referenced and is eventually garbage collected.

4. why strings are immutable?
- Strings are immutable in Python because they are designed to be hashable and can be used as keys in dictionaries. If strings were mutable, their hash values could change, leading to inconsistencies and errors when used as dictionary keys. Additionally, immutability allows for better performance and memory optimization, as strings can be shared and reused without the risk of unintended modifications.

5. varibales != objects
- varibales are just references to objects in memory. when you assign a new value to a variable, you are not modifying the object itself, but rather changing the reference of the variable to point to a new object.

6. Mutable vs Immutable Objects

Immutable Objects: cannot be modified after creation.
* int
* float
* bool
* string
* tuple 
* bytes
* frozenset

Mutable Objects: can be modified after creation without creating new object.
* list  
* dict
* set
* bytearray