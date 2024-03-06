from rest_framework.pagination import CursorPagination

class MyCursorPagination(CursorPagination):
    page_size = 3
    ordering = 'name'
    cursor_query_param = 'cu' # instead of cursor