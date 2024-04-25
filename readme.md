# Summary 
This program decodes an Transit AZTEC Barcode with the Standard VDV KA. The definition of this standard is described 
in the document 'Statische Berechtigung'

# TODO List
- [ ] Create Slices 
- [ ] Add Document Statische Berechtigung to project
- [ ] Get Certificate 
- [ ] decrypt Signature
- [ ] check Values of decyrpted Signature

# Decode Aztec Barcode

## Read Barcode
First step is to read the Barcode. This is done with the module 'zxing'. The result is a byte string.   

## Decode Function 
This Function decodes the raw data from the barcode. For this step the raw data have to be converted to ASCII 
and then to HEX. With the HEX values the next steps can be done. 

## Slicing Function
`````
barcode_slices
`````


