# -*- coding: utf-8 -*-
from plone.z3cform import layout

from plone.app.registry.browser import controlpanel as base
from collective.disqus import interfaces
from collective.disqus import i18n


class ControlPanelForm(base.RegistryEditForm):
    schema = interfaces.IDisqusSettings
    label = i18n.controlpanel_label
    description = i18n.controlpanel_desc

ControlPanelView = layout.wrap_form(ControlPanelForm,
                                    base.ControlPanelFormWrapper)
