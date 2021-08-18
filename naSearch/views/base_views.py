from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from gensim.models import FastText
from ..models import Model


model_name = 'naSearch/data/hannanum_Fasttext.model'
model = FastText.load(model_name)


def main_page(request):
    """
    main Page
    """
    query_search = request.GET.get('query', '')
    if query_search:
        print('main', query_search)
        return render(request, 'naSearch/bill_list.html', query_search)
    else:
        return render(request, 'naSearch/main_page.html')


def detail(request, bill_no):
    data = Model.bill_data
    # b_data = Model.birdge_data
    con_data = Model.conf_data
    """
    bill info
    """
    # bill = get_object_or_404(data.bill_no, pk=bill_no)  # param1이 models객체여야 하는데...
    bill = data[data['bill_no'] == bill_no][['bill_name', 'propose_date', 'proposers', 'content']].values
    
    # con_no_lst = b_data[b_data['bill_no']==bill_no].confer_num.values
    # bill_con_birdge = pd.DataFrame([[_] for _ in con_no_lst], columns=['confer_num'])
    # con = con_data.merge(bill_con_bridge, how='inner').content.values

    context = {'bill': bill[0], 'conf': ''}  # only content
    return render(request, 'naSearch/bill_info.html', context)


def Get_similarity(query):
    data = Model.bill_data
    # Keyword extracting through "Word Summarization by graph algorithm"  -> Must Check Paper, Accuracy !!
    keyword_dic = Model.keyword_dic

    # similarity : key = token of document, value = similarity between qudry and key
    similarity = dict()
    for key in keyword_dic.keys():
        if key in model.wv.vocab:
            similarity[key] = model.wv.similarity(query,key)

    # Sorting token by high similarity with query
    result = sorted(similarity.items(),key=lambda x: x[1], reverse=True)[:20]
    
    # bill_list : key = id of bill, value = [sum of simmilarity, count] of bill (same mean, document)
    bill_list = dict()
    max_v = 0
    for key, value in result:
        bill = keyword_dic[key]
        for billno in bill:
            if billno in bill_list.keys():
                tmp = bill_list[billno]
                tmp[1] += 1
                tmp[0] = value + tmp[0]
                if (max_v < tmp[1]): max_v = tmp[1]
            else :
                v = [value, 1]
                bill_list[billno] = v

    # output : key = id of bill, value = (count, average of similarity) of bill
    output = dict()
    for key in bill_list.keys():
        v = bill_list[key]
        avg = v[0] / max_v  # max_v 는 모든 의안 통틀어서 같은 값?
        value = (v[1], avg)
        output[key] = value

    # Sorting bill by high (count, average of similarity) of bill with query
    output = sorted(output.items(), key=lambda x: (-x[1][0], -x[1][1]))

    # res는 아래 코드의 list 참고
    res = []
    for idx, key in enumerate(output):
        bill_no = key[0]
        bill = data[data['bill_no'] == bill_no]
        bill_name = bill['bill_name'].values
        bill_agency = bill['proposers'].values
        # print(bill_agency)
        bill_comm = 'null'  # bill['committee'].values
        bill_date = bill['propose_date'].values
        bill_keyword = ['하이데브', '파이팅', 'BISlab짱']

        similarity = round(key[1][1], 2)
        lst = [str(idx+1) + '(' + str(similarity) + ')',
        bill_no, bill_name, bill_agency, bill_comm, bill_date, bill_keyword]
        res.append(lst)

    print(len(res))
    return res


def index(request):
    """
    bill 목록 출력
    """
    query_search = request.GET.get('query', '')
    page = request.GET.get('page','')
    print(query_search, page)
    if query_search :
        bill_list = Get_similarity(query_search)
        if page == '': page = request.GET.get('page', '1')
        paginator = Paginator(bill_list, 10)
        page_obj = paginator.get_page(page)
        print(page_obj.number)
        context = {'bill_list' : page_obj, 'query': query_search}
        return render(request, 'naSearch/bill_list.html', context)

    else :
        return render(request,'naSearch/bill_list.html',{'bill_list': None})