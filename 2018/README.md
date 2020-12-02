# Advent of Code 2018 in Python

Goals:
1. Write professional quality, debugable, tested python code.
2. Use more classes and dunder methods.


## Setup

Use pip to install all requirements

```
make
```

## Run everything

```
make run
```

### Run a single day

```
python day01.py
```

## Tests

```
make test
```

## Linting

```
make pylint
```

### Lint a single file

```
make day01.pylint
```

## Comments:
### Day01
No Issues.

### Day02
Initially made a mistake in the function find_similar-boxids. 
I Originally did:
```
for char1 in boxid1:
  for char2 in boxid2:
    if char1==char2:
       ...
```
This is incorrect as it compares everything to everything else in each string. The newer implementation uses zip which works.

### Day03
I initially wrote this as a hacky set of functions using lists (note: I am avoiding numpy for this year).
I made a number of mistakes:
1. I used variables like Xsize and YSize, rather than Rows and columns. This just confused the code.
2. I got rows and columns mixed around.
3. I didn;t have a good way of viewing my grid without needing a lot of [[".","."]] characters. Switching to a class using the ```__repr__``` method made this much much easier to debug.

