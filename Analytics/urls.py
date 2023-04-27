from django.urls import path 
from Analytics.views import MainAnalytics, AnalyticsSearch


urlpatterns = [
    
     path('analytics/', MainAnalytics.as_view(), name='analytics'),
     path('search_analytics/', AnalyticsSearch.as_view(), name='search-analytics'),
     
     
     
     
]


 