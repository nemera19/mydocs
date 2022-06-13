import os
import re
from os.path import exists
from urllib.request import urlretrieve
import time
import requests
import github
from multiprocessing.dummy import Pool
from github import Github

from sphinx.util import logging


from conf import brand_name

logger = logging.getLogger(__name__)


def process_url(url: str):
    if "tree" in url:
        repo, dir_name = re.split(r"/tree/\w+/", url)
        return repo.replace("https://github.com/", ""), dir_name
    return None, None


def process_content(content):
    content_path = content.path
    if "|brand-name|" in content.name:
        content_path = content.path.replace("|brand-name|", brand_name)
    return content_path.split("/")[-1]


def urls_list_to_dict(urls_list: list) -> dict:
    urls_dict = {}
    for url in urls_list:
        repo_name, dir_name = process_url(url.replace("blob", "tree"))
        if not urls_dict.get(repo_name, None):
            urls_dict[repo_name] = []
        urls_dict[repo_name].append(dir_name)
    return urls_dict


def check_updates(github_file_content: str, local_file_path: str) -> bool:
    dir_name = local_file_path.split("/")[0]
    file_path = dir_name + local_file_path
    if exists(dir_name):
        if exists(file_path) and github_file_content == open(file_path, "rb").read():
            return False
    else:
        os.makedirs(dir_name)
    return True

def download_file(github_file_url, file_path):
    urlretrieve(
                github_file_url,
                file_path,
            )


def download_content(content, folder):
    content_url = {}
    content_name = process_content(content)
    if content.type == "file":
        if ".rst" in content.name:
            content_url[
                folder + "/" + content_name.replace(".rst", "")
            ] = content.html_url
        github_file_url = content.download_url
        github_file = requests.get(github_file_url)
        if check_updates(
            github_file.content,
            folder + "/" + content_name,
        ):
            download_file(github_file_url, folder + "/" + content_name)
    return content_url


def get_directory_content(folder: str, urls_list: dict):
    urls_dict = urls_list_to_dict(urls_list.get(folder))
    gh = Github(login_or_token=os.environ.get("github_token", ""))
    for repo, dirs in urls_dict.items():
        repo = gh.get_repo(repo)
        for dir_name in dirs:
            contents_list = []
            try:
                contents_list = repo.get_contents(dir_name)
            except github.GithubException as e:
                logger.warning(
                   'directory "%s" was omitted, "%s", "%s"'
                    % (dir_name, e.status, e.data["message"])
                )
            content_urls = {}
            for content in contents_list:
                content_urls.update(download_content(content, dir_name))
    return content_urls
                


def get_files(urls_list: dict) -> dict:
    external_repos_url = {}
    pool = Pool(4)
    get_directory_content(urls_list.keys())
    external_repos_url.update(pool.map(get_directory_content, urls_list.keys()))
    print(external_repos_url)
    return external_repos_url
