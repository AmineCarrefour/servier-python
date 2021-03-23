from operators.ingestions_and_normalizations import *


############################################################################################################
# Search mentioned drugs and return a valid JSON
############################################################################################################

def get_drugs_list():
    drugs_list = read_drugs()['drug'].apply(pd.Series).stack().tolist()
    return drugs_list


def search_drugs(df):
    text_likes = df.select_dtypes(include=[object, "string"])
    drugs_list = get_drugs_list()
    result_list = []
    for s in drugs_list:
        contains_in_journal = df[text_likes.apply(
            lambda column: column.str.contains(s, regex=True, case=False, na=False))
            .any(axis=1)]['journal'].apply(pd.Series).stack().tolist()
        contains_in_dates = df[text_likes.apply(
            lambda column: column.str.contains(s, regex=True, case=False, na=False))
            .any(axis=1)]['date'].apply(pd.Series).stack().tolist()
        result_list.append([s, contains_in_journal, contains_in_dates])
    df = pd.DataFrame(result_list, columns=['drug_name', 'journal', 'date'])
    df = df.set_index(['drug_name']).apply(pd.Series.explode).reset_index()
    return df


def pipeline_output(df):
    df.to_json(Configs.RESULTS_PATH_JSON, orient='records', indent=4, index=True, force_ascii=False)
    print('Data flow done. Please check the output here : {}'.format(Configs.RESULTS_PATH_JSON))
