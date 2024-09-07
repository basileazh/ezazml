poetry run aml create-or-update-adls-datastore

poetry run aml create-mltable wasbs://data@azuremlexampledata.blob.core.windows.net/titanic.csv titanic/titanic_mlt2 --inputs-extension=csv --headers=all_files_same_headers --infer-column-types --include-path-column --keep-columns=col1,col2 --drop-columns=col3

poetry run aml create-dataset integration/data/books.csv --asset-type=uri_file --data-description="Dataset Description" --data-name=DatasetName --data-version=v1

poetry run aml get-dataframe --path=integration/data/books.csv --data-source=local

poetry run aml get-uri integration/data/books.csv --data-source=local

poetry run aml get-uri integration/data/books.csv --data-source=datastore

poetry run aml upload-file-to-datastore integration/data/books.csv temp/uploaded_books.csv --asset-type uri_file --overwrite MERGE_WITH_OVERWRITE

poetry run aml download-file-from-datastore integration/data/books.csv temp/downloaded_books.csv