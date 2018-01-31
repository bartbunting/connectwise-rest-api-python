def create_new_note(client, ticket, text,
                    detail_description=True, internal_analysis=False, resolution=False,
):
    data = {
        "text": text,
        #"member": {"id": 161},
        "detailDescriptionFlag": detail_description,
        "internalAnalysisFlag": internal_analysis,
                "resolutionFlag": resolution,
    }

    return client._post('/service/tickets/%d/notes/' %(int(ticket)), json=data)
