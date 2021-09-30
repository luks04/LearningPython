def serializer(dict_to_serialize: dict, database_data: dict, custom_key: str = None) -> dict:
    serialized_dict = dict()
    for key in database_data:
        try:
            if custom_key is not None:
                dict_to_serialize[key] = dict_to_serialize[custom_key]
            if type(database_data[key]) is dict:
                serialized_dict[key] = serializer(dict_to_serialize, database_data[key], key)
            else:
                value = dict_to_serialize[key] if key in dict_to_serialize.keys() else ''
                serialized_dict[key] = database_data[key].strip() if value else ''
        except Exception as error:
            print(">>> ERROR: ", error)
    return serialized_dict

if __name__ == "__main__":
    sample_dict = {
        "key_2": False,
        "key_3": {
            "key_3.1": False,
            "key_3.2": True,
        },
        "key_5": True,
    }

    database_sample_dict = {
        "key_1": "Something",
        "key_2": "Else",
        "key_3": {
            "key_3.1": "One",
            "key_3.2": "Word",
            "key_3.3": {
                "key_3.3.1": {
                    "key_3.3.1.1": "Any",
                    "key_3.3.1.2": "Thing",
                    "key_3.3.1.3": "Random",
                }
            },
        },
        "key_4": "Data",
        "key_5": "Value",
    }

    print(serializer(sample_dict, database_sample_dict))
    '''
        {'key_1': '', 
         'key_2': '', 
         'key_3': {
             'key_3.1': 'One', 
             'key_3.2': 'Word', 
             'key_3.3': {
                 'key_3.3.1': {
                     'key_3.3.1.1': 'Any', 
                     'key_3.3.1.2': 'Thing', 
                     'key_3.3.1.3': 'Random'
                  }
             }
         }, 
         'key_4': '', 
         'key_5': 'Value'}
    '''
