from django.urls import path

from . import views

app_name = 'polls'  # Đặt namespace cho các URL

urlpatterns = [
    # Sử dụng generic view IndexView cho trang index
    path("", views.IndexView.as_view(), name="index"),
    
    # Sử dụng generic view DetailView cho chi tiết câu hỏi
    path("<int:pk>/", views.DetailView.as_view(), name="detail"),  # pk là primary key
    
    # Sử dụng generic view ResultsView cho trang kết quả
    path("<int:pk>/results/", views.ResultsView.as_view(), name="results"),
    
    # Sử dụng function-based view cho việc vote
    path("<int:question_id>/vote/", views.vote, name="vote"),
]
