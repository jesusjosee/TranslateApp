from django.urls import path
from . import views

urlpatterns = [
    path('dialogue', views.DialogueListSpanishView.as_view() , name='dialogue' ),
    path('detail-dialogue/<pk>/', views.DialogueDetailView.as_view() , name='detail_dialogue' ),
    path('add-dialogue/', views.AddDialogueCreateView.as_view() , name='add_dialogue' ),
    path('update-dialogue/<pk>/', views.UpdateDialogueCreateView.as_view() , name='update_dialogue' ),
    path('delete-dialogue/<pk>/', views.DeleteDialogueView.as_view() , name='delete_dialogue' ),
    
]