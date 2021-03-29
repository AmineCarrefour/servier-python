import unittest

from operators.transformations import *


class DrugsPipelineTest(unittest.TestCase):

    @staticmethod
    def fixture_merged_all():
        return merge_all()

    @staticmethod
    def fixture_search_drugs():
        df = DrugsPipelineTest.fixture_merged_all()
        return search_drugs(df)

    ############################################################################################################
    # merge_all method should join correctly pubmed and clinical publications and return columns of type string
    ############################################################################################################

    def test_dataset_type(self):
        df = DrugsPipelineTest.fixture_merged_all()
        self.assertEqual(str(df['title'].dtype), 'string')
        self.assertEqual(str(df['date'].dtype), 'string')
        self.assertEqual(str(df['journal'].dtype), 'string')
        self.assertEqual(str(df['id'].dtype), 'string')

    ############################################################################################################
    # merge_all method should return 21 rows with title name
    ############################################################################################################

    def test_total_number_titles(self):
        df = DrugsPipelineTest.fixture_merged_all()
        merged_title_count = df['title'].count()
        expected_drug_mention_in_title_count = 21
        self.assertEqual(merged_title_count, expected_drug_mention_in_title_count)

    ############################################################################################################
    # search_drugs method should return 19 rows with drug name mentioned
    ############################################################################################################

    def test_total_number_drug(self):
        df = DrugsPipelineTest.fixture_search_drugs()
        merged_drug_count = df['drug_name'].count()
        expected_drug_mention_count = 19
        self.assertEqual(merged_drug_count, expected_drug_mention_count)

    ############################################################################################################
    # search_drugs method should return a dataset of 3 column names : 'drug_name', 'journal', 'date'
    ############################################################################################################

    def test_valid_schema(self):
        df = DrugsPipelineTest.fixture_search_drugs()
        self.assertEqual(df.columns.values.tolist(), ['drug_name', 'journal', 'date'])

    ############################################################################################################
    # DIPHENHYDRAMINE should be mentioned 6 times in the graph dependency
    ############################################################################################################

    def test_valid_number_of_mention_for_diphenhydramine(self):
        df = DrugsPipelineTest.fixture_search_drugs()
        expected_drug_count = 6
        drug_name = 'DIPHENHYDRAMINE'
        df = df[df['drug_name'] == drug_name]
        df = df['drug_name'].count()
        self.assertEqual(df, expected_drug_count)

    ############################################################################################################
    # GLUCAGON should be mentioned O time in the graph dependency since it's not the drug list
    ############################################################################################################

    def test_valid_number_of_mention_for_diphenhydramine(self):
        df = DrugsPipelineTest.fixture_search_drugs()
        expected_drug_count = 0
        drug_name = 'GLUCAGON'
        df = df[df['drug_name'] == drug_name]
        df = df['drug_name'].count()
        self.assertEqual(df, expected_drug_count)


if __name__ == "__main__":
    unittest.main()
