letter='''Dear <|NAME|>,     
  Greetings from infosys,
       I am glad to tell you that, your selected for Advance round in infytq.
Thanks and regards.
<|DATE|>
'''
name=input("Enter the name: \n")
date=input("Enter the date: \n")
letter=letter.replace("<|NAME|>",name)
letter=letter.replace("<|DATE|>",date)
print(letter)