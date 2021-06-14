from django.urls import path
from . import views

urlpatterns = [
    path('', views.PhraseListSpanishView.as_view() , name='home' ),
    path('list-english', views.PhraseListEnglishView.as_view() , name='all_english_phrase' ),
    path('list-learned/', views.LearnedListView.as_view() , name='list_learned' ),
    path('list-nolearned/', views.NoLearnedListView.as_view() , name='list_nolearned' ),
    path('detail-phrase/<pk>/', views.PhraseDetailView.as_view() , name='detail_phrase' ),
    path('add/', views.AddPhraseCreateView.as_view() , name='add' ),
    path('update/<pk>/', views.UpdatePhraseCreateView.as_view() , name='update' ),
    path('delete/<pk>/', views.DeletePhraseView.as_view() , name='delete' ),
    path('list-learned-english/', views.LearnedEnglishListView.as_view() , name='list_learned_english' ),
    path('list-nolearned-english/', views.NoLearnedEnglishListView.as_view() , name='list_nolearned_english' ),
    path('list-no-edit/', views.NoEditListView.as_view() , name='list_no_edit' ),

    #registration
    path('sign-up/', views.registration, name='sign_up'),


]