from collections import defaultdict
from random import choice, sample

class Target:
    def __init__(self, *, dictionary = 'dictionary.txt',
                 target = None,
                 minimal_length = 4):
    
        self.dictionary = dictionary
        self.minimal_length = minimal_length
        
        with open(self.dictionary) as lexicon: #####################
            self.words = dict()
            for line in lexicon:
                word = line.rstrip()
                if len(word) == len(set(word)):
                    self.words[word] = set(word)

        # A LIST OF SETS
        self.targets_letters = [self.words[word] for word in self.words if len(word) == 9]

        if target:
            if len(target) == 9 and set(target) in self.targets_letters: #####################
                self.target = target
                self.target_letters = set(target)
            else:
                target = None
                print(f'{target} is not a valid target, a random one will be generated instead.')

        if not target:
            #Choose random set 
            self.target_letters = choice(self.targets_letters)
            #Randomly arrange letters in the set to a string
            self.target = ''.join(sample(self.target_letters, 9))
        self.solutions = self._solve_target()

    def __str__(self):
        target = ''
        for i in range(9):
            if i % 3 == 0:
                target += f'\n       ___________\n\n      | {self.target[i]} |'
            else:
                target += f' {self.target[i]} |'
        target += '\n       ___________\n'
        return target

    def __repr__(self):
        return f'Target(dictionary = {self.dictionary}, minimal_length = {self.minimal_length})'

    def _solve_target(self):
        solutions = defaultdict(list)
        for word in self.words:
            if self.minimal_length <= len(word) and self.target[4] in self.words[word] and self.words[word].issubset(self.target_letters): ##############################
                solutions[len(word)].append(word)                                 
        return solutions
    
    def number_of_solutions(self):
        print(f'In decreasing order of length between 9 and {self.minimal_length}:')
        for length in range(9, self.minimal_length - 1, -1):
            nb_of_solutions = len(self.solutions[length])
            if nb_of_solutions == 1:
                print(f'    1 solution of length {length}') ##### Eric's code has 'l' not 1
            elif nb_of_solutions > 1:
                print(f'    {nb_of_solutions} solutions of length {length}')
                
    def give_solutions(self, minimal_length = None):
        if minimal_length == None:
            minimal_length = self.minimal_length
        for length in range(9, minimal_length - 1, -1):
            if not self.solutions[length]:
                continue
            if length != 9:
                print()
            if len(self.solutions[length]) == 1:
                print(f'Solution of length {length}:\n    {self.solutions[length][0]}')
            else:
                print(f'Solutions of length {length}:')
                for solution in self.solutions[length]:
                    print(f'    {solution}')

    def change_target(self, to_be_replaced, to_replace):
        if to_be_replaced != to_replace and len(to_be_replaced) == len(to_replace):
            if set(to_be_replaced) <= self.target_letters: ##############################
                new_target_letters = self.target_letters - set(to_be_replaced) | set(to_replace)
                if new_target_letters in self.targets_letters:
                    old_target_letters = self.target_letters
                    old_letter_at_centre = self.target[4]
                    self.target_letters = new_target_letters

                    self.target = self.target.translate(str.maketrans(to_be_replaced,to_replace))
                                                        
                    if new_target_letters != old_target_letters or self.target[4] != old_letter_at_centre: ##############################
                        self.solutions = self._solve_target()
                    else:
                        print('The solutions are not changed.')
                    return
        print('The target was not changed.')

           
