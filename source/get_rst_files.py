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


urls_dict = get_files(
  {
  
        "eodata": [
            "https://github.com/CloudFerro/eolab-articles/tree/main/source/eodata",
            "https://github.com/CloudFerro/eolab-articles/blob/main/source/eodata/How-To-Access-Earth-Observation-Data-EODATA",
            "https://github.com/CloudFerro/eolab-articles/blob/main/source/eodata/CopDEM-10m-Rapid-Eye-Access-In-Code-de-Repository-EO-Lab",
            "https://github.com/CloudFerro/eolab-articles/blob/main/source/eodata/How-To-Connect-With-EO-Data-In-Jupyter-Notebook-EO-Lab",
            "https://github.com/CloudFerro/eolab-articles/blob/main/source/eodata/How-To-Access-The-CREODIAS-Repository-From-A-VM-EO-Lab",
            "https://github.com/CloudFerro/eolab-articles/blob/main/source/eodata/How-To-Download-Copernicus-Contributing-Mission-Products-To-Object-Storage-EO-Lab",
        ],

        "general": [
            "https://github.com/CloudFerro/eolab-articles/tree/main/source/general",
			"https://github.com/CloudFerro/cf3-doc/blob/main/source/general/fixconsole",
			"https://github.com/CloudFerro/cf3-doc/blob/main/source/general/guiinvmwithlinux",
			"https://github.com/CloudFerro/cf3-doc/blob/main/source/general/howtousedocker",
			"https://github.com/CloudFerro/cf3-doc/blob/main/source/general/openstackdomain",
			"https://github.com/CloudFerro/cf3-doc/blob/main/source/general/openstackproject",
			"https://github.com/CloudFerro/cf3-doc/blob/main/source/general/pythonvirtualenv",
			"https://github.com/CloudFerro/cf3-doc/blob/main/source/general/statuspower",
			"https://github.com/CloudFerro/cf3-doc/blob/main/source/s3/s3fscache",
			"https://github.com/CloudFerro/cf3-doc/blob/main/source/datavolume/ephemeralvspersistentstorage",
			"https://github.com/CloudFerro/cf3-doc/blob/main/source/datavolume/volumesnapshot",
            "https://github.com/CloudFerro/eolab-articles/blob/main/source/general/How-To-Access-Sen4CAP-EO-Lab",
            "https://github.com/CloudFerro/eolab-articles/blob/main/source/general/How-To-Access-A-VM-From-Windows-PuTTY-EO-Lab",
            "https://github.com/CloudFerro/eolab-articles/blob/main/source/general/How-To-Access-A-VM-With-MobaXterm-EO-Lab",
            "https://github.com/CloudFerro/eolab-articles/blob/main/source/general/How-To-Connect-To-A-Windows-VM-Using-Remote-Desktop-EO-Lab",
            "https://github.com/CloudFerro/eolab-articles/blob/main/source/general/How-To-Get-Access-To-The-GUI-Of-A-OSGeoLive-VM-Using-X2go-EO-Lab",
            "https://github.com/CloudFerro/eolab-articles/blob/main/source/general/How-To-Install-Cuda-Nvidia-Drivers-For-VMs-With-GPU-EO-Lab",
            "https://github.com/CloudFerro/eolab-articles/blob/main/source/general/How-To-Install-Docker-In-A-Linux-VM-EO-Lab",
            "https://github.com/CloudFerro/eolab-articles/blob/main/source/general/How-To-Install-Singularity-On-Linux-EO-Lab",
            "https://github.com/CloudFerro/eolab-articles/blob/main/source/general/How-To-Make-A-VM-Available-For-Several-Remote-Users-EO-Lab",
            "https://github.com/CloudFerro/eolab-articles/blob/main/source/general/How-To-Mount-Object-Storage-Container-As-File-System-In-Windows-EO-Lab",
            "https://github.com/CloudFerro/eolab-articles/blob/main/source/general/How-To-Transfer-Data-Tofrom-A-VM-EO-Lab",
            "https://github.com/CloudFerro/eolab-articles/blob/main/source/general/How-To-Upload-And-Synchronise-Files-With-SCP-RSYNC-EO-Lab",
            "https://github.com/CloudFerro/eolab-articles/blob/main/source/general/Sentinel-Hub-Configuration-Utility-Overview-EO-Lab",
          
        ],

        "networking": [
           "https://github.com/CloudFerro/eolab-articles/tree/main/source/networking",
			"https://github.com/CloudFerro/cf3-doc/blob/main/source/networking/accessvmsusingnames",
			"https://github.com/CloudFerro/cf3-doc/blob/main/source/networking/connectviasshlinux",
			"https://github.com/CloudFerro/cf3-doc/blob/main/source/networking/connectviasshwin",
			"https://github.com/CloudFerro/cf3-doc/blob/main/source/networking/opennewports",
			"https://github.com/CloudFerro/cf3-doc/blob/main/source/networking/vmvisible",
            "https://github.com/CloudFerro/eolab-articles/blob/main/source/networking/How-To-Access-VMs-Using-Names-Instead-Of-IP-Addresses-EO-Lab",
            "https://github.com/CloudFerro/eolab-articles/blob/main/source/networking/How-To-Configure-The-Firewall-For-CODE-DE-EO-Lab",
            "https://github.com/CloudFerro/eolab-articles/blob/main/source/networking/How-To-Open-Ports-e.g.-Port-80-For-Http-For-Servicesinstances-EO-Lab",
            "https://github.com/CloudFerro/eolab-articles/blob/main/source/networking/How-To-Restrict-VM-Access-To-Dedicated-IP-Addresses-EO-Lab",
            "https://github.com/CloudFerro/eolab-articles/blob/main/source/networking/How-To-Share-Folders-Using-NFS-EO-Lab",

        ],

      "openstack": [
            "https://github.com/CloudFerro/eolab-articles/tree/main/source/openstack",
            "https://github.com/CloudFerro/cf3-doc/blob/main/source/general/accessvmfromconsole",
			"https://github.com/CloudFerro/cf3-doc/blob/main/source/openstackcli/backupaninstance",
			"https://github.com/CloudFerro/cf3-doc/blob/main/source/openstackcli/createasetofvms",
			"https://github.com/CloudFerro/cf3-doc/blob/main/source/general/clonevm",
			"https://github.com/CloudFerro/cf3-doc/blob/main/source/openstackcli/newprojectopenstack",
			"https://github.com/CloudFerro/cf3-doc/blob/main/source/openstackcli/openstacklinux",
			"https://github.com/CloudFerro/cf3-doc/blob/main/source/general/howtousesecuritygroupsinhorizon",
			"https://github.com/CloudFerro/cf3-doc/blob/main/source/general/keypairopenstack",
			"https://github.com/CloudFerro/cf3-doc/blob/main/source/general/newlinuxvm",
			"https://github.com/CloudFerro/cf3-doc/blob/main/source/general/startavmfromasnapshot",
			"https://github.com/CloudFerro/cf3-doc/blob/main/source/general/uploadimageusingopcli",
			"https://github.com/CloudFerro/cf3-doc/blob/main/source/general/vmnewvolumeno",
			"https://github.com/CloudFerro/cf3-doc/blob/main/source/general/vmnewvolumeyes",
			"https://github.com/CloudFerro/cf3-doc/blob/main/source/general/volumesnapshotinheritance",
			"https://github.com/CloudFerro/cf3-doc/blob/main/source/networking/addremovefip",
			"https://github.com/CloudFerro/cf3-doc/blob/main/source/networking/cannotaccess",
			"https://github.com/CloudFerro/cf3-doc/blob/main/source/networking/createanetworkwithrouter",
			"https://github.com/CloudFerro/cf3-doc/blob/main/source/s3/objectstorage",
     		"https://github.com/CloudFerro/cf3-doc/blob/main/source/datavolume/attachvolumetovmlessthan2tb",
            "https://github.com/CloudFerro/eolab-articles/blob/main/source/openstack/Cannot-Attach-Interface-To-VM-EO-Lab",
            "https://github.com/CloudFerro/eolab-articles/blob/main/source/openstack/Dashboard-Overview---Project-Quotas-And-Flavors-Limits-EO-Lab",
            "https://github.com/CloudFerro/eolab-articles/blob/main/source/openstack/How-To-ShelveUnshelve-A-VM-EO-Lab",
            "https://github.com/CloudFerro/eolab-articles/blob/main/source/openstack/How-To-Attach-A-Volume-2TB-To-A-VM-In-Linux-EO-Lab",
            "https://github.com/CloudFerro/eolab-articles/blob/main/source/openstack/How-To-Attach-A-Volume-To-A-Windows-VM-EO-Lab",
            "https://github.com/CloudFerro/eolab-articles/blob/main/source/openstack/How-To-Change-Parameters-Of-An-Already-Existing-And-Configured-VM-EO-Lab",
            "https://github.com/CloudFerro/eolab-articles/blob/main/source/openstack/How-To-Create-A-Volume-Backup-From-A-Linux-VM-EO-Lab",
            "https://github.com/CloudFerro/eolab-articles/blob/main/source/openstack/How-To-Create-A-Volume-Backup-From-A-Windows-VM-EO-Lab",
            "https://github.com/CloudFerro/eolab-articles/blob/main/source/openstack/How-To-Create-An-SSH-Key-Pair-In-Windows-EO-Lab",
            "https://github.com/CloudFerro/eolab-articles/blob/main/source/openstack/How-To-Transfer-VMs-And-Volumes-Between-OpenStack-Projects-EO-Lab",
            "https://github.com/CloudFerro/eolab-articles/blob/main/source/openstack/What-Image-Formats-Are-Available-In-OpenStack-EO-Lab",

        ],

    
    "s3": [
           "https://github.com/CloudFerro/eolab-articles/tree/main/source/s3",
			"https://github.com/CloudFerro/cf3-doc/blob/main/source/s3/deletelargebucket",
			"https://github.com/CloudFerro/cf3-doc/blob/main/source/s3/mountobjectstorage",
			"https://github.com/CloudFerro/cf3-doc/blob/main/source/s3/remotetransfer", 
            "https://github.com/CloudFerro/eolab-articles/blob/main/source/s3/How-To-Access-EODATA-And-Object-Storage-Using-s3cmd-Linux",
            "https://github.com/CloudFerro/eolab-articles/blob/main/source/s3/How-To-Access-Private-Object-Storage-Using-S3cmd-EO-Lab",
		

        ],

      "security": [
            "https://github.com/CloudFerro/eolab-articles/tree/main/source/security",
			"https://github.com/CloudFerro/cf3-doc/blob/main/source/general/generateec2",
			"https://github.com/CloudFerro/cf3-doc/blob/main/source/networking/sshkeypair",
            "https://github.com/CloudFerro/eolab-articles/blob/main/source/security/What-If-I-Forgot-To-Add-The-SSH-Key-To-My-VM-Or-Deleted-It-EO-Lab",
            "https://github.com/CloudFerro/eolab-articles/blob/main/source/security/How-To-Avoid-Unwanted-SSH-Login-Attempts",
	
        ],
       
    }
)
