# Advent of Code 2020 in Python

Goals:
1. Write readable, tested, professional quality code.
2. Explore gaps in my python knowledge, specifically standard libraries I am not familiar with including itertools, deque, defaultdict

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
### Day01 - 

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


### Day04
1. I originally wrote this as a class called "IdentityList" which was the whole list of identities in one object. Trying to test each of the fields because too messy so I refactored the whole thing to be based on a single passport class.
2. I spent 10 mins figuring out that this:
```
"a" in ["0123456789abcdef"]
False
```
is not the same as this:
```
"a" in list("0123456789abcdef")
True
```
3. I opted to preprocess the input list into the same format as a python dict (i.e. {key1:value1,key2:value2...}). This is a bit against the spirit of the AOC (but life got in the way today). I was unable to use this format until I discovered the ```eval``` function. Apparently this is bad practice to use and I should have used the set_attr instead.
4. When checking the pid value I was casting the pid value to a int, zero padding and comparing to the original. Some pid's in invalid passports contain heights (e.g. 175cm) or hair colours (e.g. #3937bc). The casting of these strs to int failed so I used a try/except to fix it.

### Day05
1. All mistakes very minor. Binary partitioning implemented first go!
2. I was reminded that I do not need to create methods for accessing class variables and trying to do so will give very odd error messages. I had a str called self.rows, and a method called self.rows() which return self.rows. When I called self.rows() the error message was "'str' object is not callable".
3. Used a class for each boarding pass, with 3 methods, one each to calculate the row, col and seatid. Easy to debug, easy to implement.

### Day06
1. Managed to get part 1 quickly, part 2 was more complex.
2. Finally used Any/All in combination with a list comp!

### Day07
1. I really struggled with this. I was able to build the tree, using nested dicts quite easily but struggled to tranverse it without overwriting sections of the tree. The deque solved this.
2. I rewrote part 1 to also used the deque functionality, which I now understand much better.

### Day08
1. I found today quite easy, perhaps from all the trauma of the incode computer from 2019. I quickly wrote a class for the computer and was able to solve part 1 within ~40mins of starting.
2. Part 2 was not that much more difficult. I did make a mistake on not using a var.copy() when I should have.

### Day09
1. Easy one! I think I will probably rewrite both parts to use an itertools combination function.
2. Part 2 was particularly easy?!?!?

### Day10
1. Today was very satisfying as I managed to use deque, combinations from itertools and defaultdict; the three things I wanted to learn to use in this AOC!!!!
2. Part2 I knew how to solve within about 2 mins and managed to get the code running with very little debugging (missed colons, misnamed variables etc). __I managed to get my highest ranking so far of 3500 globally!!__

### Day11
1. I was able to reuse a lot of utility methods from day 3. I avoided most of the pitfalls from that day.
2. I thought the piece of code to look along lines of sight was neat.
3. Initialising numneighours to be the same as self.grid is poor practice, but seems to work.

### Day12
1. total time was ~ 90 mins for both parts. 
2. implementing the rotations was the most interesting part. I tried cycle from itertools but ran into infinite loops, and resorted to traditional geometry/trig.
3. for part 2, the formula I came up with for rotating around the origin in 90 degree increments was surprisingly simple. I had never noticed this before.

### Day13
1. Part 1 was pretty simple, but I was completely stumped on part 2. Due to my hectic schedule I did not get to spend the required time on it and instead used the sympy implementation of crt.
2. Today felt like another one of those math tricks you either know or don't and it is impossible to solve without it.

### Day14
1. I misread 36 as 32 and spent 10 mins trying to find out why my ```assert len(input) == 32``` was failing.
2. I wrote a class straight up with init, bin2int, int2bin, mask and run methods.  I was able to write all 5 methods in one go, then test them individually and get it up and running inside 50 mins (note I was busy this afternoon).
3. Used a double ended queue in part2 to deal with the increasing number of memlocs.
4. Made the mistake of using the part1 example to test part 2. Part1 example had 34 X's which made for a LOT of memory addresses in the queue to deal with.

### Day15
1. Today's problem was easy to implement. I had a functional part 1 submitted in ~ 38 mins. Part 2 was another story. I went through the following to get part 2 running:
2. Wrote part 1 with a full memory of the entire game as a list, which was appended to each step. Looking for the two last spoken number involved a nested search backwards through the entire list. Max turns ~50k in 30 sec.
```
        for i in reversed(range(0,len(memory)):
            if memory[i] == num:
                save(i)
            for j in reversed(range(0,i):
                if memory[i] == num
                    save[j]
                    break
```
3. Refactored the search algorithm to use a single loop that terminated when the second entry was found. This got my max turns upto around 100k in 30sec.
```
        lastcalled=[]
        while len(lastcalled) <2:
            if memory[i] == num:
                lastcalled.append(i)
        
        return lastcalled[0],lastcalled[1]
```
4. Tried lru_cache decorators on my functions to do memoization.
5. Refactored the memory of the entire game into a dictionary with key's as turn number and values as numbers. I was hoping to leverage the hash table lookup features but still keeping all of the game in the dictionary. I think this got the speed up to around 500k in 30 sec.
6. Realised that you don't need to keep all of the memory of the game stored. Switched to using a dictionary of numbers as keys, and a list of the last 2 times the number was spoken as values. This gets around 30M turns in 20secs.

### Day16
1. Key takeaway from today was the difference between deque.append and deque.leftappend and the fact that deque.pop selects from the right side of the queue. My implementation had a system where if you couldn't solve a field now, it went in the queue for checking later. However as I used append, not leftappend it just popped the same field forever.
2. I made two mistakes with initialising variables in the wrong loop. 

### Day17
1. Used a generator method to find all neightbours.
2. discovered you can query a dictionary with dict.get(key,ValueNotFound) where ValueNotFound is returned if the key does not exist. THis is super useful for problems like this.
3. By using a set of all board positions I was able to update the board without a copy saving a bunch of memory!

### Day18
1. Made the mistake of storing the equation as a dict, then after evaluating bracketed sections, I had to renumber (read: re-key) the entire dictionary. I refactored the storage of the equation to a list and this was done for me!
2. Immediately knew that this problem required the use of the eval function!
3. Wrote 1 method to do calculations without brackets and one method to remove brackets. this made part2 easy as I only needed to modify the calculation method.

### Day19
1. I felt this problem was the hardest of all 25 at first glimpse. I thought it was a Choamsky grammar style question requiring a custom parser. 
2. I peeked at the solution on reddit and saw that it could be easily done with regexp, after which I found it quite easy.

### Day20
1. The last puzzle I solved. part1 I finished about 2 days after release and I left part 2 until early January.

### Day21
1. I thought the problem statement was quite vague and spent a lot of time trying to understand it. I used sets for both the ingredients and allergens which was a nice shorthand.
2. Made a mistake again with no copy.

### Day22
1. On first pass I wrote a recursive program that gave the winner of the game. this was not enough and I needed to keep track of what the players hands were during the game.
2. Current implementation is very slow and needs optimizing. I would start by looking at using a hash algorithm over my current list of tuples.

### Day23
1. I tried implementing part1 using lists, but keeping track of the updates to the location was too hard. I gave up and looked at what others had done and used the dictionary system in place now.

### Day24
1. A fun puzzle. I made a lot of silly mistakes with the movements, and didn't really solve all of them until I had a full suite of tests.
2. In part 2 I made one major mistake, and that was to iterate only over hexes next to black tiles, and not black tiles themselves. This meant black tiles never flipped white.
3. I mis-transcribed one digit (day 6) on part 2 and so my tests were not working for this day. I ended up making an animation to debug this, which I didn't need!

### Day25
1. Today was surprisingly easy! my brute force search for the loop_size found the answer in only a minute or two. Not sure how to speed this up.
