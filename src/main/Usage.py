from operators.adhoc_query import *


class Usage:

    @staticmethod
    def launch():
        df = read_data_pipeline_output()
        return get_journal_with_max_distinct_mentions(df)


if __name__ == "__main__":
    use = Usage()
    result = "The journal who mentions the most of drugs is {}.".format(use.launch())
    print(result)
