import time
import random

def menu():
    print()
    print("=======================<<< 타자연습게임 >>>=========================")
    print()
    print("1.단어",'\t',end="")
    print("2.문장"'\t',end="")
    print("3.단어 게임\t",end="")
    print("4.종료하기\t",end="")
    print()
    print("====================================================================")

def start_game():
    num = int(input("원하는 번호를 입력하세요: "))
    if num == 1:
        word()
        start_game()
    elif num == 2:
        sentence()
        start_game()
    elif num == 3:
        word_game()
        start_game()
    elif num == 4:
        print("타자연습게임을 종료합니다.")
    else:
        print("다시 입력하세요")

def word():
    lan = input("언어를 선택하세요(한글/영어): ")
    if lan == "한글":
        kor_word()
    elif lan == "영어":
        eng_word()
    else:
        print("다시 입력하세요")
        word()

def kor_word():
    correct = 0
    wrong = 0

    word_list_k = ["강아지","고양이","사랑","우정","미소","다혜","수용","진아","상명","파이썬","알고리즘","게임","노트북","한소희","정우성","갯마을","스타벅스","커피","신촌","크리스마스","할로윈"]

    randlist = random.sample(word_list_k,10)

    start= time.time()

    for i in range(10):
        
        print(randlist[i],end = " : ")
        user = input()
        if user == randlist[i]:
            correct+= 1
        else:
            wrong += 1
        
    end = time.time()
    et = end-start
    et=format(et,".2f")
    print("맞은 개수: %d, 틀린 개수: %d" %(correct,wrong))
    print("정확도: %d%%" %(correct*10))
    print("걸린 시간: %s 초" %et)

    
def eng_word():
    correct=0
    wrong=0
    word_list_e = ["dog","cat","love","friendship","miso","dahye","sooyong","jina","sangmyeong","python","algorithm","game","notebook",
                   "sohee","oosung","gotcha","starbucks","coffee","shinchon","christmas","halloween"]
    randlist = random.sample(word_list_e,10)

    start= time.time()

    for i in range(10):
        
        print(randlist[i],end = " ")
        user = input()
        if user == randlist[i]:
            correct+= 1
        else:
            wrong += 1
    end = time.time()
    et = end-start
    et=format(et,".2f")
    print("맞은 개수: %d, 틀린 개수: %d" %(correct,wrong))
    print("정확도: %d%%" %(correct*10))
    print("걸린 시간: %s 초" %et)

def sentence():
    lan = input("언어를 선택하세요(한글/영어): ")
    if lan == "한글":
        k_sentence()
    elif lan == "영어":
        e_sentence()
    else:
        print("다시 입력하세요")
        sentence()

def k_sentence():
    print("<문장 연습>\n연습파일 번호를 선택하세요\n1.아이유 - 내 손을 잡아\n2.거북이 - 빙고\n3.태연 - why")
    num = int(input("번호: "))
    if num == 1:
        f = open("iu.txt","rt",encoding = "utf-8")
    elif num == 2:
        f = open("bingo.txt","rt",encoding = "utf-8")
    elif num == 3:
        f = open("why.txt","rt",encoding = "utf-8")
    else:
        print("파일이 없습니다. 다시 선택하세요.")
        sentence()   
    l1 = f.readlines()
    l2 = []
    for i in l1:
        l2.append(i[:-1])

    start=time.time()
    for i in range(len(l2)):
        print("*문제",i+1)
        user=input(l2[i]+"\n")
        if user == l2[i]:
            print("정답")
        else:
            print("오답")
    end = time.time()
    et = end-start
    et=format(et,".2f")
    
    print("걸린 시간: %s 초" %et)
       
def e_sentence():
    print("<문장 연습>\n연습파일 번호를 선택하세요\n1.WHAM! - Last Christmas\n2.Mariah Carey - All I Want for Christmas Is You\n3.Ariana Grande - Santa Tell Me")
    num = int(input("번호: "))
    if num == 1:
        f = open("LC.txt","rt",encoding = "utf-8")
    elif num == 2:
        f = open("All.txt","rt",encoding = "utf-8")
    elif num == 3:
        f = open("STM.txt","rt",encoding = "utf-8")
    else:
        print("파일이 없습니다. 다시 선택하세요.")
        sentence()   
    l1 = f.readlines()
    l2 = []
    for i in l1:
        l2.append(i[:-1])

    start=time.time()
    for i in range(len(l2)):
        print("*문제",i+1)
        user=input(l2[i]+"\n")
        if user == l2[i]:
            print("정답")
        else:
            print("오답")
    end = time.time()
    et = end-start
    et=format(et,".2f")
    
    print("걸린 시간: %s 초" %et)

def word_game():
    lan = input("언어를 선택하세요(한글/영어): ")
    if lan == "한글":
        word_game_k()
    elif lan == "영어":
        word_game_e()
    else:
        print("다시 입력하세요")
        word_game()

def word_game_k():
    count = 0
    word_list_k = ["강아지","고양이","사랑","우정","미소","다혜","수용","진아","상명","파이썬","떡볶이","게임","노트북","한소희","정우성","갯마을","수능","커피","신촌","상명대","할로윈"]

    randlist = random.sample(word_list_k,16)

    for i in range(16):
        print("|%7s \t|"%randlist[i],end = " ")
        if i%4 == 3:
            print('\n')

    start= time.time()

    while True:
        user = input("단어를 입력하세요 : ")
        for j in range(16):
            if user == randlist[j]:
                randlist[j] = ""
                count+=1

        for i in range(16):
            print("|%7s \t|"%randlist[i],end = " ")
            if i%4 == 3:
                print('\n')
    
        if count==16:
            end = time.time()
            et = end-start
            et=format(et,".2f")
            print("게임이 종료됩니다")
            print("걸린 시간: %s초" %et)
            break
        
def word_game_e():
    count = 0
    word_list_e = ["dog","cat","love","friendship","miso","dahye","sooyong","jina","sangmyeong","python","algorithm","game","notebook",
                   "sohee","oosung","gotcha","starbucks","coffee","shinchon","christmas","halloween"]
    
    randlist = random.sample(word_list_e,16)

    for i in range(16):
        print("|%10s"%randlist[i],end = " ")
        if i%4 == 3:
            print('|\n')

    start= time.time()

    while True:
        
        user = input("단어를 입력하세요 : ")

        for j in range(16):
            if user == randlist[j]:
                randlist[j] = ""
                count+=1
                
        for i in range(16):
            print("|%10s"%randlist[i],end = " ")
            if i%4 == 3:
                print('|\n')

        if count==16:
            end = time.time()
            et = end-start
            et=format(et,".2f")
            print("게임이 종료됩니다")
            print("걸린 시간: %s초" %et)
            break   
menu()
start_game()

