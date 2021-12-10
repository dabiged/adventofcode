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

I ranked 6605/5586

### Day03
Missed whole day due to work and home stuff.
1. Initially built part 1 with functions, but refactored to use a class.
2. For part 1 I used a sort algorithm of sorted(str)[len(str)//2] to get the most common value. This did not work for part 2 and was re-written.
3. The whole CO2 vs O2 on equal value return confused me and the code is still weird but works.
4. I kept writing 02 and O2 :( .

No Ranking.

### Day04
Was interupted a lot doing this.
1. really enjoyed today. I was very happy with my implementation.
2. was able to implement both the card and game classes immediately.
3. made the mistake of including diagonals.
4. had to refactor import for part 2.
5. Part 2 is slow but does the job.

I ranked 5292/4993

### Day05
Started on time.
1. Perfect example of why I love AOC. simple-ish problem. Lots of nuance.
2. Coded part 1 in around 17-18 mins. 12 mins towrite test cases and debug.
3. Part2 was harder than I thought. I just did for row in row1, row2, for col in col1, col2 and drew big squares :( . 
4. I think there is a more elegant solution to my birds nest of if-then statements.

I ranked 4521/4752.

### Day06
Started 34 min late. Finished in 31 mins.
1. Used a dictionary of age:count to prevent exponential list operations. This is O(1) vs O(exp).
2. Was confused about part 2. It was one of the "Just increase the number to ensure you have an efficent algorithm" days.

### Day07
1. Easy puzzle. Coded and worked first try! Done in around 11 mins.
2. For part two I brute forced a solution. In hindsight I should have only passed the abs(diff) to the cost function and used a closed form solution to generate it.

### Day08
1. Couldn't find time to do this Due to work. Ended up doing 5 separate sessions over 2 days which made things much harder.
2. Struggled with finding the right data structures. I was initially passing sets which are unhashable and cannot be used as dict keys.
3. Made the mistake of removing items from a list while looping over it.
4. Probably the hardest problem so far for me.

### Day09
1. Missed start by around 2 hours.
2. Found this problem surprisingly easy. I was able to write a recursive basin finder on the first try!!

### Day10
Start on time! Got around 15 mins and got called away for 1 hour.
1. Nice problem. There is probably a regex solution that is easier to follow than my spaghetti code.
2. I felt the problem definition was a little ambigious and the example wasn't well laid out. I had to read it about 5 times to understand it.

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
