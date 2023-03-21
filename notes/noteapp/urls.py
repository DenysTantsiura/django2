from django.urls import path
from . import views

app_name = 'noteapp'

urlpatterns = [
    path('', views.main, name='main'),
    path('note/', views.note, name='note'),
    path('tag/', views.tag, name='tag'),
]

'''
name='tag' ми вказуємо ім'я маршруту. Це необхідно, щоб працювала зв'язка 
атрибуту action="{% url 'noteapp:tag' %}" форми з ім'ям маршруту. 
Змінна app_name = 'noteapp' якраз визначає префікс для маршруту в атрибуті action
'''