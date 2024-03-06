from rest_framework.pagination import LimitOffsetPagination

class MyLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 5
    offset_query_param = 'myoffset' # instead of offset
    limit_query_param = 'mylimit' # instead of limit
    max_limit = 5 # max limit of limit
