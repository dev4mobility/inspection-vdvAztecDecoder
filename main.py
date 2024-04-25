import zxing


def main():
    reader = zxing.BarCodeReader()
    barcode = reader.decode("hvvSwitchAztec.png")
    print(barcode)
    decoded_barcode = decode(barcode.raw)
    print(f"This are the HEX Values: {decoded_barcode}")
    barcode_slices(decoded_barcode)


def barcode_slices(decoded_barcode):
    print(f"Position of 0x9e: {decoded_barcode.index('0x9e')}")
    print(f"Position of 0x9a: {decoded_barcode.index('0x9a')}")
    pass  # TODO seperate Barcode Hex Values in different slices for each TAG, like Signature, Certificate


def decode(barcode):
    # barcode_raw = "\x9e\x81\x800@\x9a\n\x06Ú0¤\x16\x8cõ¤tý-A(l\x1dC\x99¤ìµ\x7fÛ°E\x85Y\x0e0dU3&Õ;ÄÒ\x9c»åH¸\x94\x86\x80fñ¿8\x06´\x1a¥:Zèåµ\x9e¥\x9fY\x04×\x02¹)\x93!\x7fe\x8dâ\x87ÍM\x86\x82\x03wb©ZÊ©òÓí¢QË\x10¥AõÀSMÍÉ^3s\xadgE)Æov-TH2¹\x8es\x16\x13÷W¸)ò1\x9a\x05VDV\x18\x00\x7f!\x81È_7\x81ÀÆ1k\xa0õ*ïY3ú\n\x99õÊh\x95g)\x0fX\x15[G0K\x07\\\x90#*\x8e\r\x7fkä¬\x80Ù²¥ÍÉb¦TådG#O6|nn\x1bßW¼Nv\x14g¹mÊddü!z«\x14\xa0\x90¨Pæí\x1aå\x93ß3Ö2ÄP\x7f`9:NØ¹÷Z[,§üðG\x96-Û¤\x06gtEIGí®\x06é&¥\x8c\x9fé\x89DÊ\x03NZ\x03Ý\nQÒ\x16C\x0f\x99\x8b+JY\x02\x8aàñ¹\x05\x8cx\x8d½°\x8bE·×ü_\x0fÖ\x1dzà\x9f¶|\x15?Ð¿Øá\x97U\xa0.©g*Ú\x8d^ry£@\x9b\x1bº¯¸@Â_8\x01\x81B\x08DEVDV\x15\x04!"
    barcode_raw = barcode
    print(f"This ist the raw Barcode Data: {barcode_raw}")
    decoded_barcode: list = []  # create empty list
    for i in range(len(barcode_raw)):
        barcode_ascii = ord(barcode_raw[i])  # change each character to ASCII code
        barcode_hex = hex(barcode_ascii)  # convert ascii code to hex
        print(f"RAW: {barcode_raw[i]}, ASCII: {barcode_ascii} HEX: {barcode_hex}")
        decoded_barcode.append(barcode_hex)  # add hex code to decrypted list.
    # print(decoded_barcode)
    # print(type(decoded_barcode))
    print(f"Length of Barcode in Byte: {len(decoded_barcode)}")
    print(f"Count of 0x9e {decoded_barcode.count('0x9e')}")
    print(f"Count of 0x9a {decoded_barcode.count('0x9a')}")
    return decoded_barcode


if __name__ == '__main__':
    main()
