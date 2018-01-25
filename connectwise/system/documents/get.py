def get_documents(client, record_type, db_rid, page_size=1000, verbose=False):
    parameters = {
        "recordId": db_rid,
        "recordType": record_type,
        "pageSize": page_size

    }
    print(parameters)
    if verbose is True: print(parameters)
    return client._get("/system/documents/", parameters=parameters)

