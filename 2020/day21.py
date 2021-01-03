"""
AOC day 21 2018
"""
from collections import defaultdict, deque
# pylint: disable=missing-module-docstring

class AllergenList:
    '''Learn a new language from an allergen list'''
    def __init__(self,ingredlistfile):
        '''
        Read a datafile and store recipies ingredients and allergens in a dict.
        Dict keys are reicpie number.
        List of sets where first set is ingredients, second set is allergens
        '''
        self.recipies={} # Num, [set(ingredients),set(allergens)]
        self.allergens={} # Allergen name (e.g. Dairy): allergen ingredient name (e.g masjdbg)
        self.allallergens=defaultdict(int) # Allergen name (e.g. Dairy): list of times appears.
        self.allingredients=set() # All ingredient names
        self.safeingredients=defaultdict(int) # all non-allegen ingredients

        with open(ingredlistfile) as inputfile:
            alldata=inputfile.read().split('\n')
        for i, line in enumerate(alldata[:-1]):
            myline=line.replace(')','').split(" (contains ")
            ingredients={ingredient for ingredient in myline[0].split()}
            allergens={allergen for allergen in myline[1].replace(',','').split()}
            self.recipies[i]=[ingredients, allergens]
        self.update_alling()

    def update_alling(self):
        '''Update the global variables allingredients and allallergens'''
        # Initialise global sets
        for recipie in self.recipies.values():
            self.allingredients |= recipie[0]
            for allergen in recipie[1]:
                self.allallergens[allergen] +=1

    def determine_allergen(self,allergen):
        '''
        for each recipie containing this allergen, perform the intersection of all
        ingredients, and if this yields a single ingredient return this ingredient.
        '''
        assert allergen in self.allallergens
        recipies_with_this_allergen=[]
        for key,recipie in self.recipies.items():
            if allergen in recipie[1]:
                recipies_with_this_allergen.append(key)

        common_ingreds=self.allingredients.copy()
        for recnum in recipies_with_this_allergen:
            common_ingreds &= self.recipies[recnum][0]
        if len(common_ingreds) == 1:
            return common_ingreds.pop()
        return None


    def determine_all_allergens(self):
        '''
        Loop through all possible allergens and establish which one is each ingredient.
        If an allergen- ingredient mapping is found:
            1. remove that allergen from all reicpies and allergen lists.
            2. Once all the allergens are identified count the number of safe ingredients

        ToDo: Make this method smaller by breaking out parts into smaller methods.
        '''
        max_allegens_per_rec=max([len(allergens[1]) for allergens in self.recipies.values()])
        allergen_queue = deque()
        # Find the recipie with the longest list of allergens and add that
        #  to the queue.
        for recipie in self.recipies.values():
            if len(recipie[1]) == max_allegens_per_rec:
                for allergen in recipie[1]:
                    allergen_queue.append(allergen)
        counter=0
        while len(allergen_queue) >0 :
            this_allergen=allergen_queue.pop()
            this_allergen_ing=self.determine_allergen(this_allergen)
            if this_allergen_ing is not None:
                # Store mapping
                self.allergens[this_allergen]=this_allergen_ing

                # remove the allergens and ingredients from main recipies list
                for key,recipie in self.recipies.items():
                    if this_allergen in recipie[1]:
                        self.recipies[key][1].remove(this_allergen)
                    if this_allergen_ing in recipie[0]:
                        self.recipies[key][0].remove(this_allergen_ing)

                # Update global lists.
                self.update_alling()
                # if any ingredients contain no allergens,
                #  remove that recipe and put and ingredients in the safe list.
                empty_recipies=[]
                for key,recipie in self.recipies.items():
                    if len(recipie[1]) == 0:
                        for ing in recipie[0]:
                            self.safeingredients[ing]+=1
                        empty_recipies.append(key)
                # Remove empty recipies from global list.
                for key in empty_recipies:
                    del self.recipies[key]
                # remove this allegen ingredient from the list of safe ones.
                if this_allergen_ing in self.safeingredients:
                    del self.safeingredients[this_allergen_ing]
            else:
                allergen_queue.appendleft(this_allergen)
            counter+=1
            if counter>10:
                # this is needed as occasionally there are ingredients in the queue
                #  that have already been solved for.
                break


    def run(self):
        '''
        Find all allergens.
        '''
        while len(self.recipies) > 0:
            self.determine_all_allergens()
        # Part 2 requires alphabetical ordering.
        allergen_sorted_keys = sorted(self.allergens)
        part2output=''
        for allergen in allergen_sorted_keys:
            part2output+=self.allergens[allergen]+','
        print(f'2101: Number of appearances of safe ingredients: {sum(ingnum for ingnum in self.safeingredients.values())}')
        print(f'2102: List of Allergens: {part2output.rstrip(",")}')
        return sum(ingnum for ingnum in self.safeingredients.values())


def day21_01():
    """Run part 1 of Day 21's code"""
    path = "./input/21/input.txt"
    testrec = AllergenList(path)
    testrec.run()

def day21_02():
    '''Don't run part2 as we solved it in part 1'''

if __name__ == "__main__":
    day21_01()
