#!/usr/bin/env python
"""
Interface for the wsgi.py file
"""

"""
Why are we not using wsgi directly? It's because of weird importing shenanigans involved when trying 
to import settings. It sets the current path to whatever the wsgi.py path is which means Python will struggle
to find the topic app which is both a level above and in an adjacent directory.

Solution?
We call the application from here, so all the directories would be BELOW this one. 
"""


import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'topic_project.topic_project.settings')

from topic_project.topic_project.wsgi import application

application = application
