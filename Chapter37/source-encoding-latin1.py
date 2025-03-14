# -*- coding: Latin-1 -*-

#----------------------------------------------------------------------------
# Demo all the ways to code non-ASCII text in Python, plus source encodings.
#
# If this file is saved as Latin-1 text, it works as is.  But changing the 
# coding line above to either ASCII or UTF-8 will then fail because the 
# Latin-1 0xc4 and 0xe8 saved in myStr1's value are not valid in either.
#
# A UTF-8 line works if this file is also saved as UTF-8 to make its mystr1 
# text match.  Because UTF-8 is the default for source, the line above is 
# optional if the file is saved as UTF-8 or its text is all UTF-8 compatible
# (e.g., ASCII, which is a subset of both the Latin-1 and UTF-8 encodings).
#----------------------------------------------------------------------------

myStr1 = 'AÄBèC'                                      # Raw, per source encoding

myStr2 = 'A\xc4B\xe8C'                                # Hex code-point escapes

myStr3 = 'A\u00c4B\U000000e8C'                        # Unicode short/long escapes

myStr4 = 'A' + chr(0xC4) + 'B' + chr(0xE8) + 'C'      # Concatenated code points

import sys, locale
print('Sys hosting platform: ', sys.platform)
print('Sys default encoding: ', sys.getdefaultencoding())
print('Open default encoding:', locale.getpreferredencoding(False))

for aStr in (myStr1, myStr2, myStr3, myStr4):
    print(f'{aStr}, strlen={len(aStr)}', end=', ')    # Decoded text+length

    bytes1 = aStr.encode()               # Default UTF-8: 2 bytes for accents
    bytes2 = aStr.encode('latin-1')      # Explicit Latin-1: 1 byte per char 
   #bytes3 = aStr.encode('ascii')        # ASCII fails: outside 0...127 range

    print(f'byteslen1={len(bytes1)}, byteslen2={len(bytes2)}')   # Encoded length
