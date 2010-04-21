from fabric.api import *

def build():
    """ Do it. 
    """
    local("ronn -5 man/kennethreitz.1.ron > index.html")

def deploy():
	""" Activate local virtualenv
	"""
	local("git commit -am 'update'")
	local("git push")