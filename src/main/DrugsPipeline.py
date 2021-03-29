from operators.transformations import *


class DrugsPipeline:

    ############################################################################################################
    # Launches data pipeline
    ############################################################################################################

    @staticmethod
    def launch():
        df = merge_all()
        search_df = search_drugs(df)
        return pipeline_output(search_df)


if __name__ == "__main__":
    pipeline = DrugsPipeline()
    pipeline.launch()
