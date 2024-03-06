from rest_framework.pagination import PageNumberPagination

class MyPageNumberPagination(PageNumberPagination):
    page_size = 5
    page_query_param = 'p' # Instaed pf page you can change the word page
    page_size_query_param = 'records' # user can specify the number of records
    max_page_size = 3 # max page size of records
    last_page_strings = 'end' # for end page