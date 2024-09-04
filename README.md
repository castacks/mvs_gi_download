# Download the dataset #

clone this rebpo.

Get the dataset lists.

```bash
python3 download_lists.py
```

Then 4 txt files will be downloaded in the local folder.

```
minio_list_train.txt
minio_list_validate.txt
tar_list_train.txt
tar_list_validate.txt
```

The `tar_` files show the size of every tar file listed in the coresponding `minio_` ones.

For the training dataset, copy `minio_list_train.txt` to a new txt file and remove lines for the tar files the user doesn't want. Name the copied file to, e.g., `list_train.txt`. Then do

```bash
python3 download_dataset.py \
    --input_list list_train.txt \
    --output_dir datasets \
    --dataset_type train
```

where 

- __output_dir__: The output directory. Will be created if does not exist.
- __dataset_type__: Choose from `train` and `validate` depending on which dataset is being downloaded.

To download `validate` dataset, copy and edit `minio_list_validate.txt` and use `--dataset_type validate` when running the above command.

Enjoy!
