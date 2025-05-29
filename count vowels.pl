% Define vowels
vowel(a).
vowel(e).
vowel(i).
vowel(o).
vowel(u).

% Base case: empty list has 0 vowels
count_vowels([], 0).

% If head is a vowel, increment count
count_vowels([H|T], Count) :-
    vowel(H),
    count_vowels(T, Rest),
    Count is Rest + 1.

% If head is not a vowel, skip it
count_vowels([H|T], Count) :-
    \+ vowel(H),
    count_vowels(T, Count).

% output:
?- count_vowels([h, e, l, l, o], Count).
Count = 2.

?- count_vowels([p, r, o, l, o, g], Count).
Count = 2.

?- count_vowels([], Count).
Count = 0.
