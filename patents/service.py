from datetime import datetime
import spacy
from rest_framework.exceptions import ValidationError


custom_nlp = spacy.load('patents/chem_model')
nlp = spacy.load("en_core_web_sm")


def to_datetime(timestamp_string, silent_fail=False):
    """ Function converts a datetime string in to datetime object """
    for date_fmt in ('%m/%d/%Y %H:%M:%S', '%m-%d-%Y %H:%M:%s', '%m-%d-%y %H:%M:%s', '%m/%d/%y %H:%M:%s',
                     '%m/%d/%Y %I:%M:%S %p', '%m/%d/%Y %H:%M:%S %p', '%d/%m/%Y %H:%M:%S'):
        try:
            datetime_obj = datetime.strptime(timestamp_string, date_fmt)
            return datetime_obj
        except (ValueError, TypeError) as e:
            pass
    if not silent_fail:
        raise ValidationError('Invalid date format, please enter in MM/DD/YYYY hh:mm:ss format')
    else:
        return None


def get_abstract(element):
    """ Function to get text of Abstract Tag """
    s = ""
    for i in element:
        if i.tag == 'p':
            for j in i:
                s += j.tail.strip()

    return s


def get_description(element):
    """ Function to get text of Description Tag """
    s = ""
    for i in element:
        if i.tag == 'heading':
            continue

        if i.tag == 'p':
            s += i.text.strip()
            for j in i:
                s += j.tail.strip()
    return s


def get_general_entities(text):
    doc = nlp(text)
    entities = [(e.text, e.label_) for e in doc.ents]
    return str(entities).strip('[]')


def get_custom_entitites(text):
    d = custom_nlp(text)
    entities = [(e.text, e.label_) for e in d.ents]
    return str(entities).strip('[]')
