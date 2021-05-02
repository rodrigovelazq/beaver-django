from django.db import models


class Owners(models.Model):
    github_id = models.BigIntegerField()
    login = models.CharField(max_length=255)
    avatar_url = models.CharField(max_length=255)
    url = models.CharField(max_length=255)
    html_url = models.CharField(max_length=255)

    def __str__(self):
        return self.login


class Repositories(models.Model):
    github_id = models.BigIntegerField()
    name = models.CharField(max_length=255)
    full_name = models.CharField(max_length=255)
    owner = models.ForeignKey(Owners, on_delete=models.CASCADE)
    description = models.TextField()
    url = models.CharField(max_length=255)
    html_url = models.CharField(max_length=255)
    git_url = models.CharField(max_length=255)
    ssh_url = models.CharField(max_length=255)
    clone_url = models.CharField(max_length=255)
    homepage = models.CharField(max_length=255)
    size = models.PositiveIntegerField()
    stargazers_count = models.PositiveIntegerField()
    watchers_count = models.PositiveIntegerField()
    language = models.CharField(max_length=255)
    forks_count = models.PositiveIntegerField()
    forks = models.PositiveIntegerField()
    open_issues = models.PositiveIntegerField()
    watchers = models.PositiveIntegerField()
    network_count = models.PositiveIntegerField()
    subscribers_count = models.PositiveIntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    pushed_at = models.DateTimeField()

    def __str__(self):
        return self.name
