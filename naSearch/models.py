from django.db import models
import pandas as pd
import numpy as np
from gensim.models import FastText
import pickle
import math

# Create your models here.

# data = pd.read_csv('naSearch/data/merge_naver_data.csv')
data = pd.read_csv('naSearch/data/bill_21.csv')
model_name = 'naSearch/data/hannanum_FastText.model'
model = FastText.load(model_name)
dic = dict()
#with open('naSearch/data/hannanum_token_dic_bill.txt', 'r', encoding='UTF-8') as f:
#    lines = f.readlines()
#for line in lines:
#    key, value = line.strip().split(':')
#    value = value.strip().split(',')
#    dic[int(key)] = value
with open('naSearch/data/keyword_dic.pkl','rb') as f:
    keyword_dic = pickle.load(f)

class Answer(models.Model):
    result = []

    def Get_similarity(query):
        similarity = dict()

        for key in keyword_dic.keys():
            if key in model.wv.vocab:
                similarity[key] = model.wv.similarity(query,key)

        result = sorted(similarity.items(),key=lambda x:x[1],reverse=True)[:20]
        bill_list = dict()
        max_v = 0
        for key,value in result:
            bill =keyword_dic[key]
            for billno in bill:
                if billno in bill_list.keys():
                    tmp = bill_list[billno]
                    tmp[1] += 1
                    tmp[0] = value +tmp[0]
                    if(max_v < tmp[1]) : max_v = tmp[1]
                else:
                    v = [value,1]
                    bill_list[billno] = v
        output = dict()

        for key in bill_list.keys():
            v = bill_list[key]
            avg = v[0]/max_v
            value = (v[1],avg)
            output[key] = value
        output = sorted(output.items(),key = lambda x:(-x[1][0],-x[1][1]))

        # keyword = data['keyword']  # keyword
        # content = data['contents']  # content

        #try:  # query 존재하는지 확인
        #    tmp = model.wv.most_similar(query, topn=10)
        #except KeyError as e:
        #    tmp = data[data['content'].str.contains(query,na=False)]
        #    return None  # KeyError 발생 시 none return ("관련된 법률안이 없습니다.")

        #score = dict()
        #for i in range(0, len(data)):
        #    key = data['billno'][i]

        #    if dic.get(int(key)):
        #        tokens = dic[int(key)]
        #        tmp = []

         #       for j in range(len(tokens)):
         #           try:
         #               if tokens[j] in model.wv.key_to_index:
         #                   tmp.append(model.wv.similarity(query, tokens[j]))
         #           except KeyError:
         #               pass
         #       if not tmp:
         #           tmp = 0
         #       else:
         #           tmp.sort(reverse=True)
         #           tmp = np.array(tmp[:10])
         #           tmp = round(tmp.mean(), 2)
         #       score[int(key)] = tmp


        #score = sorted(score.items(), key=lambda x: x[1], reverse=True)


        res = []
        print(output)

        for key in output:
            bill_no = key[0]
            bill = data[data['billno'] == bill_no]['billname'].values
            similarity = key[1][1]
            list = [bill_no,bill,similarity]
            res.append(list)

        Answer.result = res

        # word = list()
        # sim = list()

        # word = [tmp[i][0] for i in range(0, len(tmp))]  # query와 관련도 높은 상위 10개의 word 추출
        # sim.append(tmp[i][1])
        # res = [keyword[j] for i in range(0, len(tmp)) for j in range(0, len(content)) if
        #    word[i] in content[j]]  # 관련된 법률안 추출

        # return pd.unique(res).tolist()  # unique하되 순서 유지한 상태로 return
