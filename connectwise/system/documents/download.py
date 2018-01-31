def download_document(client, db_rid, verbose=False):
    url = "/system/documents/%(id)s/download/" % {
        'id': db_rid,
    }
    parameters = {}
    
    #return client._get(url, parameters=parameters)
    return client._get(url, parameters=parameters)
