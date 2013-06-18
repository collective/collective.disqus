# -*- coding: utf-8 -*-

import unittest2 as unittest


from zope.interface import alsoProvides

from plone.app.discussion.interfaces import IDiscussionLayer

from plone.app.testing import TEST_USER_ID
from plone.app.testing import setRoles

from Products.CMFCore.utils import getToolByName

from collective.disqus.testing import INTEGRATION_TESTING

from collective.disqus.comments import CommentsViewlet


class PortletsTestCase(unittest.TestCase):

    layer = INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.request = self.layer['request']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])

        portal_setup = self.portal.portal_setup
        portal_setup.runAllImportStepsFromProfile(
            'profile-collective.disqus:test_fixture'
        )

        self.portal.invokeFactory('Folder', 'test-folder')

        self.folder = self.portal['test-folder']

        alsoProvides(self.portal.REQUEST, IDiscussionLayer)

        self.portal.invokeFactory('Document', 'doc1')

        self.discussionTool = getToolByName(self.portal,
                                            'portal_discussion',
                                            None)

        self.discussionTool.overrideDiscussionFor(self.portal.doc1, False)
        self.context = getattr(self.portal, 'doc1')

    def test_viewlet_not_renders_for_improper_object(self):
        """ Only objects that have their comments enabled should
        show the viewlet
        """
        viewlet = CommentsViewlet(self.context, self.request, None, None)
        self.assertFalse(viewlet.is_discussion_allowed())

    def test_viewlet_renders_for_proper_object(self):
        """ Only objects that have their comments enabled should
        show the viewlet
        """
        self.discussionTool.overrideDiscussionFor(self.portal.doc1, True)

        viewlet = CommentsViewlet(self.context, self.request, None, None)
        self.assertTrue(viewlet.is_discussion_allowed())

    def test_viewlet_js_variables_properly_handled(self):
        """ Objects with single quotes in their titles should
            replace it with double quotes
        """
        self.discussionTool.overrideDiscussionFor(self.portal.doc1, True)
        self.context.setTitle("Title containing 'single quotes'")
        viewlet = CommentsViewlet(self.context, self.request, None, None)
        javascriptvars = viewlet.javascriptvars()
        self.assertTrue('Title containing "single quotes"' in javascriptvars)
