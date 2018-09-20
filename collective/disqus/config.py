# -*- coding: utf-8 -*-
from plone import api


PROJECTNAME = 'collective.disqus'
TCACHE = 10 * 60  # to be used on RAM cache

IS_PLONE_5 = api.env.plone_version().startswith('5')
