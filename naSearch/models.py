from django.db import models
import pandas as pd
import numpy as np
import gensim.models as g
# Create your models here.

data = pd.read_csv('naSearch/data/merge_naver_data.csv')
model_name = 'naSearch/data/word2vec_with_hannanum_3'
model = g.Doc2Vec.load(model_name)

class Answer(models.Model):

    def Get_similarity(query):
        keyword = data['keyword']  # keyword
        content = data['contents']  # content

        try:  # query 존재하는지 확인
            tmp = model.wv.most_similar(query, topn=10)
        except KeyError as e:
            return None  # KeyError 발생 시 none return ("관련된 법률안이 없습니다.")

        word = list()
        # sim = list()

        word = [tmp[i][0] for i in range(0, len(tmp))]  # query와 관련도 높은 상위 10개의 word 추출
        # sim.append(tmp[i][1])
        res = [keyword[j] for i in range(0, len(tmp)) for j in range(0, len(content)) if
            word[i] in content[j]]  # 관련된 법률안 추출

        return pd.unique(res).tolist()  # unique하되 순서 유지한 상태로 return
