# addid

adds (url-safe) base64 encoded ids (without padding) to given finc Solr schema conform line-delimited JSON

adds "id" field to given finc Solr schema conform line delimited JSON, whereby the ID will be constructed with following pattern:

    [PREFIX]-[SOURCE ID]-[RECORD ID]

 * PREFIX will be taken from the parameter "-prefix"
 * SOURCE ID will be taken from field "source_id" of the JSON record
 * RECOURD ID will be taken from field "record_id" of the JSON record

## usage

    addid.py -prefix [PREFIX] < [INPUT FINC SOLR SCHEMA CONFORM LINE-DELIMITED JSON] > [OUTPUT ENHANCED FINC SOLR SCHEMA CONFORM LINE-DELIMITED JSON]

(default prefix is "dswarm")
