def PythonFor() :
    # 한줄 for
    students = list(range(5))
    print(students)

    students = [i+100 for i in students]
    print(students)

    students2 = ["Iron man", "Thor", "I am groot"]
    students2 = [len(i) for i in students2]
    print(students2)

    students3 = ["Iron man", "Thor", "I am groot"]
    students3 = [i.upper() for i in students3]
    print(students3)

    scores = {"수학": 0, "영어": 50, "코딩":100}
    for subject, score in scores.items() :
        print(subject.ljust(8), str(score).rjust(4), sep=":")

def Study15552() :
    # 문제
    # 본격적으로 for문 문제를 풀기 전에 주의해야 할 점이 있다. 
    # 입출력 방식이 느리면 여러 줄을 입력받거나 출력할 때 
    # 시간초과가 날 수 있다는 점이다.
    # Python을 사용하고 있다면, input 대신 sys.stdin.readline을 사용할 수 있다. 
    # 단, 이때는 맨 끝의 개행문자까지 같이 입력받기 때문에 문자열을 저장하고 싶을 경우 
    # .rstrip()을 추가로 해 주는 것이 좋다.
    # 또한 입력과 출력 스트림은 별개이므로, 
    # 테스트케이스를 전부 입력받아서 저장한 뒤 전부 출력할 필요는 없다. 
    # 테스트케이스를 하나 받은 뒤 하나 출력해도 된다.

    import sys

    count = int(input("반복할 횟수를 적어 주세요 : "))

    for i in range(count) : # for i in range(1, count+1)
        a, b = map(int, sys.stdin.readline().split())
        print(a+b)

    # 리스트로 저장할 때
    # data = list(map(int,sys.stdin.readline().split()))

    # 문자열 n줄을 입력받아 리스트에 저장할 때
    # data = [sys.stdin.readline().strip() for i in range(n)]