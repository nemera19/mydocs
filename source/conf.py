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
from get_rst_files import get_files

# -- Project information -----------------------------------------------------

project = "mydocs"
copyright = "2022, Liza"
author = "Liza"


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

urls_dict = get_files(
    [
       "https://github.com/CloudFerro/cf3-doc/tree/main/source/datavolume/extendvolumelinux",
       "https://github.com/CloudFerro/cf3-doc/blob/main/source/general/startavmfromasnapshot",     
       "https://github.com/CloudFerro/cf3-doc/blob/main/source/general/keypairopenstack",     
       "https://github.com/CloudFerro/cf3-doc/blob/main/source/networking/createanetworkwithrouter", 
       "https://github.com/CloudFerro/kubernetes-doc/blob/main/source/How-to-Create-a-Kubernetes-Cluster-Using-Eumetsat-Elasticity-OpenStack-Magnum",        
       "https://github.com/CloudFerro/kubernetes-doc/blob/main/source/How-to-Create-a-Kubernetes-Cluster-Template-Using-Eumetsat-Elasticity-OpenStack-Magnum",
       "https://github.com/CloudFerro/kubernetes-doc/blob/main/source/How-To-Install-OpenStack-and-Magnum-Clients-for-Command-Line-Interface-to-Eumetsat-Elasticity-Horizon",
       "https://github.com/CloudFerro/kubernetes-doc/blob/main/source/How-To-Use-Command-Line-Interface-for-Kubernetes-Clusters-On-Eumetsat-Elasticity-OpenStack-Magnum",
       "https://github.com/CloudFerro/kubernetes-doc/blob/main/source/How-To-Access-Kubernetes-Cluster-Post-Deployment-Using-Kubectl-On-Eumetsat-Elasticity-OpenStack-Magnum",
       "https://github.com/CloudFerro/kubernetes-doc/blob/main/source/How-To-Create-API-Server-LoadBalancer-for-Kubernetes-Cluster-On-Eumetsat-Elasticity-OpenStack-Magnum",
       "https://github.com/CloudFerro/kubernetes-doc/blob/main/source/How-To-Create-Floating-IP-for-Servers-on-Eumetsat-Elasticity-OpenStack-Magnum",
       "https://github.com/CloudFerro/kubernetes-doc/blob/main/source/Creating-Additional-Nodegroups-in-Kubernetes-Cluster-on-Eumetsat-Elasticity-OpenStack-Magnum",
       "https://github.com/CloudFerro/kubernetes-doc/blob/main/source/Autoscaling-Kubernetes-Cluster-Resources-on-Eumetsat-Elasticity-OpenStack-Magnum",
       "https://github.com/CloudFerro/kubernetes-doc/blob/main/source/How-to-Connect-Two-Instances-Through-a-Private-Network-on-Eumetsat-Elasticity-OpenStack-Magnum",
       "https://github.com/CloudFerro/kubernetes-doc/blob/main/source/How-To-Create-and-Manage-Networks-on-Eumetsat-Elasticity-OpenStack-Magnum",
       "https://github.com/CloudFerro/kubernetes-doc/blob/main/source/How-to-Create-a-Router-on-Eumetsat-Elasticity-OpenStack-Magnum",
       "https://github.com/CloudFerro/kubernetes-doc/blob/main/source/How-to-Use-Security-Groups-to-Tighten-Security-Using-Eumetsat-Elasticity-OpenStack-Magnum",
       "https://github.com/CloudFerro/kubernetes-doc/blob/main/source/How-to-Create-and-Return-a-Floating-IP-Address-on-Eumetsat-Elasticity-OpenStack-Magnum",
       "https://github.com/CloudFerro/kubernetes-doc/blob/main/source/Volume-based-vs-Ephemeral-based-Storage-for-Kubernetes-Clusters-on-Eumetsat-Elasticity-OpenStack-Magnum", 
    ]
)


html_context = {
    "display_github": True,
    "urls_dict": urls_dict,
    "github_host": "github.com",
    "github_user": "CloudFerro",
    "github_repo": "test_2022",
    "github_version": "main",
    "conf_py_path": "/source/",
    "source_suffix": ".rst",
}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]
