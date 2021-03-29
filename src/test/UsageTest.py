import unittest

from operators.adhoc_query import *


class UsageTest(unittest.TestCase):

    @staticmethod
    def fixture_merged_all():
        return merge_all()

    @staticmethod
    def fixture_search_drugs():
        df = UsageTest.fixture_merged_all()
        return search_drugs(df)

    @staticmethod
    def fixture_get_journal_with_max_distinct_mentions():
        df = UsageTest.fixture_search_drugs()
        return get_journal_with_max_distinct_mentions(df)

    ############################################################################################################
    # get_journal_with_max_distinct_mentions method should select the drug with the most of mentions
    ############################################################################################################

    def test_adoc_query(self):
        result = UsageTest.fixture_get_journal_with_max_distinct_mentions()
        expected_result = 'The journal of maternal-fetal & neonatal medicine'
        self.assertEqual(result, expected_result)


if __name__ == "__main__":
    unittest.main()
