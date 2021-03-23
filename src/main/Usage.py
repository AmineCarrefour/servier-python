from operators.adhoc_query import *


class Usage:

    @staticmethod
    def launch():
        return get_journal_with_max_distinct_mentions()


if __name__ == "__main__":
    agg = Usage()
    result = agg.launch()
    print(result)
