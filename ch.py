import  hashlib

arquivo1 = 'a.txt'  #  Variável 1
arquivo2 = 'b.txt'  #  Variável 2

hash1 = hashlib.new('ripemd160')  #  Variável que recebe um tipo de hash, nesse caso ripemd160 bits.

hash1.update(open(arquivo1, 'rb').read())  #  Abre e lê 'r' arquivo em modo 'b' binário.

hash2 = hashlib.new('ripemd160')  #  Variável que recebe um tipo de hash, nesse caso ripemd160 bits.

hash2.update(open(arquivo2, 'rb').read())  #  Abre e lê 'r' arquivo em modo binário 'b'.

if hash1.digest() != hash2.digest():  #  Digest resume os dados do hash passado pelo update.
    print(f'O arquivo: {arquivo1} é diferente do arquivo: {arquivo2}')  #  Imprime descrição.
    print('O hash do arquivo a.txt é: ', hash1.hexdigest())  #  Resume o hash em exadecimal com hexdigest e imprime.
    print('O hash do arquivo b.txt é: ', hash2.hexdigest())  #  Resume o hash em exadecimal com hexdigest e imprime.
else:
    print(f'O arquivo: {arquivo1} é igual ao arquivo: {arquivo2}')  #  Imprime descrição.
    print('O hash do arquivo a.txt é: ', hash1.hexdigest())  # Resume o hash em exadecimal com hexdigest e imprime.
    print('O hash do arquivo b.txt é: ', hash2.hexdigest())  # Resume o hash em exadecimal com hexdigest e imprime.