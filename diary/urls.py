from django.urls import path
from .views import GradesListView, GradeCreateView, GradeUpdateView, GradeDeleteView

urlpatterns = [
    path('grades/', GradesListView.as_view(), name='grades_list'),
    path('grades/update/<int:pk>/', GradeUpdateView.as_view(), name='grade_update'),
    path('grades/create/', GradeCreateView.as_view(), name='grade_create'),
    path('grades/delete/<int:pk>/', GradeDeleteView.as_view(), name='grade_delete'),
]