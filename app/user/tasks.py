import re
from datetime import datetime

from app.repo.models import Repo


def get_repo(instance):
    print(instance)

    from github import Github

    if instance.git_token:
        g = Github(instance.git_token)

        repo_list = [str(repo.full_name) for repo in g.get_user().get_repos('vimm0')]
        r = re.compile('vimm0/*')
        newlist = filter(r.match, repo_list)

        another_list = [repo.replace('vimm0/', '') for repo in list(newlist)]

        for repo in another_list:
            repo_name = g.get_user().get_repo(repo)
            Repo.objects.create(name=repo_name.name, repo_full_name=repo_name.full_name,
                                owner_name=repo_name.owner.name,
                                owner_username=repo_name.owner.login, language=repo_name.language,
                                last_modified=datetime.strptime(repo_name.last_modified,
                                                                '%a, %d %b %Y %H:%M:%S %Z'),
                                size=repo_name.size, clone_url=repo_name.clone_url, issues_url=repo_name.issues_url,
                                merges_url=repo_name.merges_url, milestones_url=repo_name.milestones_url,
                                comments_url=repo_name.comments_url, commits_url=repo_name.commits_url)
