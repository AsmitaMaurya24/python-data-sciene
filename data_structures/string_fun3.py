from data import story
print(f'total chars in the story: {len(story)}')
words = story.split()
print(f'total chars in the story: {len(words)}')
print(f'rotal unique words in the story: {len(set(words))}')
print(words)

sentences = story.split('.')
print(f'total sentences in the story: {len(set(sentences))}')

lines = story.split('\n')
print(f'total lines in the story: {len(set(lines))}')
print(lines)

poem_list = [
    'Twinkle, twinkle, little star,',
    'How I wonder what you are!',
    'Up above the world so high,',
    'Like a diamond in the sky.',
]
poem  = '\n'.join(poem_list)
print(poem,'\n')


poem_list2 = [
    'Jhonny Jhonny yes papa',
    'Eating sugar no papa',
    'Telling allies no papa',
    'open you mouth',
    'ha ha ha.',

]
poem = '\n'.join(poem_list2)
print(poem,'\n')

