teacher(smith, math, m101).
teacher(jones, physics, p102).

student(john, math).
student(alice, physics).

student_teacher(Student, Teacher) :-
    student(Student, Subject),
    teacher(Teacher, Subject, _).

student_code(Student, Code) :-
    student(Student, Subject),
    teacher(_, Subject, Code).
