from PIL import Image

from main import change_pixel_value, get_pixel_value, decrypt, encrypt

default_img = Image.open("test.png")


def change_pixel_value_test():
    image = default_img
    change_pixel_value(image, 0, 0, 255, 255, 255)
    assert (get_pixel_value(image, 0, 0) == (255, 255, 255))
    change_pixel_value(image, 10, 20, 40, 50, 60)
    assert (get_pixel_value(image, 10, 20) == (40, 50, 60))
    change_pixel_value(image, 50, 200, 20, 20, 60)
    assert (get_pixel_value(image, 50, 200) == (20, 20, 60))
    change_pixel_value(image, 99, 66, 11, 88, 123)
    assert (get_pixel_value(image, 99, 66) == (11, 88, 123))
    change_pixel_value(image, 168, 190, 123, 45, 67)
    assert (get_pixel_value(image, 168, 190) == (123, 45, 67))


def test_encrypt_decrypt():
    image = default_img
    image = encrypt("Welkom avonturier!", image)
    assert (decrypt(image) == "Welkom avonturier!")

    image = default_img
    image = encrypt("JE SUIS uN OuRs PolAIre ?", image)
    assert (decrypt(image) == "JE SUIS uN OuRs PolAIre ?")

    image = default_img
    image = encrypt("Plein de charactère spéciaux @,;:!âôàèé", image)
    assert (decrypt(image) == "Plein de charactère spéciaux @,;:!âôàèé")

    image = default_img
    image = encrypt("Vamos a la plâîà", image)
    assert (decrypt(image) == "Vamos a la plâîà x)")

    image = default_img
    image = encrypt("k@rtoffèlé sàlât", image)
    assert decrypt(image) == "k@rtoffèlé sàlât"
