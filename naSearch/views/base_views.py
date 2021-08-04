from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
# from ..models import ?


def main_page(request):
    """
    main 화면
    """
    return render(request, 'naSearch/main_page.html')


def index(request):
    """
    bill 목록 출력
    """
    bill_list = [1, 2, 3, 4, 5, 6, 1, 1, 1, 1, 1, 1, 5, 6, 1, 1, 1, 1, 1, 1] # ?.objects.order_by('-create_date')
    context = {'bill_list': bill_list}
    return render(request, 'naSearch/bill_list.html', context)
