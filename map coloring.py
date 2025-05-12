from typing import Dict, List
from copy import deepcopy

class CSP:
    def __init__(self, variables: List[str], domains: Dict[str, List[int]], constraints):
        self.variables = variables
        self.domains = domains
        self.constraints = constraints

    def solve(self):
        return self.backtrack({})

    def backtrack(self, assignments):
        if len(assignments) == len(self.variables):
            return assignments

        var = self.select_unassigned(assignments)
        for value in self.domains[var]:
            new_assignments = deepcopy(assignments)
            new_assignments[var] = value
            if self.is_consistent(new_assignments):
                result = self.backtrack(new_assignments)
                if result is not None:
                    return result
        return None

    def select_unassigned(self, assignments):
        for var in self.variables:
            if var not in assignments:
                return var

    def is_consistent(self, assignments):
        for (var1, var2) in self.constraints:
            if var1 in assignments and var2 in assignments:
                if assignments[var1] == assignments[var2]:
                    return False
        return True

def map_coloring():
    variables = ['A', 'B', 'C', 'D']
    domains = {var: [1, 2, 3] for var in variables}
    constraints = [
        ('A', 'B'),
        ('A', 'C'),
        ('B', 'C'),
        ('B', 'D'),
        ('C', 'D')
    ]

    csp = CSP(variables, domains, constraints)
    result = csp.solve()

    if result:
        print("Solution Exists: Following are the assigned colors")
        print(' '.join(str(result[var]) for var in variables))
    else:
        print("No solution found")

map_coloring()

