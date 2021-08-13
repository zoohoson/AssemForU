from django.db import models
import pandas as pd
import pickle


# Create your models here.


class Model(models.Model):
    b19 = pd.read_csv('naSearch/data/bill_19.csv')
    b20 = pd.read_csv('naSearch/data/bill_20.csv')
    b21 = pd.read_csv('naSearch/data/bill_21.csv')
    bill_data = pd.concat([b19, b20, b21], axis=0).reset_index(drop=True)

    pconf19 = pd.read_csv('naSearch/data/plenary_session_19.csv')
    pconf20 = pd.read_csv('naSearch/data/plenary_session_20.csv')
    pconf21 = pd.read_csv('naSearch/data/plenary_session_21.csv')
    conf19 = pd.read_csv('naSearch/data/standing_committee_19.csv')
    conf20 = pd.read_csv('naSearch/data/standing_committee_20.csv')
    conf21 = pd.read_csv('naSearch/data/standing_committee_21.csv')
    subconf19 = pd.read_csv('naSearch/data/subcommittee_19.csv')
    subconf20 = pd.read_csv('naSearch/data/subcommittee_20.csv')
    subconf21 = pd.read_csv('naSearch/data/subcommittee_21.csv')
    conf_data = pd.concat([pconf19, pconf20, pconf21,
                           conf19, conf20, conf21, 
                           subconf19, subconf20, subconf21]).reset_index(drop=True)
    
    # brid19 = pd.read_csv()
    # brid20 = pd.read_csv()
    # brid21 = pd.read_csv()
    # bridge_data = pd.concat([brid19, brid20, brid21]).reset_index(drop=True)

    with open('naSearch/data/keyword_dic.pkl', 'rb') as f:
        keyword_dic = pickle.load(f)