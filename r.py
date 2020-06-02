import time
import progressbar

data = []
count = 0

bar = progressbar.ProgressBar(max_value=1000000)
with open('reviews.txt', 'r') as f:
    for line in f:
        data.append(line)
        count += 1
        bar.update(count)
print('檔案讀取完成,總共有', len(data), '筆資料')

datalen = 0
for d in data:
    datalen = datalen + len(d)
print('留言平均長度是', datalen/len(data))

new = []
for d in data:
    if len(d) < 100:
        new.append(d)
print('一共有', len(new), '比留言長度小於100')

#good = []
#for d in data:
#    if 'good' in d:
#        good.append(d)
good =[d for d in data if 'good' in d]
print('一共有', len(good), '比留言提到good')

#文字記數
start_time = time.time()
wc = {} #word_count
for d in data:
    words = d.split(' ')
    for word in words:
        if word in wc:
            wc[word] += 1
        else:
            wc[word] = 1
for word in wc:
    if wc[word] > 10000000:
        print(word, wc[word])
end_time = time.time()
print('花費', end_time - start_time, 'seconds')

print(len(wc))

while True:
    word = input('請問想查什麼字 : ')
    if word == 'q':
        break
    if word in wc:
        print(word , '出現次數為 : ', wc[word])
    else:
        print('這字沒出現過!')
print('感謝使用!')
    




