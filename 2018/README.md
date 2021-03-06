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

### Day04
1. I had a lot of issues naming variable and methods here. 
2. Again I started wtih a hacky set of functions. Classes are so superior for testing!!!!

## Day05
1. I am pretty sure that react and reactonce could be merged into a single method.
2. I initially had a for loop in reactonce, but later realised I needed a variable step size, in case the last two characters were removed, the second to last character was the next expected raising an out of bounds error.
3. Initially I was doing a single merge per call. This was too slow.
4. Part 2 takes a long time to run. There is definitely a more efficient approach somehow?
