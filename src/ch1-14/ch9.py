from logos.logo import logo_auction

print(logo_auction)

def start_auction():
    print("경매프로그램에 오신것을 환영합니다. !!")
    biz_users = {}
    isDone = False
    while not isDone:
        name = input("입찰자 이름을 말씀해주세요 : ")
        biz  = int(input("입찰 가격은 얼마입니까? : $"))
        biz_users[name]=biz
        if input("다른 참여자가 있습니까? 예/아니오 : ") == "아니오":
            break
    
    biz_amount_tmp = 0
    for key in biz_users:
        biz_amount = biz_users[key]
        if biz_amount > biz_amount_tmp:
            biz_amount_tmp = biz_amount
            user_tmp = key
    
    print(f"{user_tmp}가 ${biz_amount_tmp} 로 낙찰 받으셨습니다.")


        
start_auction()