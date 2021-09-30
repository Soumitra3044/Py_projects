import pywhatkit
print("Please enter the sentence to be converted to handwritten format")
n=input()
pywhatkit.text_to_handwriting(n,rgb=(0,0,255))
