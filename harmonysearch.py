#coding: utf-8

import random as _r_
from sudoku_classes import Solution, Grid





class HarmonyMemory(object):
    
    def __init__(self, problem, memory_size):
        self.problem = problem
        self.memory_size = memory_size
        self.memory = [self.rand_solu(problem) for x in range(memory_size)]
        self.memory = [(s, s.evaluate()) for s in self.memory]
        self.update()
    
    def __repr__(self):
        return str(self.memory)
        
    def update(self):
        self.memory.sort(key=lambda x: x[1])
        self.memory = self.memory[:self.memory_size]

    def rand_solu(self, problem):
        return Solution([_r_.choice(x) for x in self.problem])
        
    def memory_consideration(self, square):
        return _r_.choice([h[0].numbers[square] for h in self.memory])
        
    


def random_selection(boundaries):
    return _r_.choice(boundaries)


def pitch_adjustment(square, boundaries):
    
    





def insert_to_memory(harmony, hm):
    score = harmony.evaluate()
    if score < hm[-1][1]:
        hm.insert()
        hm.sort(key=lambda x: x[1])
        hm  = hm[:-1]
    else:
        return None



def improvise(HM, HCR, problem, PAR):
    new_harmony = [{}, 0] # Empty non-rated harmony.
    for square in problem: # For (x, y) on Sudoku board.
        if _r_.random() <= HCR: # Considering HM.
            n = _r_.randint(0, len(HM)-1) # Decides number for assignment.
            new_harmony[0][key] = HM[n][0][key] # Assignment.
        else: # Not considering HM.
            if _r_.random() <= PAR: # Considering PA.
                i = problem[0][key][1].index(HM[0][0][key])-1 # Index find.
                new_harmony[0][key] = problem[0][key][1][i] # Assignment.
            else: # Not considering PA = random.
                new_harmony[0][key] = _r_.choice(problem[0][key][1])
    evaluate_harmony(new_harmony) # Evaluate harmony score.
    return new_harmony
    



def HM_add(HM, harmony):
    for h in HM:
        if harmony[1] > h[1]:
            HM.insert(HM.index(h), harmony)
            HM.pop(len(HM)-1)
            break
            


def load_problem(problem_name="veryeasy1", heuristic=True):
    '''Loads a puzzle from the Problem folder.'''

    result = []
    with open("Problems/" + problem_name) as f:
        for line in f:
            result += [int(n) for n in line.rstrip().split("\t")]
    
    return result