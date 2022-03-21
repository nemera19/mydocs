from os.path import exists
from urllib.request import urlretrieve

import requests
from github import Github


def process_url(url: str):
    if "tree" in url:
        repo, dir_name = url.split("/tree/master/")
        return repo.replace("https://github.com/", ""), dir_name
    return None, None


def check_updates(file, file_path):
    if (
        exists(file_path.replace("source/", ""))
        and file.decode("utf-8") == open(file_path.replace("source/", ""), "r").read()
    ):
        return False
    return True


def get_files(url: str):
    repo_name, dir_name = process_url(url)
    if repo_name is None:
        return
    gh = Github()
    repo = gh.get_repo(repo_name)
    github_raw_url = "https://raw.githubusercontent.com"
    contents_list = repo.get_contents(dir_name)
    for content in contents_list:
        if content.type == 'file':
            github_file = requests.get(
                github_raw_url
                + "/"
                + repo.full_name
                + "/master/"
                + dir_name
                + "/"
                + content.path.replace(' ', '%20').split("/")[-1]
            )
            if check_updates(github_file.content, content.path):
                urlretrieve(
                    github_raw_url
                    + "/"
                    + repo.full_name
                    + "/master/"
                    + dir_name
                    + "/"
                    + content.path.replace(' ', '%20').split("/")[-1],
                    content.path.split("/")[-1],
                )
