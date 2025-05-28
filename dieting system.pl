diet(sugar, oats).
diet(sugar, leafy_greens).
diet(sugar, nuts).

diet(bp, banana).
diet(bp, dark_chocolate).
diet(bp, beetroot).

diet(obesity, apple).
diet(obesity, cucumber).
diet(obesity, lentils).
suggest_diet(Disease, Food) :- diet(Disease, Food).
all_diets(Disease, List) :- findall(Food, diet(Disease, Food), List).
