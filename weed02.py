scores = [100, 60 , 30, 10]
hap = 0
count = 0
for score in scores:
    hap = hap + score
    count +=  1

average = hap / count
print(average)
