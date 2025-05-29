can_fly(sparrow).
can_fly(eagle).
can_fly(pigeon).

cannot_fly(ostrich).
cannot_fly(penguin).
cannot_fly(kiwi).

bird_flight(Bird) :-
    can_fly(Bird),
    format('~w can fly.~n', [Bird]).

bird_flight(Bird) :-
    cannot_fly(Bird),
    format('~w cannot fly.~n', [Bird]).

% output:
?- bird_flight(sparrow).
sparrow can fly.
?- bird_flight(penguin).
penguin cannot fly.
