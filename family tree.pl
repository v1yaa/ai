% Facts
male(john).
male(paul).
male(david).
female(mary).
female(linda).

parent(john, paul).     % John is the parent of Paul
parent(mary, paul).     % Mary is the parent of Paul
parent(john, linda).
parent(mary, linda).
parent(paul, david).
parent(linda, david).

% Rules
father(X, Y) :- male(X), parent(X, Y).
mother(X, Y) :- female(X), parent(X, Y).
sibling(X, Y) :- parent(Z, X), parent(Z, Y), X \= Y.
grandparent(X, Y) :- parent(X, Z), parent(Z, Y).

% output:
?- father(john, paul).        
true
?- mother(mary, linda).       
true
?- sibling(paul, linda).      
true
?- grandparent(john, david).  
true
