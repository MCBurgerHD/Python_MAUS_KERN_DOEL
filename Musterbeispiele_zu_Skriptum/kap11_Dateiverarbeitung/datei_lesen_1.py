try:
    # Textdatei zeilenweise auslesen
    f2 = open('testfile.txt', 'r')    # r+t oder rt+
    print(f2)                   # <_io.TextIOWrapper name='testfile.txt' mode='r+' encoding='cp1252'>
    
    print(f2.read())            # Text1
                                # Text2
                                # nochText
    f2.close()
    f2 = open('unterordner/testfile.txt', 'rb')   # Binär
    print(f2.read())            # b'Text1\r\nText2\r\nnochText\r\n'
    f2.close()
except BaseException as err:
    print('Fehler:', err)