# 샘플 예제 # 'A-Z' -> 65-90(26) , 'a-z' -> 97-122(26)
word = 'Hello everyone, my name is duhyun!!!!'
push  = 3

def caesar_cipher(words,push) -> str:
    result=''
    for char in words:
        if char.isupper():
            result += chr((ord(char)+push-65)%26+65)
        elif char.islower():
            result += chr((ord(char)+push-97)%26+97)
        else :
            result += char
    return result

def encode(words,shift) -> str:
    return caesar_cipher(words,shift)

def decode(words,shift) -> str:
    return caesar_cipher(words,-shift)



print("init -> "+word)
print("encode -> "+encode(word,push))
print("decode -> "+decode(encode(word,push),push))