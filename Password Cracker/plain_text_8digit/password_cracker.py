import time

def passwordCracker(password):
     startTime = time.time()
     letter = []
     with open('dictionary', 'r') as file:
          plain_text = (file.read().splitlines())
     Pw = password
     for x in range (0,len(Pw)):
          for y in range (0,len(plain_text)):
               if Pw[x] == plain_text[y]:
                letter.append(plain_text[y])
                #print(letter)
     Found_password = ''.join(letter)
     endtime = time.time()
     elapsedTime = endtime - startTime
     print(f'Password match : {Found_password}')
     print(f'It took {elapsedTime} seconds to crack!')


passwordCracker("Cool1234")