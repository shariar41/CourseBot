from argparse import Namespace
from django.urls import path, include


#router = routers.DefaultRouter()

#router.register(r'auth', CouponViewSet, basename='coupon')
urlpatterns = [
    #path('urls/',include('knox.urls')),
    path('auth/',include('accounts.urls')),
]
# 'rest_framework_datatables.renderers.DatatablesRenderer',
#     ),
#     'DEFAULT_FILTER_BACKENDS': (
#         'rest_framework_datatables.filters.DatatablesFilterBackend',
#     ),
#     'DEFAULT_PAGINATION_CLASS': 'rest_framework_datatables.pagination.DatatablesPageNumberPagination',
#     'PAGE_SIZE': 50,