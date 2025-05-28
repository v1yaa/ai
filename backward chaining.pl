% Declare dynamic predicate
:- dynamic(fact/1).

% Facts
fact(sun_is_shining).
fact(has_sunscreen).

% Rules
rule(can_go_to_beach, [sun_is_shining, has_sunscreen]).
rule(is_happy, [can_go_to_beach]).

% Backward chaining: prove/1 succeeds if all goals in rule body can be proven
prove(X) :- fact(X).
prove(X) :- rule(X, Conditions), prove_all(Conditions).

% Prove all elements in a list
prove_all([]).
prove_all([H|T]) :- prove(H), prove_all(T).
