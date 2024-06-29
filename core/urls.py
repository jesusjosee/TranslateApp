from django.urls import path
from . import views

urlpatterns = [
    path('', views.PhraseListSpanishView.as_view() , name='dashboard' ),
    path('list-english', views.PhraseListEnglishView.as_view() , name='all_english_phrase' ),
    path('list-learned/', views.LearnedListView.as_view() , name='list_learned' ),
    path('list-nolearned/', views.NoLearnedListView.as_view() , name='list_nolearned' ),
    path('detail-phrase/<int:year>/<int:month>/<int:day>/<int:pk>/<slug:slug>/', views.PhraseDetailView.as_view() , name='detail_phrase' ),
    path('add/', views.AddPhraseCreateView.as_view() , name='add' ),
    path('update/<int:year>/<int:month>/<int:day>/<int:pk>/<slug:slug>/', views.UpdatePhraseCreateView.as_view() , name='update' ),
    path('delete/<int:year>/<int:month>/<int:day>/<int:pk>/<slug:slug>/', views.DeletePhraseView.as_view() , name='delete' ),
    path('list-learned-english/', views.LearnedEnglishListView.as_view() , name='list_learned_english' ),
    path('list-nolearned-english/', views.NoLearnedEnglishListView.as_view() , name='list_nolearned_english' ),
    path('list-no-edit/', views.NoEditListView.as_view() , name='list_no_edit' ),
    path('prueba-query/', views.Pruebaquery.as_view(), name='prueba-query'),

    #registration
    #path('sign-up/', views.registration, name='sign_up'),


]