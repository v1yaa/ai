% Define the edges
edge(a, b).
edge(a, c).
edge(b, d).
edge(c, e).
edge(d, goal).
edge(e, goal).

% Define heuristic values for nodes
heuristic(a, 5).
heuristic(b, 4).
heuristic(c, 2).
heuristic(d, 3).
heuristic(e, 1).
heuristic(goal, 0).

% Best First Search main predicate
best_first(Start, Goal, Path) :-
    bfs([[Start]], Goal, RevPath),
    reverse(RevPath, Path).

% Base case: goal found
bfs([[Goal|Rest]|_], Goal, [Goal|Rest]).

% Recursive case: expand and sort paths
bfs([[Node|Rest]|OtherPaths], Goal, Path) :-
    findall([Next,Node|Rest],
        (edge(Node, Next), \+ member(Next, [Node|Rest])),
        NewPaths),
    append(OtherPaths, NewPaths, AllPaths),
    sort_paths(AllPaths, Sorted),
    bfs(Sorted, Goal, Path).

% Sort paths by heuristic value of the head node
sort_paths(Paths, Sorted) :-
    map_list_to_pairs(get_hval, Paths, Pairs),
    keysort(Pairs, SortedPairs),
    pairs_values(SortedPairs, Sorted).

% Get heuristic of the first node in a path
get_hval([Node|_], H) :- heuristic(Node, H).

% output:
?- best_first(a, goal, Path).
Path = [a, c, e, goal].
