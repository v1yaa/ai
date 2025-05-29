planet(mercury, 0, no).
planet(venus, 0, yes).
planet(earth, 1, yes).
planet(mars, 2, yes).
planet(jupiter, 79, yes).
planet(saturn, 82, yes).
planet(uranus, 27, yes).
planet(neptune, 14, yes).
has_atmosphere(P) :- planet(P, _, yes).
many_moons(P, N) :- planet(P, M, _), M > N.

% output:
?- many_moons(P, 10).
P = jupiter ;
P = saturn ;
P = uranus ;
P = neptune.
