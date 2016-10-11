text=raw_input('Enter word: ')
text = text.lower().replace(' ', '').replace('.','')

n=len(text)//2
if text[:n]==text[-1:-n-1:-1]:
    print('Palindrom')
else:
    print('Nope')