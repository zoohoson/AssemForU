from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from ..models import Answer


# from ..models import ?


def index(request):
    """
    bill 목록 출력
    """

    query_search = request.GET.get('query', '')

    if query_search:
        print(query_search)
        Answer.Get_similarity(query_search)

    #page = request.GET.get('page', '1')
    #paginator = Paginator(bill_list,10)
    #page_obj = paginator.get_page(page)
    #context = {'bill_list',page_obj}

        bill_list = Answer()

        context = {'bill_list' : bill_list}
        return render(request, 'naSearch/bill_list.html', context)
    else :
        return render(request,'naSearch/bill_list.html',{'bill_list': None})