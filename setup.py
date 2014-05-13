# -*- coding: utf-8 -*-

from setuptools import find_packages
from setuptools import setup

version = '2.0rc2.dev0'
long_description = (
    open('README.rst').read() + '\n' +
    open('CONTRIBUTORS.rst').read() + '\n' +
    open('CHANGES.rst').read()
)

setup(name='collective.disqus',
      version=version,
      description="Integration of Disqus comments platform API into Plone.",
      long_description=long_description,
      classifiers=[
          'Development Status :: 5 - Production/Stable',
          'Environment :: Web Environment',
          'Framework :: Plone',
          'Framework :: Plone :: 4.1',
          'Framework :: Plone :: 4.2',
          'Framework :: Plone :: 4.3',
          # 'Framework :: Plone :: 5.0',
          'Intended Audience :: End Users/Desktop',
          'Intended Audience :: System Administrators',
          'License :: OSI Approved :: GNU General Public License v2 (GPLv2)',
          'Operating System :: OS Independent',
          'Programming Language :: JavaScript',
          'Programming Language :: Python',
          'Programming Language :: Python :: 2.6',
          'Programming Language :: Python :: 2.7',
          'Topic :: Office/Business :: News/Diary',
          'Topic :: Software Development :: Libraries :: Python Modules',
      ],
      keywords='plone disqus comments api portlets',
      author='JeanMichel FRANCOIS aka toutpt',
      author_email='toutpt@gmail.com',
      url='http://github.com/collective/collective.disqus',
      license='GPLv2',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['collective'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'collective.prettydate',
          'disqus-python',
          'plone.app.discussion',
          'plone.app.layout',
          'plone.app.registry',
          'plone.memoize',
          'plone.portlets',
          'plone.registry',
          'Products.CMFCore',
          'Products.CMFPlone >=4.1',
          'Products.GenericSetup',
          'setuptools',
          'zope.component',
          'zope.i18nmessageid',
          'zope.interface',
          'zope.schema',
      ],
      extras_require={
          'test': [
              'AccessControl',
              'plone.app.testing',
              'plone.browserlayer',
              'unittest2',
          ],
      },
      entry_points="""
      [z3c.autoinclude.plugin]
      target = plone
      """,
      )
