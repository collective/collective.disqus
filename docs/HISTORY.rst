Changelog
---------

2.0b3 (unreleased)
^^^^^^^^^^^^^^^^^^

- Use plone styles in portlets HTML [agnogueira]

- Show portlets results inside an ordered list [agnogueira]

- Fixes an issue with content title containing single quotes [ericof]

- provide partial 0.3.1->2.0 upgrade profile [gyst]

- Tested compatibility with Plone 4.3. [hvelarde]


2.0b2 (2013-02-22)
^^^^^^^^^^^^^^^^^^

- Add Disqus icon on the control panel. [hvelarde]

- Include an Id in the counter link for themming purposes [tamosauskas]

- Update Traditional Chinese translation. [l34marr]

- Bugfix, javascript variables weren't being embedded in the page.
  [jcbrand]


2.0b1 (2012-12-13)
^^^^^^^^^^^^^^^^^^^

- Added a "Disqus summary view" to include comments count on listings.
  [frapell]

- Added a viewlet that will display the comments count beneath the object's 
  title. [frapell]

- If wrong url (not returning json), return empty list. [flecox]

- Use network-path reference to load Disqus JavaScript to avoid "This Page
  Contains Both Secure and Non-Secure Items" messages over HTTPS. [hvelarde]

- Updated Brazilian Portuguese translation. [hvelarde]

- Updated German translation. [fRiSi]

- Updated Spanish translation. [frapell]

- Bugfix for the article's titles. [frapell]

- Avoid removal of registry records on reinstall. [hvelarde]

- Tested for Plone 4.2 compatibility. [hvelarde]

- Added portlets for hot and popular threads. [hvelarde]

- Added records to access the Disqus API to the control panel. [hvelarde]

- Updated development buildout configurations. [hvelarde]

- Updated package distribution and documentation. [hvelarde]

- Add control panel and viewlet. [toutpt]

- Complete refactoring of the package. [toutpt, hvelarde, frapell]


0.3.2 (unreleased)
^^^^^^^^^^^^^^^^^^

- moved javascript template code from disqus_panel.pt into it's view to bypass
  a chameleon related bug. [thet]
- added DisqusAPI class for remote DISQUS API calls with predefined control
  panel settings, it inherits from disqus-python API [piv]
- added option to switch DISQUS credit link off [piv]
- added DISQUS SSO Addon support [piv]
- added export comments view from plone to WXR format to import
  it into DISQUS [piv]
- added product layer interface and registered viewlet for it instead of
  hiding it on uninstall [piv]
- added highly recommended disqus_url additional parameter [piv]
- added an option to display DISQUS comments only for anonymous [zupo]
- add french translation [toutpt]
- updated pot file and Spanish translation; removed mo file [hvelarde]
- include Products.CMFCore.permissions.zcml [ajung]
- add support for language param according to http://docs.disqus.com/help/97/
  [toutpt]


0.3.1 (2011-01-31)
^^^^^^^^^^^^^^^^^^

- cleaned up i18n and added German translation [fRiSi]
- added Spanish translation [hvelarde]
- fixed action icons [hvelarde]
- disqus_summary_listing now uses the configured shortname and includes
  the js only once [fRiSi]


0.3.0 (2010-08-15)
^^^^^^^^^^^^^^^^^^

- updated disqus api [garbas]
- added disqus summary listing view with number of comments [garbas]
- added some basic integration tests using plone.app.testing [garbas]
- removed actionicon registration - depracated [garbas]
- found and fixed bug in plone which was causing hidding of default plone
  commenting viewlet only for "Plone Classic Theme". [garbas]
  https://dev.plone.org/plone/ticket/10903
- add test buildout, with coverage report and pylint check
  current result is 82% coverage and pylint score is -13.21/10 [garbas]
- added translation for english and slovenian [garbas]


0.2.0 (2009-10-30)
^^^^^^^^^^^^^^^^^^

- Compatibility with Plone 4 [sargo]
- Uninstall profile (unhide plone.comment viewlet, hide collective.disqus
  viewlet) [sargo]


0.1.0 (2009-08-13)
^^^^^^^^^^^^^^^^^^

- Initial release [sargo]
