if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    # print(type(student_marks))
    # print(student_marks)
    marks = student_marks[query_name]
    avg = 0
    holder = 0
    for i in marks:
        avg += i
        holder += 1
    result = avg / holder
    print(f'{result:.2f}')

    # Line 1- 8 given. Two forms input, dictionary and specific key desired. 
    # Determine specific mark 

    if __name__ == '__main__':
        n = int(input())
        student_marks = {}
        for _ in range(n):
            name, *line = input().split()
            scores = list(map(float, line))
            student_marks[name] = scores
        query_name = input()
        
        # print(type(student_marks))
        # print(student_marks)
        marks = student_marks[query_name]
        # avg = 0
        # holder = 0
        # for i in marks:
        #     avg += i
        #     holder += 1
        # result = avg / holder
        # print(f'{result:.2f}')
        avg = sum(marks) / len(marks)
        print(f'{sum(marks) / len(marks):.2f}')