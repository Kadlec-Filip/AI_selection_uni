﻿from collections import Counter

# Funkce pro zakódování zprávy
def encrypt(text, key):
    encrypted_msg = ""
    text = text.upper()
    for i in range(len(text)):
        if text[i].isalpha():
            if ord(text[i]) + key > 90:
                shifted_letter = chr(ord(text[i]) + key - 26)
                encrypted_msg += shifted_letter
            else:
                shifted_letter = chr(ord(text[i]) + key)
                encrypted_msg += shifted_letter
        else:
            encrypted_msg += text[i]
    return encrypted_msg

# Funkce pro dekódování zprávy
def decrypt(encrypted_msg, most_common_letters_eng):
    array_of_letters = []

    # převod textového řetězce na pole charů kvůli následné jednodušší manipulaci
    for i in encrypted_msg:
        if i.isalpha():
            array_of_letters.append(i)

    # Počet jednotlivých znaků
    frequency = Counter(array_of_letters)
    # Seřazené znaky podle četnosti
    letters_by_freq = sorted(frequency, key=frequency.get, reverse=True)

    # jen prevod charu na ascii num, kvuli str.translate()
    for i in range(len(letters_by_freq)):
        letters_by_freq[i] = ord(letters_by_freq[i])
    for i in range(len(most_common_letters_eng)):
        most_common_letters_eng[i] = ord(most_common_letters_eng[i])

    dictionary = dict(zip(letters_by_freq, most_common_letters_eng))
    decrypted_msg = encrypted_message.translate(dictionary)

    return decrypted_msg


txt = "It was a bright cold day in April, and the clocks were striking thirteen. Winston Smith, his chin nuzzled into" \
      " his breast in an effort to escape the vile wind, slipped quickly through the glass doors of Victory Mansions, " \
      "though not quickly enough to prevent a swirl of gritty dust from entering along with him.The hallway smelt of " \
      "boiled cabbage and old rag mats. At one end of it a coloured poster, too large for indoor display, had been " \
      "tacked to the wall. It depicted simply an enormous face, more than a metre wide: the face of a man of about " \
      "forty-five, with a heavy black moustache and ruggedly handsome features. Winston made for the stairs. It was " \
      " no use trying the lift. Even at the best of times it was seldom working, and at present the electric current " \
      "was cut off during daylight hours. It was part of the economy drive in preparation for Hate Week. The flat was " \
      "seven flights up, and Winston, who was thirty-nine and had a varicose ulcer above his right ankle, went slowly," \
      " resting several times on the way. On each landing, opposite the lift-shaft, the poster with the enormous face " \
      "gazed from the wall. It was one of those pictures which are so contrived that the eyes follow you about when you" \
      " move. BIG BROTHER IS WATCHING YOU, the caption beneath it ran. Inside the flat a fruity voice was reading out " \
      "a list of figures which had something to do with the production of pig-iron. The voice came from an oblong metal " \
      "plaque like a dulled mirror which formed part of the surface of the right-hand wall. Winston turned a switch and" \
      " the voice sank somewhat, though the words were still distinguishable. The instrument (the telescreen, it was" \
      " called) could be dimmed, but there was no way of shutting it off completely. He moved over to the window: a " \
      "smallish, frail figure, the meagreness of his body merely emphasized by the blue overalls which were the uniform " \
      "of the party. His hair was very fair, his face naturally sanguine, his skin roughened by coarse soap and blunt " \
      "razor blades and the cold of the winter that had just ended. Outside, even through the shut window-pane, the " \
      "world looked cold. Down in the street little eddies of wind were whirling dust and torn paper into spirals, and" \
      " though the sun was shining and the sky a harsh blue, there seemed to be no colour in anything, except the posters" \
      " that were plastered everywhere. The blackmoustachio'd face gazed down from every commanding corner. There was " \
      "one on the house-front immediately opposite. BIG BROTHER IS WATCHING YOU, the caption said, while the dark eyes" \
      " looked deep into Winston's own. Down at streetlevel another poster, torn at one corner, flapped fitfully in the " \
      "wind, alternately covering and uncovering the single word INGSOC. In the far distance a helicopter skimmed down " \
      "between the roofs, hovered for an instant like a bluebottle, and darted away again with a curving flight. It was" \
      " the police patrol, snooping into people's windows. The patrols did not matter, however. " \
      "Only the Thought Police mattered. Behind Winston's back the voice from the telescreen was still babbling away" \
      " about pig-iron and the overfulfilment of the Ninth Three-Year Plan. The telescreen received and transmitted " \
      "simultaneously. Any sound that Winston made, above the level of a very low whisper, would be picked up by it, " \
      "moreover, so long as he remained within the field of vision which the metal plaque commanded, he could be seen" \
      " as well as heard. There was of course no way of knowing whether you were being watched at any given moment. " \
      "How often, or on what system, the Thought Police plugged in on any individual wire was guesswork. It was even" \
      " conceivable that they watched everybody all the time. But at any rate they could plug in your wire whenever " \
      "they wanted to. You had to live -- did live, from habit that became instinct -- in the assumption that every " \
      "sound you made was overheard, and, except in darkness, every movement scrutinized. Winston kept his back turned " \
      "to the telescreen. It was safer, though, as he well knew, even a back can be revealing. A kilometre away the" \
      " Ministry of Truth, his place of work, towered vast and white above the grimy landscape. This, he thought with" \
      " a sort of vague distaste -- this was London, chief city of Airstrip One, itself the third most populous of the" \
      " provinces of Oceania. He tried to squeeze out some childhood memory that should tell him whether London had " \
      "always been quite like this. Were there always these vistas of rotting nineteenth-century houses, their sides" \
      " shored up with baulks of timber, their windows patched with cardboard and their roofs with corrugated iron," \
      " their crazy garden walls sagging in all directions? And the bombed sites where the plaster dust swirled in" \
      " the air and the willow-herb straggled over the heaps of rubble; and the places where the bombs had cleared" \
      " a larger patch and there had sprung up sordid colonies of wooden dwellings like chicken-houses? But it was " \
      "no use, he could not remember: nothing remained of his childhood except a series of bright-lit tableaux " \
      "occurring against no background and mostly unintelligible. The Ministry of Truth -- Minitrue, in Newspeak --" \
      " was startlingly different from any other object in sight. It was an enormous pyramidal structure of glittering " \
      "white concrete, soaring up, terrace after terrace, 300 metres into the air. From where Winston stood it was" \
      " just possible to read, picked out on its white face in elegant lettering, the three slogans of the Party:" \
      "WAR IS PEACE" \
      "FREEDOM IS SLAVERY " \
      "IGNORANCE IS STRENGTH" \
      "The Ministry of Truth contained, it was said, three thousand rooms above ground level, and corresponding " \
      "ramifications below. Scattered about London there were just three other buildings of similar appearance and " \
      "size. So completely did they dwarf the surrounding architecture that from the roof of Victory Mansions you " \
      "could see all four of them simultaneously. They were the homes of the four Ministries between which the entire " \
      "apparatus of government was divided. The Ministry of Truth, which concerned itself with news, entertainment," \
      " education, and the fine arts. The Ministry of Peace, which concerned itself with war. The Ministry of Love," \
      " which maintained law and order. And the Ministry of Plenty, which was responsible for economic affairs. " \
      "Their names, in Newspeak: Minitrue, Minipax, Miniluv, and Miniplenty. " \
      "The Ministry of Love was the really frightening one. There were no windows in it at all." \
      " Winston had never been inside the Ministry of Love, nor within half a kilometre of it. It was a place" \
      " impossible to enter except on official business, and then only by penetrating through a maze of barbed-wire" \
      " entanglements, steel doors, and hidden machine-gun nests. Even the streets leading up to its outer barriers " \
      "were roamed by gorilla-faced guards in black uniforms, armed with jointed truncheons." \
      " Winston turned round abruptly. He had set his features into the expression of quiet optimism which it was" \
      " advisable to wear when facing the telescreen. He crossed the room into the tiny kitchen. By leaving the " \
      "Ministry at this time of day he had sacrificed his lunch in the canteen, and he was aware that there was no " \
      "food in the kitchen except a hunk of dark-coloured bread which had got to be saved for tomorrow's breakfast." \
      " He took down from the shelf a bottle of colourless liquid with a plain white label marked VICTORY GIN. It " \
      "gave off a sickly, oily smell, as of Chinese ricespirit. Winston poured out nearly a teacupful, nerved himself " \
      "for a shock, and gulped it down like a dose of medicine. Instantly his face turned scarlet and the water ran" \
      " out of his eyes. The stuff was like nitric acid, and moreover, in swallowing it one had the sensation of" \
      " being hit on the back of the head with a rubber club. The next moment, however, the burning in his belly" \
      " died down and the world began to look more cheerful. He took a cigarette from a crumpled packet marked" \
      " VICTORY CIGARETTES and incautiously held it upright, whereupon the tobacco fell out on to the floor. " \
      "With the next he was more successful. He went back to the living-room and sat down at a small table that" \
      " stood to the left of the telescreen. From the table drawer he took out a penholder, a bottle of ink, and a" \
      " thick, quarto-sized blank book with a red back and a marbled cover. For some reason the telescreen in the" \
      " living-room was in an unusual position. Instead of being placed, as was normal, in the end wall, where it " \
      "could command the whole room, it was in the longer wall, opposite the window. To one side of it there was a " \
      "shallow alcove in which Winston was now sitting, and which, when the flats were built, had probably been" \
      " intended to hold bookshelves. By sitting in the alcove, and keeping well back, Winston was able to remain " \
      "outside the range of the telescreen, so far as sight went. He could be heard, of course, but so long as he " \
      "stayed in his present position he could not be seen. It was partly the unusual geography of the room that had" \
      " suggested to him the thing that he was now about to do. " \
      "But it had also been suggested by the book that he had just taken out of the drawer. It was a peculiarly" \
      " beautiful book. Its smooth creamy paper, a little yellowed by age, was of a kind that had not been " \
      "manufactured for at least forty years past. He could guess, however, that the book was much older than " \
      "that. He had seen it lying in the window of a frowsy little junk-shop in a slummy quarter of the town " \
      "(just what quarter he did not now remember) and had been stricken immediately by an overwhelming desire " \
      "to possess it. Party members were supposed not to go into ordinary shops ('dealing on the free market'," \
      " it was called), but the rule was not strictly kept, because there were various things, such as shoelaces " \
      "and razor blades, which it was impossible to get hold of in any other way. He had given a quick glance up" \
      " and down the street and then had slipped inside and bought the book for two dollars fifty. At the time he" \
      " was not conscious of wanting it for any particular purpose. He had carried it guiltily home in his briefcase." \
      " Even with nothing written in it, it was a compromising possession. The thing that he was about to do was" \
      " to open a diary. This was not illegal (nothing was illegal, since there were no longer any laws), but if" \
      " detected it was reasonably certain that it would be punished by death, or at least by twenty-five years in" \
      " a forced-labour camp. Winston fitted a nib into the penholder and sucked it to get the grease off. The pen" \
      " was an archaic instrument, seldom used even for signatures, and he had procured one, furtively and with " \
      "some difficulty, simply because of a feeling that the beautiful creamy paper deserved to be written on with" \
      " a real nib instead of being scratched with an ink-pencil. Actually he was not used to writing by hand. " \
      "Apart from very short notes, it was usual to dictate everything into the speakwrite which was of course " \
      "impossible for his present purpose. He dipped the pen into the ink and then faltered for just a second. A " \
      "tremor had gone through his bowels. To mark the paper was the decisive act. In small clumsy letters he " \
      "wrote:" \
      "April 4th, 1984."


most_common_letters_eng = ['E','T', 'A','O','I','N','S','R','H','L','D','C','U','M','F','P','G','W','Y','B','V','K',
                           'X', 'J','Q','Z']
key = 3

print("\nInput text: ")
print(txt)

encrypted_message = encrypt(txt, key)
print("\nEncrypted text: ")
print(encrypted_message)

decrypted_msg = decrypt(encrypted_message, most_common_letters_eng)
print("\nDecrypted text: ")
print(decrypted_msg)
