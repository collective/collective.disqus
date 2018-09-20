# -*- coding: utf-8 -*-
from collective.disqus.interfaces import IDisqusSettings
from plone.registry.interfaces import IRegistry
from Products.CMFPlone.PloneBatch import Batch
from Products.Five.browser import BrowserView
from zope.component import getUtility


class View(BrowserView):
    """ This view works as the regular summary_view but it will
    add the comments count to each item
    """

    def get_counter_js(self):
        """ Get the js mentioned in
        http://disqus.com/admin/universal/ for counting comments
        """
        registry = getUtility(IRegistry)
        settings = registry.forInterface(IDisqusSettings)

        short_name = settings.forum_short_name

        if short_name:
            result = """
<script async src="https://{0}.disqus.com/count.js">
</script>""".format(short_name)
        else:
            result = ''

        return result

    def get_results(self, b_start, limit_display, contentFilter):
        """ This method will get the batched list of items that
        should be showed by the template.
        It will get results whether the object is:
         - A folderish
         - Any other object that implements a "results" method
           (like ATTopic and Collection)
        Bear in mind, that the "results" method, *must* return a
        batched result.

        :param b_start: The element number where the batch should start with
        :type b_start: int
        :param limit_display: The number of elements to include
        :type limit_display: int
        :param contentFilter: Dictionary used to filter results in case of a folderish
        :type contentFilter: dict
        :returns: Batched results
        :rtype: Batch
        """
        results = Batch([], 0, 0)

        results_method = getattr(self.context, 'results', None)

        if results_method:
            results = results_method(b_start=b_start)
            if not isinstance(results, Batch):
                results = Batch([], 0, 0)

        else:
            contents = getattr(self.context, 'getFolderContents')
            if contents:
                results = contents(contentFilter,
                                   batch=True,
                                   b_size=limit_display)

        return results
