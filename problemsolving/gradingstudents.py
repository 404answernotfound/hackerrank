def gradingStudents(grades):
    # Write your code here
    # next multiple of 5, if grade - next multiple < 3, grade = next multiple
    _grades = []
    for grade in grades:
        if grade < 38:
            _grades.append(grade)
            continue
        sgrade = list(str(grade))
        if int(sgrade[1]) > 5:
            sgrade[1] = '0'
            sgrade[0] = str(int(sgrade[0]) + 1)
        else:
            sgrade[1] = '5'
            
        diff = int(''.join(sgrade)) - grade
        
        if diff < 3:
            _grades.append(int(''.join(sgrade)))
        else:
            _grades.append(grade)
    print(_grades)
    return _grades
            
gradingStudents([37, 91, 95, 99])