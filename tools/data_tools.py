import json


def trans_json_for_key(j, key):
    try:
        if key in j:
            if key.startswith('htsusRate'):
                try:
                    return f"{float(j[key]) * 100}%"
                except ValueError:
                    return j[key]
            else:
                return j[key] if j[key] is not None else ''
        else:
            return ''
    except json.JSONDecodeError:
        return ''


def check_json_for_key(j, key):
    try:
        if key in j:
            return True
        else:
            return False
    except json.JSONDecodeError:
        return False


def add_commas(string):
    return "{:,.2f}".format(float(string))
