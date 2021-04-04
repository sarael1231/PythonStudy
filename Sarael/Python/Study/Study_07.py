class Study_07_Package :
    def PythonString(self) :
        #문자열 자르기
        jumin = "123456-1234567";

        print(jumin[7]);
        print(jumin[0:2]);
        print(jumin[2:4]);
        print(jumin[:6]);
        print(jumin[7:]);
        print(jumin[-7:]);

        #문자열 변환
        my_str = "Python is Amazing";

        print(my_str.lower());
        print(my_str.upper());
        print(my_str[0].isupper());
        print(len(my_str));
        print(my_str.replace("Python", "Jave"));

        index = my_str.index("n");
        print(index);
        index = my_str.index("n", index + 1);
        print(index);

        print(my_str.find("n"));

        print(my_str.find("Java")); # -1
        # print(my_str.index("Java")); # error

        print(my_str.count("n"));
        print(my_str[:my_str.index("n")]);

        print("Red Apple\rPine");
        print("Redd\bApple");
        print("Red\tApple");

    def Study1316(self) :
        # 문제
        # 그룹 단어란 단어에 존재하는 모든 문자에 대해서, 
        # 각 문자가 연속해서 나타나는 경우만을 말한다. 
        # 예를 들면, ccazzzzbb는 c, a, z, b가 모두 연속해서 나타나고, 
        # kin도 k, i, n이 연속해서 나타나기 때문에 그룹 단어이지만, 
        # aabbbccb는 b가 떨어져서 나타나기 때문에 그룹 단어가 아니다.
        # 단어 N개를 입력으로 받아 그룹 단어의 개수를 출력하는 프로그램을 작성하시오.

        import sys

        count = int(input("1 ≤ N ≤ 100, N은 정수 : "))
        data = [sys.stdin.readline().strip() for i in range(count)]
    
        groupword_count = 0
        for i in data :
            if self.__IsGroupWord(i) :
                groupword_count += 1

        print(f"그룹 단어 수 : {groupword_count}")

    def __IsGroupWord(self, data) :
        alphabet = []

        for i in data :
            if i in alphabet :
                if alphabet[0] != i :
                    return False
            else :
                alphabet.insert(0, i)

        return True
