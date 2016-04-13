# -*- coding: utf-8 -*-

from collective.disqus.testing import INTEGRATION_TESTING
from collective.disqus.utils import get_disqus_results
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID

import os
import unittest


hot0 = 'lavrov-los-sirios-deberan-decidir-el-futuro-de-bashar-al-asad'
hot1 = 'nuevo-ataque-de-un-drone-estadounidense-deja-10-fallecidos-al-noreste-de-pakistan'
hot2 = 'farc-niegan-haber-emprendido-una-campana-terrorista'
hot3 = 'television-cubana-transmitio-primeras-imagenes-del-ano-del-lider-de-la-revolucion-fidel-castro'
hot4 = 'colombianos-marchan-en-el-suroeste-del-pais-contra-la-violencia'
hot5 = 'guatemala-respalda-a-argentina-en-reclamo-por-soberania-de-las-islas-malvinas'
hot6 = 'canciller-de-colombia-visita-cuba-para-impulsar-cumbre-del-alba'
hot7 = 'ingenieria-de-un-ataque-militar'
hot8 = 'argentina-protestara-en-la-onu-por-militarizacion-del-atlantico-sur'
hot9 = 'francia-e-italia-llaman-a-consultas-a-embajadores-en-siria'

popular0 = 'farc-niegan-haber-emprendido-una-campana-terrorista'
popular1 = 'television-cubana-transmitio-primeras-imagenes-del-ano-del-lider-de-la-revolucion-fidel-castro'
popular2 = 'lavrov-los-sirios-deberan-decidir-el-futuro-de-bashar-al-asad'
popular3 = 'colombianos-marchan-en-el-suroeste-del-pais-contra-la-violencia'
popular4 = 'indigena-panameno-muere-en-accion-policial-durante-protesta-contra-ley-minera'
popular5 = 'canciller-de-colombia-visita-cuba-para-impulsar-cumbre-del-alba'
popular6 = 'ingenieria-de-un-ataque-militar'
popular7 = 'cumbre-del-alba-continua-este-domingo-revision-de-temas-pendientes'
popular8 = 'guatemala-respalda-a-argentina-en-reclamo-por-soberania-de-las-islas-malvinas'
popular9 = 'diez-razones-por-las-que-estados-unidos-ya-no-es-la-tierra-de-la-libertad'

PATHNAME = os.path.dirname(__file__) + '/'


class DisqusUtilsTestCase(unittest.TestCase):

    layer = INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.request = self.layer['request']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        self.portal.invokeFactory('Folder', 'articulos')
        self.folder = self.portal['articulos']

    def test_disqus_list_hot(self):
        results = get_disqus_results(PATHNAME + 'listHot.json')
        self.assertEqual(len(results), 10)
        self.assertEqual(results[0]['title'], 'Hot 0')
        self.assertEqual(results[1]['title'], 'Hot 1')
        self.assertEqual(results[2]['title'], 'Hot 2')
        self.assertEqual(results[3]['title'], 'Hot 3')
        self.assertEqual(results[4]['title'], 'Hot 4')
        self.assertEqual(results[5]['title'], 'Hot 5')
        self.assertEqual(results[6]['title'], 'Hot 6')
        self.assertEqual(results[7]['title'], 'Hot 7')
        self.assertEqual(results[8]['title'], 'Hot 8')
        self.assertEqual(results[9]['title'], 'Hot 9')
        # si hay algún error se retorna una lista vacía
        self.assertEqual(get_disqus_results('listHot.error.json'), [])

    def test_disqus_list_popular(self):
        results = get_disqus_results(PATHNAME + 'listPopular.json')
        self.assertEqual(len(results), 10)
        self.assertEqual(results[0]['title'], 'Popular 0')
        self.assertEqual(results[1]['title'], 'Popular 1')
        self.assertEqual(results[2]['title'], 'Popular 2')
        self.assertEqual(results[3]['title'], 'Popular 3')
        self.assertEqual(results[4]['title'], 'Popular 4')
        self.assertEqual(results[5]['title'], 'Popular 5')
        self.assertEqual(results[6]['title'], 'Popular 6')
        self.assertEqual(results[7]['title'], 'Popular 7')
        self.assertEqual(results[8]['title'], 'Popular 8')
        self.assertEqual(results[9]['title'], 'Popular 9')
        # si hay algún error se retorna una lista vacía
        self.assertEqual(get_disqus_results('listPopular.error.json'), [])

    def test_disqus_wrong_response(self):
        results = get_disqus_results(PATHNAME + 'response.notjson')
        self.assertEqual(results, [])
