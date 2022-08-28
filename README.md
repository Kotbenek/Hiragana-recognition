# Hiragana recognition

WIP hiragana recognition utility

## Obtaining the ETL Character Database

To download *ETL Character Database*, you need to accept `Conditions of Use` and fill the `Registration Form` at [etlcdb.db.aist.go.jp](http://etlcdb.db.aist.go.jp).

## Extracting hiragana dataset

- Clone this repository:
`git clone https://github.com/Kotbenek/Hiragana-recognition.git`
- Unzip downloaded *ETL Character Database* files into ETL directory
- Unzip downloaded `unpack.zip` into repository root folder
- Run `create_dataset.sh` script consisting of:
    - Creation and setup of virtual python environment
    - *ETL Character Database* extraction
    - Hiragana dataset extraction
    - Minor samples cleanup
    - Samples size unification
    - (TODO) Creation of standardized text-based dataset files

## Classifier

TODO

## Character recognition

TODO

