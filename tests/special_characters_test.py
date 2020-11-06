from main import decode_special_characters, encode_special_characters


def encode_special_characters_test():
    assert encode_special_characters("blé@") == "blecutearobase"
    assert encode_special_characters("etnonilyenapa") == "etnonilyenapa"
    assert encode_special_characters("@kînîm@gîn@blé") == "arobasekichaponichapomarobasegichaponarobaseblecute"
    assert encode_special_characters("plutôt") == "plutochapot"
    assert encode_special_characters("pâlâlatîtèt") == "pachapolachapolatichapotegravet"


def decode_special_characters_test():
    assert decode_special_characters("blecutearobase") == "blé@"
    assert decode_special_characters("etnonilyenapa") == "etnonilyenapa"
    assert decode_special_characters("arobasekichaponichapomarobasegichaponarobaseblecute") == "@kînîm@gîn@blé"
    assert decode_special_characters("plutochapot") == "plutôt"
    assert decode_special_characters("pachapolachapolatichapotegravet") == "pâlâlatîtèt"
