# -*- coding: utf-8 -*-

import json
import logging
import urllib

from urlparse import urlparse

from zope.component import getUtility
from zope.app.component.hooks import getSite

from plone.registry.interfaces import IRegistry

from collective.disqus.config import PROJECTNAME
from collective.disqus.interfaces import IDisqusSettings

logger = logging.getLogger(PROJECTNAME)


def disqus_list_hot(forum, max_results):
    """
    Gets a list of most recommended threads.
    """
    base_url = ("https://disqus.com/api/3.0/threads/listHot.json?"
                "access_token=%s&api_key=%s&api_secret=%s&"
                "forum=%s&limit=%s")

    registry = getUtility(IRegistry)
    disqus = registry.forInterface(IDisqusSettings)
    url = base_url % (disqus.access_token,
                      disqus.app_public_key,
                      disqus.app_secret_key,
                      forum,
                      max_results)

    return get_disqus_results(url)


def disqus_list_popular(forum, max_results, interval):
    """
    Gets a list of most popular threads.
    """
    base_url = ("https://disqus.com/api/3.0/threads/listPopular.json?"
                "access_token=%s&api_key=%s&api_secret=%s&"
                "forum=%s&limit=%s&interval=%s")

    registry = getUtility(IRegistry)
    disqus = registry.forInterface(IDisqusSettings)
    url = base_url % (disqus.access_token,
                      disqus.app_public_key,
                      disqus.app_secret_key,
                      forum,
                      max_results,
                      interval)

    return get_disqus_results(url)


def get_disqus_results(url):
    """
    Creates a request to Disqus API, using the url parameter.
    """
    try:
        request = urllib.urlopen(url)
    except IOError:
        url_parse = urlparse(url)
        logger.error('IOError accessing %s://%s%s' % (url_parse.scheme,
                                                      url_parse.netloc,
                                                      url_parse.path))
        return []

    response = request.read()
    disqus = json.loads(response)
    if disqus['code'] != 0:
        logger.error('Disqus API error: %s (see http://disqus.com/api/docs/errors/ '
                     'for more details)' % disqus['response'])
        return []

    site = getSite()
    items = []

    for item in disqus['response']:
        # HACK: Disqus' API doesn't return data in a correct way.
        #This code obtains the title according to the returned url by Disqus
        #and then searches the catalog building the url from the object's id
        #backwards to the site root.
        #It also replaces the url by the site's url.
        if item['title'] == item['link']:
            url_parse = urlparse(item['link'])
            # We remove the inicial '/' and cast the path to str
            path = str(url_parse.path[1:])
            obj = site.unrestrictedTraverse(path, None)
            if obj is not None:
                item['title'] = obj.Title()
                items.append(item)
        else:
            items.append(item)

    return items
