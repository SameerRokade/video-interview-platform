from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('record/', views.record, name='record'),
    path('ajaxHandler/<int:num_question>/', views.getQuestionAjaxHandler, name='ajaxHandler'),
    path('create-interview/', views.createInterview, name='create-interview'),
    path('finish-interview/', views.interview_is_finished, name='finish-interview'),
    path('success-interview/', views.success_interview, name='success-interview'),

    
    
    
	


]