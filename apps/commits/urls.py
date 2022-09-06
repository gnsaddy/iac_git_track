from django.urls import path, include
from .views import ping_pong, git_commits, get_last_commit, get_stable_commit, git_add_commits
from rest_framework import routers

router = routers.DefaultRouter()


urlpatterns = [
    path('ping/', ping_pong),
    path('gitcommits/', git_commits),
    path('lastcommit/', get_last_commit),
    path('stablecommit/', get_stable_commit),
    path('addcommits/', git_add_commits),
    path('', include(router.urls)),
]
