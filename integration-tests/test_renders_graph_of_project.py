import unittest
import splinter
from expects import expect, be_true
import logging
from integration_test import IntegrationTest

selenium_logger = logging.getLogger('selenium.webdriver.remote.remote_connection')
selenium_logger.setLevel(logging.WARNING)


TEST_SERVER = 'http://localhost:8001'


class TestRendersGraphOfProject(IntegrationTest):
    def setUp(self):
        self.browser = splinter.Browser()
        self.person = Person(self.browser)

    def test_shows_name_of_project(self):
        self.person.visit_site()

        expect(self.browser.is_text_present('gitignore', wait_time=3)).to(be_true)


class Person(object):
    def __init__(self, browser):
        self.browser = browser

    def visit_site(self):
        self.browser.visit(TEST_SERVER)

