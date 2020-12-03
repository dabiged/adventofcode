# Advent of Code 2020 in Python

Goals:
1. Write readable, tested, professional quality code.
2. Explore gaps in my python knowledge, specifically standard libraries I am not familiar with including itertools.

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

1. Current implmentation is slow O(n^2) and O(n^3) but functional. 
2. Others have used itertools to sample all combinations of 2 or 3 from the pool which is something I should look at in future.
3. writing tests took less time than I feared and was very helpful.

### Day02

1. I originally misread part 2 and thought the letter had to be at BOTH locations in the password.

### Day03
1. I had a previously built class using very similar syntax from 2018 AOC. It already had init, repr, numcols, numrows and shape methods.
2. Made a mistake with an off-by-one error whilst looping through the run, and being overly specific with the end condition (!= instead of <=):
```
while row !=self.runrows()
```
should have been:
```
while row<= self.numrows()-1
```
3. Forgot to add a "self" parameter to the tree_count method which gave some odd errors.
4. Correctly set row and column steps as parameters in the tree_count method which made part 2 very easy.
5. Wrote all code and submitted both answers with writing tests.
