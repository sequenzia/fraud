import os, sys, warnings, yaml
from typing import List, Any, Union, Optional



file_base = "google"

config_file = "/var/lib/alpha/quantum/_projects/fraud/config.yml"
cloud_files = ["creditcard.csv.zip"]

# if not file_base:
#     file_base = {"dirs": {"data": "data"}}

# if file_base == "google":

file_base = {"dirs": {"data": "data"}, "cloud": {"google": {"bucket_name": "sequenzia-public", "blob_dir": "projects/data", "cloud_files": "[""creditcard.csv.zip""]"}}}

                 #          {"bucket_name": "sequenzia-public",
                 #           "blob_dir": "projects/data"}
                 #      }
                 # }



with open(config_file, 'w') as file:
    yml_doc = yaml.dump(file_base, file, default_flow_style=False, sort_keys=False)





