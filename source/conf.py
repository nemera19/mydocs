# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))

from download_files import get_files

# -- Project information -----------------------------------------------------

project = "mydocs"
copyright = "2022, Liza"
author = "Liza"

rst_prolog = """
.. |brand-name| replace:: EO-Lab
.. |brand-name-hyphen| replace:: EO-Lab
"""
brand_name = 'EO-Lab'
# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = []

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "sphinx_rtd_theme"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]

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
html_context = {
    "display_github": True,
    "urls_dict": urls_dict,
    "github_host": "github.com",
    "github_user": "CloudFerro",
    "github_repo": "waw3-1-kubernetes-test",
    "github_version": "main",
    "conf_py_path": "/source/",
    "source_suffix": ".rst",
}
html_logo = "eolablogo.png"
html_theme_options = {
    'logo_only': True,
    'display_version': False,
}
