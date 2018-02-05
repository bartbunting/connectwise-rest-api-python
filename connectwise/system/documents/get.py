def get_documents(client, db_rid, record_type='ticket', verbose=False):
    parameters = {
        "recordId": db_rid,
        "recordType": record_type,
    }

    return client._get("/system/documents/", parameters=parameters)

