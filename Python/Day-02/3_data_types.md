# Python Data Types

> ## What are Data Types?
- A data type (or object type) defines the kind of data that can be stored in memory and the operations that can be performed on it.
- In python, everything is object. Therefore, the term **Data Type** and **Object Type** are often used interchangeably.

> ## Why are Data types important?
- programs mainly perform two tasks:
    1. Store data in memory
    2. Perform operations on that data

different types of data require different containers.

> ## Python Data Types

### 1. Numeric Data Types
- used to store numeric values.
```
Integer (int) a = 10
Float (float) b = 10.5 
Complex (complex) c = 2 + 3j
Decimal (decimal) d = 10.5
Fraction (fraction) e = 1/2
```

### 2. Strings
- used to store text data.
- strings can be written using single quotes, double quotes, and unicode characters.
```
Single quotes: 'Hello'   
Double quotes: "Hello"
```
> python also supports Unicode characters (including emojis and non-english text) using the u prefix: u'Hello' or u'\u2602'

- String Characteristics:
    - Ordered sequence
    - supports indexing and slicing
    - immutable (cannot be changed after creation)

### 3. Lists
- used to store a collection of items.
```
my_list = [1, 2, 3, 4, 5]
```
- features
    - ordered
    - mutable
    - indexed
    - can store different data types
```
my_list = [1, "Hello", 3.14, True]
nested_list = [1, 2, [3, 4], 5]
```

### 4. Tuples
- used to store a collection of items.
```
my_tuple = (1,2,3)
```
- uses:
    - ordered collection
    - similar to lists but immutable
    - can store different data types

### 5. Sets
- used to store a collection of unique items.
```
my_set = {"A", 1, 2, "hey"}
```

### 6. Dictionaries
- used to store key-value pairs.
```
my_dict = {
    "name": "John",
    "age": 30,
    "city": "New York"
}
```
- features:
    - unordered collection
    - mutable
    - indexed by keys
    - can store different data types

### 7. Boolean
- used to store True or False values.
```
True
False
```
- used in:
    - conditions
    - comparisons
    - decision making

### 8. None
- represents no value or absence of data.
```
temp = None
```
- used to indicate:
    - uninitialized variables
    - missing values
    - end of a function that does not return anything

> If a weather api that doesn't return a tempeature. Instead of returning 0 or -1, it can return None to indicate that the temperature is not available.

## Summary
| Data Type | Example | Key Feature |
|-----------|---------|-------------|
| Integer | 10 | Whole numbers |
| Float | 3.14 | Decimal numbers |
| Complex | 3+4j | Complex numbers |
| String | "Python" | Immutable text |
| List | [1,2,3] | Mutable ordered collection |
| Tuple | (1,2,3) | Ordered collection |
| Dictionary | {"name":"Shadow"} | Key-value pairs |
| Set | {1,2,3} | Unique elements |
| Boolean | True | Logical values |
| None | None | No value |


