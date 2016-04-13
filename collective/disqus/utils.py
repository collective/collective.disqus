# -*- coding: utf-8 -*-

from collective.disqus.config import PROJECTNAME
from collective.disqus.interfaces import IDisqusSettings
from plone.registry.interfaces import IRegistry
from urlparse import urlparse
from zope.component import getUtility

import json
import logging
import urllib


logger = logging.getLogger(PROJECTNAME)


def disqus_list_hot(forum, max_results):
    """
    Gets a list of most recommended threads.
    """
    base_url = ('https://disqus.com/api/3.0/threads/listHot.json?'
                'access_token={0}&api_key={1}&api_secret={2}&'
                'forum={3}&limit={4}')

    registry = getUtility(IRegistry)
    disqus = registry.forInterface(IDisqusSettings)
    url = base_url.format(
        disqus.access_token,
        disqus.app_public_key,
        disqus.app_secret_key,
        forum,
        max_results,
    )

    return get_disqus_results(url)


def disqus_list_popular(forum, max_results, interval):
    """
    Gets a list of most popular threads.
    """
    base_url = ('https://disqus.com/api/3.0/threads/listPopular.json?'
                'access_token={0}&api_key={1}&api_secret={2}&'
                'forum={3}&limit={4}&interval={5}')

    registry = getUtility(IRegistry)
    disqus = registry.forInterface(IDisqusSettings)
    url = base_url.format(
        disqus.access_token,
        disqus.app_public_key,
        disqus.app_secret_key,
        forum,
        max_results,
        interval,
    )

    return get_disqus_results(url)


def get_disqus_results(url):
    """
    Creates a request to Disqus API, using the url parameter.
    """
    try:
        request = urllib.urlopen(url)
    except IOError:
        url_parse = urlparse(url)
        msg = 'IOError accessing {0}://{1}{2}'
        logger.error(
            msg.format(url_parse.scheme, url_parse.netloc, url_parse.path))
        return []

    response = request.read()

    items = []
    if response:
        try:
            disqus = json.loads(response)
        except:  # noqa FIXME: B901 blind except: statement
            msg = 'Response error with url: {0} '\
                  '(see http://disqus.com/api/docs/errors/ for more details)'
            logger.error(msg.format(url))
            return []

        if disqus['code'] != 0:
            msg = 'Disqus API error: {0} '\
                  '(see http://disqus.com/api/docs/errors/ for more details)'
            logger.error(msg.format(disqus['response']))
            return []

        items = disqus['response']

    return items
