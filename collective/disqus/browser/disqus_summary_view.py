
from Products.CMFPlone.PloneBatch import Batch

from Products.Five.browser import BrowserView

from collective.disqus.utils import get_forum_short_name


class View(BrowserView):
    """ This view works as the regular summary_view but it will
    add the comments count to each item
    """

    def get_counter_js(self):
        """ Get the js mentioned in
        http://disqus.com/admin/universal/ for counting comments
        """

        short_name = get_forum_short_name(self.context)

        if short_name:
            result = ("<script type=\"text/javascript\" async=\"async\""
                      "        src=\"http://%s.disqus.com/count.js\" >"
                      "</script>" % short_name)

        else:
            result = ""

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
