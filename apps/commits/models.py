from django.db import models


class GitCommits(models.Model):
    commit_id = models.IntegerField(unique=True, blank=True, null=True)
    commit_sha = models.CharField(
        unique=True, max_length=255, blank=True, null=True)
    commit_message = models.TextField(blank=True, null=True)
    commit_author_email = models.CharField(
        max_length=255, blank=True, null=True)
    commit_committer_name = models.CharField(
        max_length=255, blank=True, null=True)
    commit_committer_email = models.CharField(
        max_length=255, blank=True, null=True)
    commit_date = models.DateTimeField(blank=True, null=True)
    commit_author_name = models.CharField(
        max_length=255, blank=True, null=True)
    commit_stable_status = models.IntegerField(
        blank=True, null=True, default=0)
    repo_name = models.CharField(max_length=255, blank=True, null=True)
    owner = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'git_commits'

    def __str__(self):
        return f"{self.commit_id} - {self.commit_sha} "
