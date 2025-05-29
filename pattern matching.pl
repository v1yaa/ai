% match(Pattern, List) is true if Pattern matches the start of List

% Empty pattern matches any list
match([], _).

% Match head of pattern and list, then recurse on tail
match([H|TP], [H|TL]) :-
    match(TP, TL).

% output:
?- match([a, b], [a, b, c, d]).
true.

?- match([x, y], [x, y, z]).
true.

?- match([x, y], [x, z, y]).
false.
