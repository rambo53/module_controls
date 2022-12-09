from controls.utils.directory_utils import get_file_extension
import pandas as pd
import sys

class Df_Utils():

    def __init__(self, file_path):
        file_to_df = self.get_df(file_path)
        self.nb_rows = self.get_nb_rows(file_to_df)
        self.nb_cols = self.get_nb_cols(file_to_df)
        self.first_rows = self.get_first_rows(file_to_df)

    def get_df(self, file_path):
        file_extension = get_file_extension(file_path)
        
        try:
            if file_extension.lower() == ".csv":
                try:
                    df = pd.read_csv(file_path, sep=";")
                    return df
                except pd.errors.EmptyDataError:
                    return "Le fichier ne contient pas de données."
            elif file_extension.lower() == ".xlsx":
                try:
                    df = pd.read_excel(file_path)
                    return df
                except pd.errors.EmptyDataError:
                    return "Le fichier ne contient pas de données."
            else:
                return "L'extension n'est pas correcte ou il n'y en as pas."
        except FileNotFoundError:
            return "Le fichier n'a pas été trouvé."


    def get_nb_rows(self, df):
        return df.shape[0]

    def get_nb_cols(self, df):
        return df.shape[1]

    def get_first_rows(self, df):
        df = df.iloc[0:4].fillna("NaN")
        return df.to_html(justify='center',classes='table text-center',index=False)
