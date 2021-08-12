from django.db import models
import pandas as pd
import numpy as np
from gensim.models import FastText
import pickle
import math

# Create your models here.

data = pd.read_csv('naSearch/data/bill_21.csv')
model_name = 'naSearch/data/hannanum_FastText.model'
model = FastText.load(model_name)
dic = dict()
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

        res = []
        print(output)

        for key in output:
            bill_no = key[0]
            bill = data[data['billno'] == bill_no]['billname'].values
            similarity = key[1][1]
            list = [bill_no,bill,similarity]
            res.append(list)

        Answer.result = res
