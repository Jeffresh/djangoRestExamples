from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from snippets import views



# function based
# urlpatterns = [
#     path('snippets/', views.snippet_list),
#     path('snippets/<int:pk>/', views.snippet_detail),
# ]

# API endpoints
urlpatterns = [
    # path('snippets/', views.SnippetList.as_view()),
    # path('snippets/<int:pk>/', views.SnippetDetail.as_view()),
    #
    # path('users/', views.UserList.as_view()),
    # path('users/<int:pk>/', views.UserDetail.as_view()),

    path('', views.api_root),

    path('snippets/',
         views.SnippetList.as_view(),
         name='snippet-list'),

    path('snippets/<int:pk>/',
         views.SnippetDetail.as_view(),
         name='snippet-detail'),

    path('snippets/<int:pk>/highlight/',
         views.SnippetHighlight.as_view(),
         name='snippet-highlight'),

    path('users/',
         views.UserList.as_view(),
         name='user-list'),

    path('user/<int:pk>/',
         views.UserDetail.as_view(),
         name='user-detail')
]


# We don't necessarily need to add these extra url patterns in,
# but it gives us a simple, clean way of referring to a specific format.
urlpatterns = format_suffix_patterns(urlpatterns)