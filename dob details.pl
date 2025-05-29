person('Alice', dob(12, may, 1995)).
person('Bob', dob(23, june, 1990)).
person('Charlie', dob(5, december, 1985)).
person('Diana', dob(29, february, 2000)).
person('Eve', dob(10, october, 1998)).

% output:
?- person(Name, DOB).
Name = 'Alice',
DOB = dob(12, may, 1995) ;
Name = 'Bob',
DOB = dob(23, june, 1990) ;
Name = 'Charlie',
DOB = dob(5, december, 1985) ;
Name = 'Diana',
DOB = dob(29, february, 2000) ;
Name = 'Eve',
DOB = dob(10, october, 1998).
