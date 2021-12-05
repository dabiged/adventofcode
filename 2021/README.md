# Advent of Code 2020 in Python

### Goals:
1. use more advance python libraries. Itertools, threading, functools.
2. Get 20 stars in the month of December. (stretch goal 25)
3. Write good public classes, unit tests and clean code.
4. Keep complexity within a method understandable and debuggable. Don't be afraid to build 50 methods in a class if they are all simple.

### Summary:


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
1. was Rushing for leaderboard on part1 and was off-by-one. Submitted inside 2 mins though!
2. For part2 I started at arry location 2 and counted the next 2 measurements, not the last two. Again, rushing for leaderboard.

I ranked 3175/3057.

### Day02
Missed start of day by 1 minute.
1. Had issues with setup (didn't have things ready to go)
2. Lots of issues running previous day's code (unable to find day01_01 etc).
3. First mistake was not casting the input number to an int (was left as a str).
4. Second mistake was using the wrong input file reader (tried to import as array of ints).

### Day03
Missed whole day due to work and home stuff.
1. Initially built part 1 with functions, but refactored to use a class.
2. For part 1 I used a sort algorithm of sorted(str)[len(str)//2] to get the most common value. This did not work for part 2 and was re-written.
3. The whole CO2 vs O2 on equal value return confused me and the code is still weird but works.
4. I kept writing 02 and O2 :( .

### Day04
Was interupted a lot doing this.
1. really enjoyed today. I was very happy with my implementation.
2. was able to implement both the card and game classes immediately.
3. made the mistake of including diagonals.
4. had to refactor import for part 2.
5. Part 2 is slow but does the job.

I ranked ~5000.

### Day06

### Day07

### Day08

### Day09

### Day10

### Day11

### Day12

### Day13

### Day14

### Day15

### Day16

### Day17

### Day18

### Day19

### Day20

### Day21

### Day22

### Day23

### Day24

### Day25
