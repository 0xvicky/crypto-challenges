import base64


def convert_to_bytes(hexaDeci):
    return bytes.fromhex(hexaDeci)


hex_bytes = "72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf"

byte_res = convert_to_bytes(hex_bytes)


def bytes_to_base64(bytes_data):
    base64_res = base64.b64encode(bytes_data)
    print(base64_res)


bytes_to_base64(byte_res)
