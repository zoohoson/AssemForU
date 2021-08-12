from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from ..models import Answer

def main_page(request):
    """
    main Page
    """
    return render(request, 'naSearch/main_page.html')


def index(request):
    """
    bill List
    """
    query_search = request.GET.get('query', '')
    
    if query_search:
        print(query_search)
        Answer.Get_similarity(query_search)

        bill_list = Answer()

        context = {'bill_list' : bill_list}
        return render(request, 'naSearch/bill_list.html', context)
    else :
        return render(request,'naSearch/bill_list.html',{'bill_list': None})


def detail(request, bill_id):
    """
    bill info
    """
    # bill = get_object_or_404(bill_model, pk=bill_id)  # 없는 bill_id요청시 404에러 하고싶은데, bill_model필요하다

    bill = 1
    context = {'bill': bill}
    return render(request, 'naSearch/bill_info.html', context)
