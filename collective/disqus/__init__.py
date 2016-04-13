# -*- coding: utf-8 -*-
from zope.i18nmessageid import MessageFactory


_ = MessageFactory('collective.disqus')


def initialize(context):
    """Initializer called when used as a Zope 2 product."""
