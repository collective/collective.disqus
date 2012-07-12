# -*- coding: utf-8 -*-
from Acquisition import aq_inner
from zope.component import getUtility
from plone.uuid.interfaces import IUUID
from plone.registry.interfaces import IRegistry

from plone.app.layout import viewlets
from plone.app.discussion.interfaces import IConversation

from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile

from collective.disqus import interfaces

class CommentsViewlet(viewlets.common.ViewletBase):
    """Viewlet to display disqus"""
    index = ViewPageTemplateFile('comments.pt')

    def is_discussion_allowed(self):
        context = aq_inner(self.context)
        conversation = IConversation(context)
        super_enabled = conversation.enabled()
        return super_enabled and self._activated()

    def _activated(self):
        settings = self.settings()
        return settings.activated and bool(settings.forum_short_name)

    def javascriptvars(self):
        """
        Return javascripts vars
        Documented in http://help.disqus.com/customer/portal/articles/472098
        """
        vars = {}
        settings = self.settings()
        vars['disqus_shortname'] = settings.forum_short_name
        uid = IUUID(self.context, None)
        if not uid:
            uid = self.context.UID()
        vars['disqus_identifier'] = uid
        vars['disqus_url'] = self.context.absolute_url()
        vars['disqus_title'] = self.context.pretty_title_or_id()

        def to_string(key):
            return "var %s='%s';"%(key, str(vars[key]))

        return "".join(map(to_string, vars.keys()))

    def settings(self):
        registry = getUtility(IRegistry)
        return registry.forInterface(interfaces.IDisqusSettings)
