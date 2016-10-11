text=raw_input('Enter word: ')
n=len(text)//2
if text[0:n:1]==text[-1:-n-1:-1]: # why this works?
    print('Palindrom')
else:
    print('Nope')
