import os

if os.path.exists('Donkey.txt') == False:
    print('File does not exist')

with open('Donkey.txt', 'r') as file:
    content = file.read()
    Count = content.count('donkey')
    print(f'The word "donkey" appears {Count} times in the file.')
new_content = content.replace('donkey', 'Twinkle')

with open('Donkey.txt', 'w') as file:
    file.write(new_content)
print('All occurrences of "donkey" have been replaced with "Twinkle".')