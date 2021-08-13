from django.db import models
import pandas as pd
import pickle


# Create your models here.


class Model(models.Model):
    bill_data = pd.read_csv('naSearch/data/bill_21.csv')
    with open('naSearch/data/keyword_dic.pkl', 'rb') as f:
        keyword_dic = pickle.load(f)