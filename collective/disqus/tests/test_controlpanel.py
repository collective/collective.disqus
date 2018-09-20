# -*- coding: utf-8 -*-

from collective.disqus.config import PROJECTNAME
from collective.disqus.interfaces import IDisqusSettings
from collective.disqus.testing import INTEGRATION_TESTING
from plone.app.testing import logout
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from plone.registry.interfaces import IRegistry
from zope.component import getMultiAdapter
from zope.component import getUtility

import unittest


BASE_REGISTRY = 'collective.disqus.interfaces.IDisqusSettings.'


class ControlPanelTestCase(unittest.TestCase):

    layer = INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.controlpanel = self.portal['portal_controlpanel']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])

    def test_controlpanel_has_view(self):
        view = getMultiAdapter((self.portal, self.portal.REQUEST),
                               name='disqus-controlpanel')
        view = view.__of__(self.portal)
        self.assertTrue(view())

    def test_controlpanel_view_is_protected(self):
        from AccessControl import Unauthorized
        logout()
        self.assertRaises(Unauthorized,
                          self.portal.restrictedTraverse,
                          '@@disqus-controlpanel')

    def test_controlpanel_installed(self):
        actions = [a.getAction(self)['id']
                   for a in self.controlpanel.listActions()]
        self.assertTrue('collective.disqus.settings' in actions,
                        'control panel was not installed')

    def test_controlpanel_removed_on_uninstall(self):
        qi = self.portal['portal_quickinstaller']
        qi.uninstallProducts(products=[PROJECTNAME])
        actions = [a.getAction(self)['id']
                   for a in self.controlpanel.listActions()]
        self.assertTrue('collective.disqus.settings' not in actions,
                        'control panel was not removed')

    def test_controlpanel_required_fields(self):
        view = getMultiAdapter((self.portal, self.portal.REQUEST),
                               name='disqus-controlpanel')

        schema = view.form.schema
        self.assertEqual(len(schema.names()), 6)

        self.assertIn('app_public_key', schema)
        self.assertIn('access_token', schema)
        self.assertIn('activated', schema)
        self.assertIn('app_secret_key', schema)
        self.assertIn('forum_short_name', schema)
        self.assertIn('developer_mode', schema)

        self.assertFalse(schema['app_public_key'].required)
        self.assertFalse(schema['app_secret_key'].required)
        self.assertFalse(schema['access_token'].required)
        self.assertTrue(schema['activated'].required)
        self.assertTrue(schema['forum_short_name'].required)
        self.assertTrue(schema['developer_mode'].required)


class RegistryTestCase(unittest.TestCase):

    layer = INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.registry = getUtility(IRegistry)
        self.settings = self.registry.forInterface(IDisqusSettings)
        setRoles(self.portal, TEST_USER_ID, ['Manager'])

    def test_activated_record_in_registry(self):
        self.assertTrue(hasattr(self.settings, 'activated'))
        self.assertEqual(self.settings.activated, None)

    def test_forum_short_name_record_in_registry(self):
        self.assertTrue(hasattr(self.settings, 'forum_short_name'))
        self.assertEqual(self.settings.forum_short_name, None)

    def test_access_token_record_in_registry(self):
        self.assertTrue(hasattr(self.settings, 'access_token'))
        self.assertEqual(self.settings.access_token, None)

    def test_app_public_key_record_in_registry(self):
        self.assertTrue(hasattr(self.settings, 'app_public_key'))
        self.assertEqual(self.settings.app_public_key, None)

    def test_app_secret_key_record_in_registry(self):
        self.assertTrue(hasattr(self.settings, 'app_secret_key'))
        self.assertEqual(self.settings.app_secret_key, None)

    def test_records_removed(self):
        qi = self.portal['portal_quickinstaller']
        qi.uninstallProducts(products=[PROJECTNAME])

        records = [
            BASE_REGISTRY + 'activated',
            BASE_REGISTRY + 'forum_short_name',
            BASE_REGISTRY + 'access_token',
            BASE_REGISTRY + 'app_public_key',
            BASE_REGISTRY + 'app_secret_key',
        ]

        for r in records:
            self.assertNotIn(r, self.registry)
