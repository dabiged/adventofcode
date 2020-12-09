"""
AOC day 07 2018
"""
from lib.filehelper import file_to_str_array
from collections import deque
# pylint: disable=missing-module-docstring

def build_dict(test_input):
    """
    builds a dict of nested bags:

    Key is outer bag color
    Value is a List of Tuples.
    Tuple is Number of bags and their colors
    If a bag contains no other bags, its Value is a list containing None.
    """
    bags={}
    # loop over lines.
    for i in test_input:
        # light red bags contain 1 bright white bag, 2 muted yellow bags. 
        # |--outergbag-|         |----- inner baglist ------------------|
        outerbag, innerbaglist = map(str, i.split("contain"))
        outerbag=outerbag.replace(" bags ","")
        innerbagdict={}
        for innerbagstr in innerbaglist.split(","):
            # innerbag[0] = '1 bright white bag'
            # innerbag[1] = '2 muted yellow bags.
            innerbagall=innerbagstr.split()

            if innerbagall[0] == 'no':
                innerbagdict={}
            else:
                innerbagdict[" ".join(innerbagall[1:-1])]= int(innerbagall[0])
        if outerbag not in bags:
            bags[outerbag]=innerbagdict
    return bags

def bags_that_can_contain_our_bag(bags_to_contain,ourdict):
    """
    Find out the set of all possible bags that could contain our bag.
    """
    # The list of all possible bags.
    validbags=set()
    while len(bags_to_contain) >0:
        # All the bags that could contain the current bag.
        bags_that_can_contain_bags_to_contain =set()
        for innerbag in bags_to_contain:
            for bag in ourdict:
                if innerbag in ourdict[bag]:
                    # If a bag could have an bag inside (innerbag)
                    # Add it to the set of bags.
                    bags_that_can_contain_bags_to_contain|={bag}

        validbags=validbags.union(bags_that_can_contain_bags_to_contain)
        bags_to_contain = bags_that_can_contain_bags_to_contain
    return validbags

def bags_could_contain_our_bag_queue(bags_to_contain,ourdict):
    """
    Find which bags could be used to contain our bag, 'shiny gold'
    using a queue data structure.
    """
    # The list of bags to return
    bags = []
    # Our queue of bags to check
    queue = deque(['shiny gold'])
    while len(queue) >0:
        #Grab the key to check
        key = queue.pop()
        # Loop over everything in ourdict
        for bagkey in ourdict:
            # if the bag exists inside another bag add the outer bag to the list, 
            #   and check if the new outer bag is inside any other bags by adding 
            #   it to the queue.
            if key in ourdict[bagkey]:
                bags.append(bagkey)
                queue.append(bagkey)
    # Return only the list of unique bags.
    return set(bags)

def bags_in_our_bag(contained_bags,ourdict):
    """
    Final all bags that are in our bag
    """
    bags = {}
    # Create a double ended Queue to traverse the tree row by row.
    queue = deque([{'shiny gold':1}])
    while len(queue) > 0:
        # Grab the next item in the queue
        thisbag = queue.pop()
        for key, value in thisbag.items():
            # This is a shitty way of getting the dict keys/values out of the queue.
            # The for loop only ever runs through once but turns thisbags keys/values
            #    from .keys()/.values() datatypes into str/ints.
            #  I am probably using the wrong data structure but this works.
            color = key
            amount= value
        for key in ourdict[color]:
            # Traverse the tree adding the new leaves to the queue to process later.
            queue.append({key: ourdict[color][key] * amount})
            if key not in bags.keys():
                # I hate this initialise/add to dict as an if statement. 
                #  Note to self: Look into defaultdicts or something like that.
                bags[key] = ourdict[color][key] * amount
            else:
                bags[key] += ourdict[color][key] * amount
    return sum(bags.values())

def day07_01():
    """Run part 1 of Day 07's code"""
    path = "./input/07/input.txt"
    part1dict=build_dict(file_to_str_array(path))
    ourbag={'shiny gold':1}
    result=len(bags_that_can_contain_our_bag(ourbag,part1dict))
    print(f'0701: The number of bags that can contain our bag is: {result}')
    result2=len(bags_could_contain_our_bag_queue(ourbag,part1dict))
    print(f'0701: the number of bags that can contain our bag (with queue data structure) is: {result2}')

def day07_02():
    """Run part 2 of Day 07's code"""
    path = "./input/07/input.txt"
    part2dict=build_dict(file_to_str_array(path))
    ourbag={'shiny gold':1}
    result=bags_in_our_bag(ourbag,part2dict)
    print(f'0702: Sum of all bags in our bag: {result}')

if __name__ == "__main__":
    day07_01()
    day07_02()
