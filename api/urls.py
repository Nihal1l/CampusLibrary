from django.urls import path, include
from book.views import BookViewSet
from borrow.views import BorrowItemViewSet, BorrowRecordViewSet
from rest_framework_nested import routers

router = routers.DefaultRouter()
router.register('books', BookViewSet, basename='books')
router.register('borrows', BorrowRecordViewSet, basename='borrows')



borrow_router = routers.NestedDefaultRouter(router, 'borrows', lookup='borrow')
borrow_router.register('items', BorrowItemViewSet, basename='borrow-item')

# urlpatterns = router.urls

urlpatterns = [
    path('', include(router.urls)),
    path('', include(borrow_router.urls))
]