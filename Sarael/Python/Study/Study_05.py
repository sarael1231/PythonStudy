from random import *

class Study_05_Package :
    def PythonList(self) :
        count = int(random() * 10) + 5
        numbers = []

        for num in range(count) :
            numbers.append(randint(10, 100))

        numbers.insert(0, 1)
        print(numbers)

        numbers.sort()
        print(numbers)

        numbers.reverse()
        print(numbers)

        shuffle(numbers)
        print(numbers)

        print(sample(numbers, 1))

        print(1 in numbers)

        mix_list = ["test", True]
        numbers.extend(mix_list)
        print(numbers)

    def PythonDictionary(self) :
        my_dic = {1:"test1", 3:"test3"}
        print(my_dic[1])

        print(my_dic.items())
        print(my_dic.values())

        # print(my_dic[5]) #error
        print(my_dic.get(5, "없음"))

        print(3 in my_dic)
        print(5 in my_dic)

        my_dic[2] = "test2"
        print(my_dic)

        del my_dic[2]
        print(my_dic)

    def PythonTuple(self) :
        #내용변경, 추가 안되나 속도가 빠름
        my_tuple = ("test1", "test3")

        #name = "name"
        #age = 20
        #hobby = "hobby"

        name, age, hobby = "name", 20, "hobby"
        # == (name, age, hobby) = ("name", 20, "hobby")
        print(name, age, hobby)

        name = "test"
        print(name, age, hobby)

    def PythonSet(self) :
        # 중복 안됨, 순서 없음

        my_set = {1,2,3,3,3}
        print(my_set)

        # set 선언
        java = {"유재석", "김태호", "양세형"}
        python = set(["유재석", "박명수"])

        print(java & python) # print(java.intersection(python))
        print(java | python) # print(java.union(python))
        print(java - python) # print(java.difference(python))

    def PythonConversion(self) :
        menu = {"커피", "우유", "주스"}
        print(menu, type(menu))

        menu = list(menu)
        print(menu, type(menu))

        menu = tuple(menu)
        print(menu, type(menu))

        menu = set(menu)
        print(menu, type(menu))

    def Study4344(self) :
        # 문제
        # 대학생 새내기들의 90%는 자신이 반에서 평균은 넘는다고 생각한다. 
        # 당신은 그들에게 슬픈 진실을 알려줘야 한다.

        # 입력
        # 첫째 줄에는 테스트 케이스의 개수 C가 주어진다.
        # 둘째 줄부터 각 테스트 케이스마다 학생의 수 N(1 ≤ N ≤ 1000, N은 정수)이 
        # 첫 수로 주어지고, 이어서 N명의 점수가 주어진다.
        # 점수는 0보다 크거나 같고, 100보다 작거나 같은 정수이다.
        # -> 학생의 수 N(1 ≤ N ≤ 10, N은 정수)으로 랜덤하게 점수도 같이 생성되게 수정

        count = int(input("테스트 횟수를 입력하세요(1 ~ 10) : "))
        test_score = []

        for i in range(count) :
            student_num = randint(1, 10)
            score_list = []

            for j in range(student_num) :
                score_list.append(randint(0, 100))

            print(student_num, score_list)
            test_score.append(score_list)

        print()

        for i in test_score:
            sum_score = 0
            for j in i:
                sum_score += j

            avg = sum_score / len(i)
            pass_count = 0;
            for j in i:
                if avg <= j :
                    pass_count += 1

            print(format((pass_count / len(i)) * 100, ".3f") + "%")

        print()

    def Study8958(self) :
        # 문제
        # "OOXXOXXOOO"와 같은 OX퀴즈의 결과가 있다. 
        # O는 문제를 맞은 것이고, X는 문제를 틀린 것이다. 
        # 문제를 맞은 경우 그 문제의 점수는 그 문제까지 연속된 O의 개수가 된다. 
        # 예를 들어, 10번 문제의 점수는 3이 된다.
        # "OOXXOXXOOO"의 점수는 1+2+0+0+1+0+0+1+2+3 = 10점이다.
        # OX퀴즈의 결과가 주어졌을 때, 점수를 구하는 프로그램을 작성하시오.

        # 입력
        # 첫째 줄에 테스트 케이스의 개수가 주어진다. 
        # 각 테스트 케이스는 한 줄로 이루어져 있고, 
        # 길이가 0보다 크고 80보다 작은 문자열이 주어진다. 
        # 문자열은 O와 X만으로 이루어져 있다.
        # ->랜덤으로 케이스 개수만큼 OX생성(5 ≤ N ≤ 20, N은 정수)

        count = int(input("OX퀴즈 횟수를 입력하세요(1 ~ 10) : "))
        test_score = []

        for i in range(count) :
            student_num = randint(5, 20)
            score_list = []

            for j in range(student_num) :
                if randint(0, 1) == 0 :
                    score_list.append("X");
                else :
                    score_list.append("O");

            print(student_num, score_list)
            test_score.append(score_list)

        print()

        for i in test_score:
            sum_score = 0
            cur_score = 0

            for j in i:
                if j == "O" :
                    cur_score += 1
                    sum_score += cur_score
                else :
                    cur_score = 0

            print(sum_score)

        print()

    def Study1546(self) :
        # 문제
        # 세준이는 기말고사를 망쳤다. 
        # 세준이는 점수를 조작해서 집에 가져가기로 했다. 
        # 일단 세준이는 자기 점수 중에 최댓값을 골랐다. 
        # 이 값을 M이라고 한다. 그리고 나서 모든 점수를 점수/M*100으로 고쳤다.
        # 예를 들어, 세준이의 최고점이 70이고, 수학점수가 50이었으면 수학점수는 50/70*100이 되어 71.43점이 된다.
        # 세준이의 성적을 위의 방법대로 새로 계산했을 때, 새로운 평균을 구하는 프로그램을 작성하시오.

        count = int(input("테스트 횟수를 입력하세요(1 ~ 10) : "))
        test_score = []

        for i in range(count) :
            test_score.append(randint(0, 100))

        test_score.sort()
        test_score.reverse()
        max = test_score[0]
        print(test_score, "\n")

        sum_score = 0
        for i in test_score :
            score = i / max * 100
            sum_score += float(format(score, ".2f"))
            print(i, format(score, ".2f"))

        print("\n평균 :", format(sum_score / len(test_score), ".2f"))
