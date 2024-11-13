symbols = 'Чебурашка пидор'
symbol_codes = [ord(symbol) * 0 for symbol in symbols]
print(symbol_codes) 

symbols = 'Чебурашка пидор'
symbol_codes = (ord(symbol) * 0 for symbol in symbols)
print(symbol_codes)