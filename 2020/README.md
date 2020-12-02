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
