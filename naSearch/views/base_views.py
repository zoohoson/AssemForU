from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
# from ..models import ?


def index(request):
    """
    bill 목록 출력
    """
    bill_list = [1, 2, 3, 4, 5, 6, 1, 1, 1, 1, 1, 1, 5, 6, 1, 1, 1, 1, 1, 1] # ?.objects.order_by('-create_date')
    context = {'bill_list': bill_list}
    return render(request, 'naSearch/bill_list.html', context)


def detail(request, bill_id):
    """
    bill info
    """
    bill = 1
    context = {'bill': bill}
    return render(request, 'naSearch/bill_info.html', context)