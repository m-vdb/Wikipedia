# -*- coding: utf-8 -*-
import unittest

from wikipedia import wikipedia
from request_mock_data import mock_data


# mock out _wiki_request
def _wiki_request(params):
  return mock_data["_wiki_request calls"][tuple(sorted(params.items()))]
wikipedia._wiki_request = _wiki_request


class TestCategory(unittest.TestCase):

	def test_init_title(self):
		games = wikipedia.WikipediaCategory('Games')
		self.assertEqual(games.title, 'Category: Games')


	def test_get_members(self):
		games = wikipedia.WikipediaCategory('Games')
		members = list(games.get_members())
		self.assertEqual(len(members), 6)
