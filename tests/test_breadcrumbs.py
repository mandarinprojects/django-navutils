from django.test import LiveServerTestCase, TestCase

from navutils import Breadcrumb
from navutils.templatetags import navutils_tags


class BreadcrumbTest(LiveServerTestCase):
    def test_breadcrumb_reverse(self):
        crumb = Breadcrumb(label='Test', pattern_name='index')

        self.assertEqual(crumb.get_url(), '/')

    def test_breadcrumb_url(self):
        crumb = Breadcrumb(label='Test', url='http://test.com')

        self.assertEqual(crumb.get_url(), 'http://test.com')



class RenderBreadcrumbTest(TestCase):

    def test_render_single_crumb(self):
        crumb = Breadcrumb(label='Test', pattern_name='index')

        output = navutils_tags.render_crumb(crumb)
        self.assertHTMLEqual(
            output,
            '<li class="crumb"><a href="/">Test</a></li>')

    def test_render_breadcrumbs(self):
        crumbs = []
        crumbs.append(Breadcrumb(label='Test1', pattern_name='index'))
        crumbs.append(Breadcrumb(label='Test2', url='http://test.com'))

        output = navutils_tags.render_breadcrumbs(crumbs)
        self.assertHTMLEqual(
            output,
            """
            <ul class="breadcrumbs">
                <li class="crumb"><a href="/">Test1</a></li>
                <li class="crumb"><a href="http://test.com">Test2</a></li>
            </ul>
            """)
