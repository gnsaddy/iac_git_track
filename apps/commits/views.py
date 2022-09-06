from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import viewsets
from apps.commits.helper import commits_of_repo_github

from apps.utils import error_response, success_response
from .models import GitCommits
from .serializers import GitCommitsSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from rest_framework.decorators import api_view
import os
import requests


def ping_pong(request):
    return JsonResponse({"message": "ping-pong"})

# view for adding new commit to database


@api_view(['GET'])
def git_add_commits(request):
    if request.method == 'GET':
        try:
            github_api = "https://api.github.com"
            gh_session = requests.Session()
            gh_session.auth = (
                "gnsaddy", "ghp_lSZj70j18X3dDjGymwSE3vUKe7rwu40iayR64"
            )
            url = github_api + '/repos/gnsaddy/tf-nginx-docker/commits'

            commits = gh_session.get(url=url)
            
            if commits.status_code == 200:
                fetch_commits = commits_of_repo_github(
                    'tf-nginx-docker', 'gnsaddy', github_api, gh_session
                )
                print(f"fetch_commits: {fetch_commits}")
                if len(fetch_commits) > 0:
                    return success_response(message="Commits added successfully", data=fetch_commits)
                else:
                    return success_response(message="No new commits found to add", data=fetch_commits)
            else:
                return error_response(message="Error in fetching commits", data=commits.json())
        except Exception as e:
            return error_response(str(e))


@api_view(['GET'])
def git_commits(request):
    if request.method == 'GET':
        git_commits = GitCommits.objects.all()
        serializer = GitCommitsSerializer(git_commits, many=True)
        commit_list = []
        for commit in serializer.data:
            commit_list.append({
                'commit_id': commit['commit_id'],
                'commit_sha': commit['commit_sha'],
                'commit_message': commit['commit_message'],
                'commit_date': commit['commit_date'],
                'commit_author_name': commit['commit_author_name'],
                'commit_author_email': commit['commit_author_email'],
                'commit_committer_name': commit['commit_committer_name'],
                'commit_committer_email': commit['commit_committer_email'],
                'repo_name': commit['repo_name'],
                'owner': commit['owner'],
                'stable_status': commit['commit_stable_status']
            })
        if serializer.data:
            return success_response('GitCommits list', commit_list)
        else:
            return error_response('GitCommits list not found')

# view for getting last inserted commit


@api_view(['GET'])
def get_last_commit(request):
    if request.method == 'GET':
        git_commits = GitCommits.objects.all().order_by('-id')[:1]
        serializer = GitCommitsSerializer(git_commits, many=True)
        commit_list = []
        for commit in serializer.data:
            commit_list.append({
                'commit_id': commit['commit_id'],
                'commit_sha': commit['commit_sha'],
                'commit_message': commit['commit_message'],
                'commit_date': commit['commit_date'],
                'commit_author_name': commit['commit_author_name'],
                'commit_author_email': commit['commit_author_email'],
                'commit_committer_name': commit['commit_committer_name'],
                'commit_committer_email': commit['commit_committer_email'],
                'repo_name': commit['repo_name'],
                'owner': commit['owner'],
                'stable_status': commit['commit_stable_status']
            })
        if serializer.data:
            return success_response('GitCommits list', commit_list)
        else:
            return error_response('GitCommits list not found')


# view for getting commit whose stable status is true
@api_view(['GET'])
def get_stable_commit(request):
    if request.method == 'GET':
        git_commits = GitCommits.objects.filter(commit_stable_status=True)
        serializer = GitCommitsSerializer(git_commits, many=True)
        commit_list = []
        for commit in serializer.data:
            commit_list.append({
                'commit_id': commit['commit_id'],
                'commit_sha': commit['commit_sha'],
                'commit_message': commit['commit_message'],
                'commit_date': commit['commit_date'],
                'commit_author_name': commit['commit_author_name'],
                'commit_author_email': commit['commit_author_email'],
                'commit_committer_name': commit['commit_committer_name'],
                'commit_committer_email': commit['commit_committer_email'],
                'repo_name': commit['repo_name'],
                'owner': commit['owner'],
                'stable_status': commit['commit_stable_status']
            })
        if serializer.data:
            return success_response('GitCommits list', commit_list)
        else:
            return error_response('GitCommits list not found')

# view to update stable status of commit based on commit_sha


@api_view(['PUT'])
def update_stable_status(request):
    if request.method == 'PUT':
        commit_sha = request.data['commit_sha']
        stable_status = request.data['stable_status']
        git_commits = GitCommits.objects.filter(commit_sha=commit_sha)
        serializer = GitCommitsSerializer(git_commits, many=True)
        commit_list = []
        for commit in serializer.data:
            commit_list.append({
                'commit_id': commit['commit_id'],
                'commit_sha': commit['commit_sha'],
                'commit_message': commit['commit_message'],
                'commit_date': commit['commit_date'],
                'commit_author_name': commit['commit_author_name'],
                'commit_author_email': commit['commit_author_email'],
                'commit_committer_name': commit['commit_committer_name'],
                'commit_committer_email': commit['commit_committer_email'],
                'repo_name': commit['repo_name'],
                'owner': commit['owner'],
                'stable_status': commit['commit_stable_status']
            })
        if serializer.data:
            git_commits.update(commit_stable_status=stable_status)
            return success_response(f'Updated successfully!!!', commit_list)
        else:
            return error_response('Update failed!!!')
