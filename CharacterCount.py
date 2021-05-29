
london = "Romeo and Juliet Summary. An age-old vendetta between two powerful families erupts into bloodshed. A group of masked Montagues risk further conflict by gatecrashing a Capulet party. A young lovesick Romeo Montague falls instantly in love with Juliet Capulet, who is due to marry her father's choice, the County Paris.!!!"

frequency = dict()

for character in london:
    if character in frequency:
        frequency[character] +=1
    else:
        frequency[character] =1


for letter, count in frequency.items():
    print(letter, ':', count)
