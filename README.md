# addid

adds (url-safe) base64 encoded ids (without padding) to given finc Solr schema conform line-delimited JSON

adds "id" field to given finc Solr schema conform line delimited JSON, whereby the ID will be constructed with following pattern:

    [PREFIX]-[SOURCE ID]-[RECORD ID]

 * PREFIX will be taken from the parameter "-prefix"
 * SOURCE ID will be taken from field "source_id" of the JSON record
 * RECOURD ID will be taken from field "record_id" of the JSON record

## requirements

* [argparse](https://docs.python.org/3/library/argparse.html#module-argparse)

### install requirements

1. (optionally) install [pip](https://pip.pypa.io/) for Python 3.x:

    sudo apt-get install python3-pip

2. install requirements with pip:

    sudo -H pip3 install -r requirements.txt

## usage

    addid.py -prefix [PREFIX] < [INPUT FINC SOLR SCHEMA CONFORM LINE-DELIMITED JSON] > [OUTPUT ENHANCED FINC SOLR SCHEMA CONFORM LINE-DELIMITED JSON]

(default prefix is "dswarm")
