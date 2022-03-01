def form_teams(n, students):
    students.sort()        
    end = len(students) - 1
    s = 0
    for _ in range(n):  
        end -= 1    
        s += students[end]
        end -= 1
    return s      
                

Q = int(input())
for _ in range(Q):
    N = int(input())
    students = [int(n) for n in input().split(" ")]
    print(form_teams(N, students))

