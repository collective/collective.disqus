# -*- coding: utf-8 -*-
from Acquisition import aq_inner
from collective.disqus import interfaces
from plone.app.discussion.interfaces import IConversation
from plone.app.layout import viewlets
from plone.registry.interfaces import IRegistry
from plone.uuid.interfaces import IUUID
from Products.CMFPlone.utils import safe_unicode
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from zope.component import getUtility


class DisqusBaseViewlet(viewlets.common.ViewletBase):
    """ A base class to be used for Disqus viewlets """

    def is_discussion_allowed(self):
        context = aq_inner(self.context)
        conversation = IConversation(context)
        super_enabled = conversation.enabled()
        return super_enabled and self._activated()

    def _activated(self):
        settings = self.settings()
        return settings.activated and bool(settings.forum_short_name)

    def settings(self):
        registry = getUtility(IRegistry)
        return registry.forInterface(interfaces.IDisqusSettings)


class CommentsViewlet(DisqusBaseViewlet):
    """Viewlet to display disqus"""
    index = ViewPageTemplateFile('comments.pt')

    def javascriptvars(self):
        """
        Return javascripts vars
        Documented in http://help.disqus.com/customer/portal/articles/472098
        """
        vars = {}
        settings = self.settings()
        vars['disqus_shortname'] = settings.forum_short_name
        if settings.developer_mode:
            vars['disqus_developer'] = 1
        uid = IUUID(self.context, None)
        if not uid:
            uid = self.context.UID()
        vars['disqus_identifier'] = uid
        vars['disqus_url'] = self.context.absolute_url()
        vars['disqus_title'] = self.context.pretty_title_or_id()

        def to_string(key):
            value = vars[key]
            if isinstance(value, basestring):
                # Replace single quotes for double quotes
                # This avoids Unexpected identifier error in JavaScript
                value = safe_unicode(vars[key]).replace("'", '"')
            else:
                value = str(value)
            return "var {0}='{1}';".format(key, value)

        output = ''
        for k in vars.keys():
            output += to_string(k)
        return output


class CommentsCountViewlet(DisqusBaseViewlet):
    """ Viewlet that will display the number of comments """

    def get_counter_js(self):
        """ Get the js mentioned in
        http://disqus.com/admin/universal/ for counting comments
        """
        settings = self.settings()

        short_name = settings.forum_short_name

        if short_name:
            result = """
<script async src="https://{0}.disqus.com/count.js">
</script>""".format(short_name)
        else:
            result = ''

        return result
