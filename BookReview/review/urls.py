from django.urls import path
from .views import index, BookListCreateAPIView, SubmitReviewView, BookReviewsView

urlpatterns = [
    path('', index, name='index'),
    path('books/', BookListCreateAPIView.as_view(), name='book_list'),
    path('books/<int:book_id>/reviews', BookReviewsView.as_view(), name='book_review'),
    path('submit-review/', SubmitReviewView.as_view(), name='submit_review'),
]
