from main import to_nine_bits


def to_nine_bits_test():
    assert to_nine_bits(["0001"]) == "000000001"
    assert to_nine_bits(["11001"]) == "000011001"
    assert to_nine_bits(["1"]) == "000000001"
    assert to_nine_bits(["0"]) == "000000000"
    assert to_nine_bits(["0", "0110", "1", "011"]) == "000000000000000110000000001000000011"
