#To calcuktae percentagebof pages in a book
book=input('enter name of book you\'re reading:\n')
page=input('which page are you on?\n')
total=input(f'what is tge total number of pages in {book} ?\n')

percentage= ((int(page)/int(total))*100)
close= (100 - percentage)
if close==0:
	print (f'you\'re done with reading {book}')
elif percentage==0:
	print('you havn\'t started the book')
else:
	print(f'you have read {percentage} percent of the book titled {book} and you are {close} percent closer to completing it.')