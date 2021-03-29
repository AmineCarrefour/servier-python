from operators.transformations import *


############################################################################################################
# Ad-hoc processing : from the output, find the journal who mentions the most of different drug names
############################################################################################################


def get_journal_with_max_distinct_mentions(df):
    aggregated_series = df.groupby(by=['journal'], dropna=False, as_index=None).drug_name.nunique()
    df = aggregated_series[aggregated_series == aggregated_series.max()]
    max_distinct_mentions_list = str(df['journal'].dropna().apply(pd.Series).stack().tolist()).strip('[\'\']')
    return max_distinct_mentions_list
