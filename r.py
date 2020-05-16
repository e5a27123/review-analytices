data = []
count = 0
datalen = 0
with open('reviews.txt', 'r') as f:
    for line in f:
        data.append(line)
        datalen = len(data[count]) + datalen
        count += 1
        if count % 1000 == 0:
            print(len(data))
print(data[0])
datalen = datalen / len(data)
print('平均是', datalen)