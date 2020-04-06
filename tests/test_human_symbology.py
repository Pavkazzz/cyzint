from pyzint.pyzint import Zint, BARCODE_QRCODE


def test_human_symbology():
    z = Zint("Barcode", BARCODE_QRCODE)
    assert z.symbology_name == "qrcode"
