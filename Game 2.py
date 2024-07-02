from itertools import product
import random

count_draw = 0 # 무승부횟수 기록용
count_win = 0 # 승리횟수 기록용
count_lost = 0 # 패배횟수 기록용


# 계속 플레이할지 묻는 함수    
def retry_asking(): 
    while True:
        choice_try = input("다시 플레이하시겠습니까? (Y/N): ").lower()
        if choice_try == "y" or choice_try == "ㅛ":
            print("'계속 플레이'를 선택하셨습니다.")
            return True
        elif choice_try == "n" or choice_try == "ㅜ":
            print("'게임 종료'를 선택하셨습니다.")
            return False
        else:
            print("잘못된 답을 입력하셨습니다. 다시 입력해주세요.")
        


# 게임 진행 코드
while True:
    try:
        print("★ 가위바위보 게임을 시작합니다 ★") # 게임시작 안내문
        
        case = ["가위", "바위", "보"]
        
        random_num = random.randint(0, 2)  # 컴퓨터 랜덤 가위바위보 선정
        computer = case[random_num]
        player = input("가위, 바위, 보 중 하나를 선택하세요: ") # 플레이서 가위바위보 선정
        
        # 가위,바위,보 외에 다른 입력값이 들어왔을 때 경고문
        if player not in case:
            print("경고: 가위,바위,보 중 하나를 입력해주세요!")
            continue
        
        event = (player,computer) # (플레이어,컴퓨타) 결과 듀플로 묶기 -> 밑에 product가 생성한 경우의 수와 비교하기 위해
                
        for x, y in enumerate(product(case, case), 1): # 가위바위보 모든 경우의 수 생성
            if event == y:
                if x in [1,5,9]:
                    print(">>> 무승부입니다 <<<)")
                    print(f"(컴퓨터:{computer} / 플레이어:{player})")
                    count_draw += 1
                elif x in [3,4,8]:
                    print(">>> 이겼습니다!!! <<<")
                    print(f"(컴퓨터:{computer} / 플레이어:{player})")
                    count_win += 1
                else:
                    print(">>> 졌습니다ㅠㅠ <<<")
                    print(f"(컴퓨터:{computer} / 플레이어:{player})")
                    count_lost += 1
                    
        if retry_asking():
            continue
        else:
            print(f"[게임 전적] 승:{count_win} / 패:{count_lost} / 무승부:{count_draw} / 승률: {round(count_win/(count_win + count_lost + count_draw)*100,1)}%")
            print("게임을 종료합니다. 또 만나요!")
            break                    
    
    except ZeroDivisionError:
        print("게임 전적 없이 게임을 마칩니다.")
        break
    
    except Exception:
        print("예상치못한 에러가 생겼습니다. 다시 게임을 시작합니다!")
        continue
