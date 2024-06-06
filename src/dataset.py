import json
import string
import random
all_data = []
letters_set = string.ascii_letters
for i in range(10):
    data = {'id' : i, 'conversations' : []}
    random_list = random.sample(letters_set,5)
    random_num = [random.randint(0,99) for _ in range(5)]
    for n,m in zip(random_list,random_num):
        new = [n,str(m)]
        data['conversations'].append(new)
    all_data.append(data)

with open('dataset.json','w') as f:
    json.dump(all_data,f,indent=2)