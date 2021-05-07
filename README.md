# Azure Cup 2021 - Triumviratus

This is a repository for codes of the team Triumviratus participating in [AzureCup 2021](https://azurecup.cz/). The goal
of the project is to create an application capable of classifying different types of mushrooms.

## Project structure

The project is split into three parts - a front end application, a back end classifier and a data folder. There are
specific structure requirements, noted below.

```
.
├── backend
│   ├── keychain
│   │   └── kaggle
│   ├── notebook
│   │   ├── dataset downloader.ipynb
│   ├── requirements.txt
│   └── src
│       ├── __init__.py
│       ├── arguments.py
│       ├── classifier.py
│       ├── dataset.py
│       ├── executioner.py
│       ├── handler.py
│       ├── image.py
│       ├── main.py
│       ├── publisher.py
│       ├── template.py
│       └── watcher.py
├── frontend
│   ├── client.js
│   ├── package.json
│   ├── package-lock.json
│   └── server.js
├── data
│   ├── image-database
│   │   └── DATASET #1
│   │   │   ├── test
│   │   │   │   ├── CLASS #1
│   │   │   │   ├── CLASS #2
│   │   │   │   ├── ...
│   │   │   │   └── CLASS #N
│   │   │   └── train
│   │   │       ├── CLASS #1
│   │   │       ├── CLASS #2
│   │   │       ├── ...
│   │   │       └── CLASS #N
│   │   └── DATASET #2
│   └── marketplace
│       ├── input
│       └── output
├── LICENSE
├── project-structure.txt
└── README.md
```

# Backend [Classifier]

## Requirements

* Python 3.x (developed with 3.6.x, 3.7.x and 3.8.x)
* Python dependencies can be installed using the provided `requirements.txt`

## Installing dependencies

1. Download & install [Python 3.x](https://www.python.org/downloads/).
1. Download/clone the project.
1. Navigate to the project's backend folder
    ```
    cd azurecup-2021-triumviratus/backend
    ```
1. Create and activate [virtual environment](https://docs.python.org/3/tutorial/venv.html) (or use an existing one).
   `python -m venv venv`. Activation is platform dependent, refer to
   the [documentation](https://docs.python.org/3/tutorial/venv.html#creating-virtual-environments). For
   Windows: `venv\Scripts\Activate.bat`.
1. Install dependencies
    ```
    python -m pip install -r requirements.txt
    ```

Alternatively you may want to use distributions like [Anaconda](https://www.anaconda.com/) for downloading & dependency
management.

## Running the classifier

Running the application in the main mode, listening for input data, requires three items:

1. an input folder
1. an output folder
1. a classifier model

Both the input and output folder are assumed to be under the same umbrella directory, called `marketplace`, supplied to
the application at runtime.

It is recommended to have the `marketplace` directory placed in the project's `data` directory:

```
.
├── backend
│   ├── keychain
│   ├── notebook
│   └── src
├── data
│   └── marketplace
│        ├── input
│        └── output
└── frontend
```

The marketplace is the drop point for input images and output results. To run the application, listening in the `input`
folder for data, provide a path to the classifier model.

```
python main.py --classify --model PATH_TO_MODEL --marketplace PATH_TO_MARKETPLACE_ROOT --classes PATH_TO_CLASS_FOLDER
```

### Marketplace

'Marketplace' is the point of interaction with the front end application. Any file placed in the `marketplace/input`
directory is examined, processed, if it is an image, and always deleted. The results of the classifier is then placed in
the `marketplace/output` folder as a `json` file with the following schema:

```json
{
   "name": "input-name",
   "predictions": {
      "class1": "probability of class 1",
      "class2": "probability of class 2",
      "classN": "probability of class N"
   }
}
```

The output file is named identically to the input file, differing only in file extension, i.e. for an input `foo.png`,
the output file is `foo.json`.

## Data

Currently, the goal of the classification is to distinguish common genus'. To that end,
the [Mushrooms classification - Common genus's images](https://www.kaggle.com/maysee/mushrooms-classification-common-genuss-images)
is used. To download and prepare this dataset, a notebook is provided:

```
backend/notebook/dataset downloader.ipynb
```

In order to download the data using Kaggle API, you will need an [API token](https://www.kaggle.com/docs/api). Place
the `json` file containing your credentials in the `backend/keychain/kaggle`
folder.

*Note: Kaggle data can usually be downloaded without the token, but you will have to update the downloading notebook
accordingly.*

## Training a new model

In order to train a model, the programme needs data to learn from. There are two requirements:

1. Images have to be sorted into folders with their class names.
1. Data has to be split into a training and testing subset. An example of the required data structure is as follows:

```
.
└── data
    └── image-database
        └── maysee-mushrooms-classification-common-genuss-images
            ├── test
            │   ├── Agaricus
            │   ├── Amanita
            │   ├── Boletus
            │   ├── Cortinarius
            │   ├── Entoloma
            │   ├── Hygrocybe
            │   ├── Lactarius
            │   ├── Russula
            │   └── Suillus
            └── train
                ├── Agaricus
                ├── Amanita
                ├── Boletus
                ├── Cortinarius
                ├── Entoloma
                ├── Hygrocybe
                ├── Lactarius
                ├── Russula
                └── Suillus
```

To commence training, add the `--train` flag, as well as provide a path to the `train` and `test` folders.

```
python main.py --train --train-data PATH_TO_TRAIN_DATA_FOLDER --test-data PATH_TO_TEST_DATA_FOLDER
```

## Classification results

| Dataset | Performance | Number of Epochs | Resolution | Activation function | Momentum | Batch size | Learn rate |
| ------- | ----------- | ---------------- | ---------- | ------------------- | -------- | ---------- | ---------- |

# To-do list

- [x] Local running script
- [x] Listening for folder changes
- [x] Find a high performance model
- [ ] Transform into a web application
- [ ] Record runs in the Classification results table
- [ ] Find new data sources
- [ ] Tied with the above, find a finer labeled dataset
- [ ] Develop a phone application
- [ ] Remove the need to include a folder of classes for a classifier (Have a 'hard coded' list stored, or maybe provide
  file with list at runtime? FOLDER WITH CLASS NAMES MAY NOT BE AVAILABLE, ESPECIALLY IF NO TRAINING OCCURS AND MODEL IS
  JUST PROVIDED).
