"""Functions to help Azara and Rui locate pirate treasure."""


def get_coordinate(record):
    return record[1]


def convert_coordinate(coordinate):
    return tuple(coordinate)


def compare_records(azara_record, rui_record):
    azara = tuple(azara_record[1])
    return azara == rui_record[1]



def create_record(azara_record, rui_record):
    if compare_records(azara_record,rui_record):
        return azara_record+rui_record
    else:
        return "not a match"


def clean_up(combined_record_group):
    return '\n'.join([str((rec[0],rec[2],rec[3],rec[4])) for rec in combined_record_group]) + '\n'
