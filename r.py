#讀檔案
date = []
count = 0
with open('orginal.txt'，'r') as f:
    for line in f:
        date.append(line)
        count = count + 1
        if count % == 1000:
print(len(data))

print('檔案讀取玩了'，'總共有'，len(data)，'筆資料')

sum_len =0
for d in data:
	sum_len = sum_len + len(d)
print('平均留言長度'，sum_len/len(data))