from tests.conversions_test import binstr_to_ascii_test, string_to_ascii_test, ascii_to_string_test, \
    ascii_to_binary_test
from tests.image_manipulation_test import change_pixel_value_test, test_encrypt_decrypt
from tests.special_characters_test import decode_special_characters_test, encode_special_characters_test
from tests.to_nine_bits_test import to_nine_bits_test

ascii_to_binary_test()
ascii_to_string_test()
string_to_ascii_test()
binstr_to_ascii_test()

encode_special_characters_test()
decode_special_characters_test()

to_nine_bits_test()

change_pixel_value_test()

test_encrypt_decrypt()
