###### 숫자 맞추기 게임 ######

import random

print("10번만에 랜덤 숫자 맞추기 게임")

random_number = random.randint(1,100) ## ★ 1부터 100사이의 랜덤한 숫자 생성
try_number = 0 #시도횟수 초기세팅값
max_try_number = 10 # 시도 최고횟수

while True: ## ★ 숫자를 맞추거나 게임을 종료할 때까지 반복
    
    try_number += 1    
    
    try:
        print("숫자를 입력하세요")
        number = input("1부터 100까지 숫자 중 하나를 입력하세요: ")
        player_number = int(number)
        
        if player_number == random_number:
            print(f">> 컴퓨터 숫자 : {random_number} / 플레이어 숫자 : {player_number}")
            print(f"정답! {try_number}번 만에 컴퓨터의 숫자를 맞추셨습니다!") ## ★ 시도한 횟수 출력
            break
        
        elif 0 > player_number > 101:
            print("범위를 벗어난 숫자입니다. 다시 입력하세요!") ## ★ 범위를 벗어난 숫자 경고
            
        elif max_try_number == try_number:
            print("모든 기회를 소진하셨습니다. Game Over")
            break
        
        else:
            print("땡! 다시 시도하시겠습니까? (Y/N)") ## ★ 재시작 여부
            answer = input("다시 시도하려면 Y, 종료하려면 N 또는 아무 글자나 입력하세요: ").lower() 
            
            if answer == "y":
                print(f"남은 시도 횟수 : {max_try_number-try_number} 번")
                print("Hint: Down") if player_number > random_number else print("Hint: Up") ## ★ 업/다운 힌트
                continue
            else:
                print("취소를 선택하셨습니다 : Game Over")
                break
    
    except ValueError:
        print(f"'{number}'은 숫자가 아닙니다. 다시 입력해주세요")
        continue
    
    except Exception as e:
        print(f"잘못된 형식입니다. error : {e}")
        continue

print("게임을 종료합니다! 또 만나요.")