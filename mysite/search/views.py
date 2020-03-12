from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.shortcuts import render
from search import views as search_views

from wagtail.core.models import Page
from wagtail.search.models import Query


def search(request):
    template = 'search/search.html'  #new
    search_query = request.GET.get('q', None)
    page = request.GET.get('page', 1)
    
    # Search
    if search_query:
        query = Query.get(search_query)
        search_results = Post.objects.filter(Q(title__icontains=query) | Q(body__icontains=query)).search(search_query)

        # Record hit
        query.add_hit()
    else:
        search_results = Page.objects.none()

    # Pagination
    paginator = Paginator(search_results, 10)
    try:
        search_results = paginator.page(page)
    except PageNotAnInteger:
        search_results = paginator.page(1)
    except EmptyPage:
        search_results = paginator.page(paginator.num_pages)

    return render(request, 'search/search.html', {
        'search_query': search_query,
        'search_results': search_results,
    })
