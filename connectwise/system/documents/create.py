import os

def create_new_document(client, ticket, path):

    filename = os.path.basename(path)

    data = {
        'recordType': 'Ticket',
        'title': filename,
        'recordId': ticket
    }

    filenames = {'file': (filename, open(path, 'rb'))}

    #print(data)
    #print(filenames)

    return client._post_doc('/system/documents/', json=data, filenames=filenames)
