from main import ascii_to_binary, ascii_to_string, string_to_ascii, binstr_to_ascii


def ascii_to_binary_test():
    assert (ascii_to_binary([98, 111, 110, 106, 111, 117, 114]) == (
        ['0b1100010', '0b1101111', '0b1101110', '0b1101010', '0b1101111', '0b1110101', '0b1110010']))
    assert (ascii_to_binary([64, 82, 68, 92, 81]) == (
        ['0b1000000', '0b1010010', '0b1000100', '0b1011100', '0b1010001']))
    assert (ascii_to_binary([120, 103, 116, 64, 95, 100]) == (
        ['0b1111000', '0b1100111', '0b1110100', '0b1000000', '0b1011111', '0b1100100']))
    assert (ascii_to_binary([120, 76, 91, 91, 105, 81]) == (
        ['0b1111000', '0b1001100', '0b1011011', '0b1011011', '0b1101001', '0b1010001']))
    assert (ascii_to_binary([74, 81, 92, 124, 95]) == (
        ['0b1001010', '0b1010001', '0b1011100', '0b1111100', '0b1011111']))


def ascii_to_string_test():
    assert ascii_to_string([66, 111, 110, 106, 111, 117, 114]) == "Bonjour"
    assert ascii_to_string([78, 83, 73]) == "NSI"
    assert ascii_to_string([80, 121, 116, 104, 111, 110]) == "Python"
    assert ascii_to_string([65, 98, 99]) == "Abc"
    assert ascii_to_string([120, 121, 90]) == "xyZ"


def string_to_ascii_test():
    assert string_to_ascii("bonjour") == [98, 111, 110, 106, 111, 117, 114]
    assert string_to_ascii("MeSsAgE SeCrEt") == [77, 101, 83, 115, 65, 103, 69, 32, 83, 101, 67, 114, 69, 116]
    assert string_to_ascii("Texte") == [84, 101, 120, 116, 101]
    assert string_to_ascii("James Bond") == [74, 97, 109, 101, 115, 32, 66, 111, 110, 100]
    assert string_to_ascii("007") == [48, 48, 55]


def binstr_to_ascii_test():
    assert binstr_to_ascii(
        ['0b1100010', '0b1101111', '0b1101110', '0b1101010', '0b1101111', '0b1110101', '0b1110010']) == [98, 111, 110,
                                                                                                         106, 111, 117,
                                                                                                         114]
    assert binstr_to_ascii(['0b1000000', '0b1010010', '0b1000100', '0b1011100', '0b1010001']) == [64, 82, 68, 92, 81]
    assert binstr_to_ascii(['0b1111000', '0b1100111', '0b1110100', '0b1000000', '0b1011111', '0b1100100']) == [120, 103,
                                                                                                               116, 64,
                                                                                                               95, 100]
    assert binstr_to_ascii(['0b1111000', '0b1001100', '0b1011011', '0b1011011', '0b1101001', '0b1010001']) == [120, 76,
                                                                                                               91, 91,
                                                                                                               105, 81]
    assert binstr_to_ascii(['0b1001010', '0b1010001', '0b1011100', '0b1111100', '0b1011111']) == [74, 81, 92, 124, 95]
