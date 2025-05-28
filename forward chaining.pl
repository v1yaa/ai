:- dynamic(fact/1).

% Initial facts
fact(a).
fact(b).

% Rules (new fact, [conditions])
rule(c, [a, b]).
rule(d, [b, c]).
rule(e, [c]).

% Forward chaining
forward_chaining :-
    infer_new_facts,
    list_all_facts.

infer_new_facts :-
    rule(NewFact, Conditions),
    \+ fact(NewFact),
    all_true(Conditions),
    assertz(fact(NewFact)),
    infer_new_facts.
infer_new_facts.

all_true([]).
all_true([H|T]) :- fact(H), all_true(T).

list_all_facts :-
    write('Inferred facts: '), nl,
    fact(X),
    write('- '), write(X), nl,
    fail.
list_all_facts.
