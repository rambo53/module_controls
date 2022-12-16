from flask import jsonify
from app import repo, app
import os
from controls.utils.controls_utils import Controls
from controls.utils.df_utils import Df_Utils

def get_error_file_service(name):
    try:
        path_to_directory = os.path.join(repo, app.config["DIRECTORY_NAME"],name, 'out')
        data_file = [f for f in os.listdir(path_to_directory) if os.path.isfile(os.path.join(path_to_directory, f))]
        path_error_file = os.path.join(path_to_directory, data_file[0])
        df_errors  = Df_Utils(path_error_file).df_from_file.iloc[:,1:]
        html_errors = df_errors.to_html(justify='center',classes='table text-center',index=False)

        return jsonify({'error_table':html_errors})
    except Exception as e:
        return jsonify({'message' : str(e), 'status':404})


def add_error_file_service(data):

    try:
        path_to_directory = os.path.join(repo, app.config["DIRECTORY_NAME"], data['name'], 'in')
        data_file = [f for f in os.listdir(path_to_directory) if os.path.isfile(os.path.join(path_to_directory, f))]
        path_to_file = os.path.join(path_to_directory, data_file[0])
        df_errors = Controls().controls_global(path_to_file, data['controls_dict'])

        path_to_directory_error = os.path.join(repo, app.config["DIRECTORY_NAME"], data['name'], 'out')

        Df_Utils.df_to_csv(df_errors, os.path.join(path_to_directory_error,data['name']+"error.csv"))

        nb_rows_error = Df_Utils.get_nb_rows(df_errors)

        return jsonify(
            {
                'message' : f"ok get error file {nb_rows_error}",
                'status': 200,
                'name_file_error': data['name']
                }
            )
    except Exception as e:
        return jsonify({'message' : str(e), 'status':404})


