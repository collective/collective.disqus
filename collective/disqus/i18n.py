from zope.i18nmessageid import MessageFactory
_ = MessageFactory("collective.disqus")

activated = _(u"label_activated",
              default=u"Activate disqus as system comment for Plone")

forum_short_name = _(u"label_forum_shortname",
                     default=u"The forum shortname as registered on Disqus.")


controlpanel_label = _(u"label_controlpanel",
                       default=u"Disqus settings")
controlpanel_desc = _(u"help_controlpanel",
                      default=u"Fill this form to make plone comment system use disqus")
