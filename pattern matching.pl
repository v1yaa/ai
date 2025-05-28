% match(Pattern, List) is true if Pattern matches the start of List

% Empty pattern matches any list
match([], _).

% Match head of pattern and list, then recurse on tail
match([H|TP], [H|TL]) :-
    match(TP, TL).
