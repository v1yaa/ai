fruit(apple, red).
fruit(banana, yellow).
fruit(grape, purple).
fruit(orange, orange).
fruit(kiwi, green).
fruit(apple, green).

% output:
?- fruit(F, C).
F = apple,
C = red ;
F = banana,
C = yellow ;
F = grape,
C = purple ;
F = C,
C = orange ;
F = kiwi,
C = green ;
F = apple,
C = green ;
