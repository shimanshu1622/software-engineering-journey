# How python works
```
python source code(.py) ---> python compiler ---> bytecode(.pyc) ---> python virtual machine ---> machine instruction ---> CPU
```

- print("Hello World") from python source code(.py) is compiled into bytecode(.pyc) by the python compiler. The bytecode is then executed by the python virtual machine, which translates it into machine instructions that the CPU can understand and execute.

## Bytecode 
- bytecode is a low-level representation of the source code that is platform-independent. It allows Python to be portable across different operating systems and hardware architectures. The Python virtual machine (PVM) is responsible for interpreting the bytecode and executing it on the underlying hardware.

- bytecode files (.pyc) are generated automatically when a Python script is run. These files are stored in the __pycache__ directory and can be reused to speed up subsequent executions of the same script.

> bytecode looks something like this: 
```
LOAD_NAME 0 (print) 
LOAD_CONST 0 ('Hello World') 
CALL_FUNCTION 1 
RETURN_VALUE
```

- Humans cannot directly read or understand bytecode.

## Python is both compiled and interpreted. 
- The source code is first compiled into platform-independent bytecode(.pyc) by the python compiler, and then the bytecode is interpreted and executed by the python virtual machine (PVM). This combination of compilation and interpretation allows python to be both efficient and flexible.
 
### Frozen Binaries 
- Python can also be distributed as frozen binaries, which are standalone executables that contain the Python interpreter and all the necessary libraries and dependencies. This allows Python applications to be run on systems without requiring a separate Python installation. some exp of this are PyInstaller, cx_Freeze, and py2exe. 

### Cpython
- The standard implementation of Python is written in C and is known as CPython. It is the most widely used implementation and provides the reference for the Python language specification. CPython compiles Python source code into bytecode and executes it using the Python virtual machine.