import time
import random

print('-'*65)
print('I am a fortune teller! ')
print()
question = input('What is your question? ')
time.sleep(0.7)
print('shocked!')
time.sleep(0.7)
print('.....thinking.....')
time.sleep(0.7)
print('.....thinking.....')
time.sleep(0.7)

choice = random.randint(2,4)

if choice == 1:
	print(' hmmm ')
elif choice == 2:
	print(' maybe? ')
elif choice == 3:
	print(' The answer is....? ')
elif choice == 4:
	print(' YES! ')
elif choice == 5:
	print(' Now run along? ')
elif choice == 6:
	print(' Be gone ')

print('-'*65)

