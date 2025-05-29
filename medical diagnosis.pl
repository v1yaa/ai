disease(flu) :-
    has(fever),
    has(cough),
    has(body_ache).

disease(cold) :-
    has(sneezing),
    has(runny_nose),
    has(cough).

disease(malaria) :-
    has(fever),
    has(chills),
    has(sweating).

% output:
?- assert(has(fever)).
?- assert(has(cough)).
?- assert(has(body_ache)).

?- disease(D).
D = flu 
