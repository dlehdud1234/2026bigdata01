import ticket
ages = list()
age = 0;

humans = int(input("인원 : "))

for i in range(humans):
    age = int(input("나이 : "))
    ages.append(age)

print(f"총 요금 {ticket.Entrance_Fee(ages)}원 입니다")
#print(ages)