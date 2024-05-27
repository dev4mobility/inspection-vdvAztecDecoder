# Notes
## Infos from Heiko Sasse 
Hi Sebastian,
 
ja, das ist nicht ganz trivial.
 
Nehmen wir die folgenden Daten aus einem Level 1 Barcode (hattest du selber mal mit meiner App gescannt: https://pro.eticket.app/shareCardScan/5411/0a86e01093a4b6b6ad5763c9d5ce80308d9af70f0fd3339df4ee37757ad04781)
9E81807BB44C2D06541B9D844C270D780BA7B2D17C9CB72E334F06B105CCECD4DFBA993BEB6F7F6BFA089485DB30AC06894258B276794B34363478BF9F0B5FED2A1A8865198CBF8D001BD84A9C7BB6E3BFD83510E8B5E74F59105BD8436768DEDA53E84088B9F2D42D68AA9A757C895883BE0FF42772E1F94FB98FA57D09032B4C426B9A0F0516010000051602C1E356445600007F2181C85F3781C0563279CBCAD9FF8D89AE2EB95176C16B53A347A0A6F579929EC9DB833D36632E30B306BA99BD3E7C07CD919DC5E7DB8DB0038AF7D7C691FD709B26487ABDC03744C1F4549B7800B38EFD02EEAC5A45B00EE01FF158BE012D11541AF418B201121BDE9098F3BB147DA890FF20238233CB4724CC32B63B3A1C325CAC0882371ACD74EDA6FE23495C6E2EC43EFC1E73725D61BA8666793484788ABFED1367275837A3DEF5E0DF527D608BE707C79B4B41AB4A350943BA1C40DD66BDD9E54AF325025F38018142084445564456130218
 
Die einzelnen TLV Stukturen (mehrer auf der einer Ebene ohne gemeinsames Wurzelelement):
 
Tag 0x9E (L:128 / 0x8180): "Daten der Signatur"
- HexWerte: 7B B4 4C 2D 06 54 1B 9D - 84 4C 27 0D 78 0B A7 B2 
            D1 7C 9C B7 2E 33 4F 06 - B1 05 CC EC D4 DF BA 99 
            3B EB 6F 7F 6B FA 08 94 - 85 DB 30 AC 06 89 42 58 
            B2 76 79 4B 34 36 34 78 - BF 9F 0B 5F ED 2A 1A 88 
            65 19 8C BF 8D 00 1B D8 - 4A 9C 7B B6 E3 BF D8 35 
            10 E8 B5 E7 4F 59 10 5B - D8 43 67 68 DE DA 53 E8 
            40 88 B9 F2 D4 2D 68 AA - 9A 75 7C 89 58 83 BE 0F 
            F4 27 72 E1 F9 4F B9 8F - A5 7D 09 03 2B 4C 42 6B

Tag 0x9A (L:15 / 0x0F): "Restdaten der Signatur"
- HexWerte: 05 16 01 00 00 05 16 02 - C1 E3 56 44 56 00 00

Tag 0x7F21 (L:200 / 0x81C8): "CV Certificate"
. Tag 0x5F37 (L:192 / 0x81C0): "Signatur des Zertifikatsherausgebers"
. - HexWerte: 56 32 79 CB CA D9 FF 8D - 89 AE 2E B9 51 76 C1 6B 
.             53 A3 47 A0 A6 F5 79 92 - 9E C9 DB 83 3D 36 63 2E 
.             30 B3 06 BA 99 BD 3E 7C - 07 CD 91 9D C5 E7 DB 8D 
.             B0 03 8A F7 D7 C6 91 FD - 70 9B 26 48 7A BD C0 37 
.             44 C1 F4 54 9B 78 00 B3 - 8E FD 02 EE AC 5A 45 B0 
.             0E E0 1F F1 58 BE 01 2D - 11 54 1A F4 18 B2 01 12 
.             1B DE 90 98 F3 BB 14 7D - A8 90 FF 20 23 82 33 CB 
.             47 24 CC 32 B6 3B 3A 1C - 32 5C AC 08 82 37 1A CD 
.             74 ED A6 FE 23 49 5C 6E - 2E C4 3E FC 1E 73 72 5D 
.             61 BA 86 66 79 34 84 78 - 8A BF ED 13 67 27 58 37 
.             A3 DE F5 E0 DF 52 7D 60 - 8B E7 07 C7 9B 4B 41 AB 
.             4A 35 09 43 BA 1C 40 DD - 66 BD D9 E5 4A F3 25 02

. Tag 0x5F38 (L:1 / 0x01): "PK Remainer"
. - HexWerte: 81

Tag 0x42 (L:8 / 0x08): "Certificate Authority Reference (CAR)"
- HexWerte: 44 45 56 44 56 13 02 18
 
 
Die gekürzten Berechtigungsdaten (gemäß Kapitel 3 Standarddatenstruktur Statischer Berechtigungen, KA STB-Spec) stecken in der Signatur über die Daten:
Tag 0x9E (L:128 / 0x8180): "Daten der Signatur"
Tag 0x9A (L:15 / 0x0F): "Restdaten der Signatur"
 
Um die eigentlichen Daten zu bekommen, musst Du die Signatur „auswickeln“, also gemäß Kapitel 4 Sicherheitsmerkmale und Gesamtdatenstrukturen der Statischen Berechtigung, KA STB-Spec, aber rückwärts.
 
Du beginnst also mit dem angegebenen Sub-CA-Zertifikate der (44 45 56 44 56 13 02 18 = DE-VDV-13-02-14) und dem zugehörigen öffentlichen Root-Schlüssels.
Damit kannst Du dann den öffentlichen Schlüssel des SAMs aus dem Zertifikat in Tag 0x7F21 (L:200 / 0x81C8): "CV Certificate" „entschlüsseln“
und mit dem öffentlichen Schlüssel des SAMs dann wieder die Daten aus ser Signatur in Tag 0x9E (L:128 / 0x8180): "Daten der Signatur" und Tag 0x9A (L:15 / 0x0F): "Restdaten der Signatur" „entschlüsseln“.
 
Ich hoffe, dass bringt sich auf den richtigen Weg. Ist so ein bisschen matroschka-mäßig Image
 
Beste Grüße
Heiko Sasse