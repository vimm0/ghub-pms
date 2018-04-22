import re
from datetime import datetime

from app.repo.models import Repo


def get_repo(instance):
    print('Populating repo ...')
    if instance.git_token:
        from github import Github

        g = Github(instance.git_token)
        GIT_USERNAME = g.get_user().login

        repo_list = [str(r.full_name) for r in g.get_user().get_repos(GIT_USERNAME)]
        print(repo_list)
        r = re.compile(GIT_USERNAME + '/*')
        newlist = filter(r.match, repo_list)

        another_list = [repo.replace(GIT_USERNAME + '/', '') for repo in list(newlist)]
        print(another_list)
        for repo in another_list:
            repo_name = g.get_user().get_repo(repo)
            print(repo_name)
            Repo.objects.get_or_create(name=repo_name.name, repo_full_name=repo_name.full_name,
                                       owner_name=repo_name.owner.name, language=repo_name.language,
                                       owner_username=repo_name.owner.login, size=repo_name.size,
                                       clone_url=repo_name.clone_url, issues_url=repo_name.issues_url,
                                       merges_url=repo_name.merges_url, milestones_url=repo_name.milestones_url,
                                       comments_url=repo_name.comments_url, commits_url=repo_name.commits_url,
                                       git_last_modified=datetime.strptime(repo_name.last_modified,
                                                                           '%a, %d %b %Y %H:%M:%S %Z'))
