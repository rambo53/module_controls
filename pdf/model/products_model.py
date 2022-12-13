import os
#from easy_framework.akeneo import Akeneo
from pprint import pprint
import pandas as pd

root = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))


class Products_model():
    """
        Class that implement Akeneo framework.

    """
    '''
    def __init__(self):
        self.akeneo = Akeneo("{}/config.ini".format(root))


    def refresh_products_from_pim_to_csv(self, root):
        df = self.akeneo.products.get_products()
        df.to_csv("{}/Ressources/get_products.csv".format(root), header=True, index=False)
    '''

    def get_all_products_from_csv(self):
        """ Get all products contained into the csv file.
        Args:
            root(string): root path to locate files
        """

        all_products_dict = [{}]
        try:
            df = pd.read_csv(f"{root}/ressources/get_products.csv", sep=",", encoding="utf-8")
        except Exception as e:
            return [{
                "identifier": "",
                "name": "",
                "enabled": "",
                "parent": "",
                "family": "",
                "created": "",
                "updated": ""
            }]
        # Transform the df into a dict, bc its easier to manipulate in template
        for index, row in df.iterrows():
            # Date format from df is like : 2021-07-22T10:19:53+00:00
            # We want a better format like : 2021-07-22 10:19:53
            tmp_created = row["created"].split("+")[0].replace("T", " ")
            tmp_updated = row["updated"].split("+")[0].replace("T", " ")

            all_products_dict.append({
                "identifier": row["sku"],
                "name": row["name"],
                "enabled": row["enabled"],
                "parent": row["parent"],
                "family": row["family"],
                "created": tmp_created,
                "updated": tmp_updated
            })
        # Clear data
        all_products_dict = [x for x in all_products_dict if "identifier" in x]
        for item in all_products_dict:
            if str(item["parent"]) == 'nan':
                item["parent"] = ""
        return all_products_dict

    def search_products(self, product_to_search, all_products):
        """ Return all lines contained in all_products where
            product_to_search pattern is in an all_products dict

        Args:
            all_products(list(dict)): List of dict where each dict corresponds to a product
            product_to_search(str): pattern of what we want

        Returns:
            products(list(dict)): list of dict of all products matched with product_to_search pattern

        """
        products = []
        for prod in all_products:
            for key, value in prod.items():
                if str(product_to_search).lower() in str(value).lower() and prod not in products:
                    products.append(prod)

        return products
