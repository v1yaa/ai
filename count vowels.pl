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
