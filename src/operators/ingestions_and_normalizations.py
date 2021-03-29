from utils.Configs import *

Configs = Configs()


############################################################################################################
# Read input files and normalize dates
############################################################################################################

def normalize_types(df):
    df['date'] = pd.to_datetime(df.date)
    df = df.astype('string')
    return df


def read_pubmed_csv():
    pubmed_csv = pd.read_csv(Configs.PUBMED_CSV_PATH, sep=',')
    return pubmed_csv


def read_pubmed_json():
    pubmed_json = pd.read_json(Configs.PUBMED_JSON_PATH)
    return pubmed_json


def read_drugs():
    df = pd.read_csv(Configs.DRUGS_PATH, sep=',')
    return df


def read_clinical_trials():
    df = normalize_types(pd.read_csv(Configs.CLINICAL_TRIALS_PATH, sep=','))
    return df


def read_data_pipeline_output():
    pubmed_json = pd.read_json(Configs.RESULTS_PATH_JSON)
    return pubmed_json


############################################################################################################
# Merge all data
############################################################################################################

def merge_pubmed():
    pubmed_csv = normalize_types(read_pubmed_csv())
    pubmed_json = normalize_types(read_pubmed_json())
    pubmed_merged = pd.concat([pubmed_csv, pubmed_json], ignore_index=True)
    return pubmed_merged


def merge_all():
    pubmed_df = merge_pubmed()
    clinical_df = read_clinical_trials()
    clinical_df = clinical_df.rename(columns={"scientific_title": "title"})
    merged = pd.concat([clinical_df, pubmed_df], ignore_index=True)
    return merged
