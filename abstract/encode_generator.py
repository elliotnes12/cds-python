import json
import base64

def encode(json_par):
    """

    Codifica el json de entrada.

    :param json_par: json.
    :type json_par: str.
    :return: json encode
    :rtype: str
    """
    encoded_bytes = base64.b64encode(json_par.encode("utf-8"))
    encoded_str = str(encoded_bytes, "utf-8")
    return encoded_str


def decode(encoded_str):
    """

    Codifica el json de entrada.

    :param encoded_str: json.
    :type encoded_str: str.
    :return: json decode
    :rtype: str
    """
    decode_string = base64.b64decode(encoded_str)
    return json.loads(decode_string)


def read_json_config(path: str):
    """

    Codifica el json de entrada.

    :param path: str.
    :type path: str.
    :return: json config
    :rtype: json
    """
    file_path = path
    file = open(file_path, 'r')
    json_str = json.dumps(json.load(file))
    file.close()
    return json.loads(json_str)


def put_json(json_in: str):
    """
      print json response
    """
    print(str(json.dumps(json_in).rstrip()), end='')