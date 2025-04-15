from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination, CursorPagination


class SmallPageNumberPagination(PageNumberPagination):
    page_size = 5
    page_query_param = 'page_size'

    max_page_size = 20


class SmallLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 10
    offset_query_param = 'default_limit'

    max_limit = 20


class SmallCursorPagination(CursorPagination):
    ordering = '-created_time'
