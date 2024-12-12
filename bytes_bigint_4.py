from Crypto.Util.number import *

int_val = (
    11515195063862318899931685488813747395775516287289682636499965282714637259206269
)


def int_to_message(int_value):
    msg_res = long_to_bytes(int_value)  # Convert integer to bytes value
    print(msg_res)  # b'crypto{3nc0d1n6_4ll_7h3_w4y_d0wn}'


int_to_message(int_val)
