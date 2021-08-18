from django.urls import path
from . import views

urlpatterns = [
    path('dialogue', views.DialogueListSpanishView.as_view() , name='dialogue' ),
    path('detail-dialogue/<int:year>/<int:month>/<int:day>/<int:pk>/<slug:slug>/', 
        views.DialogueDetailView.as_view() , name='detail_dialogue' ),
    path('add-dialogue/', views.AddDialogueCreateView.as_view() , name='add_dialogue' ),
    path('update-dialogue/<int:year>/<int:month>/<int:day>/<int:pk>/<slug:slug>/',
         views.UpdateDialogueCreateView.as_view() , name='update_dialogue' ),
    path('delete-dialogue/<int:year>/<int:month>/<int:day>/<int:pk>/<slug:slug>/',
         views.DeleteDialogueView.as_view() , name='delete_dialogue' ),
    
]