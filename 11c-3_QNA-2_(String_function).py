


'''String fountions'''
# len/leanth  = (total word and gap numbers)
story = "once upon a time there was a millioner name fayad who get 1 miilion in every month"
print(len(story))                    # 82   
 


# endswith  = (any lines last letter/word)
story = "once upon a time there was a millioner name fayad who get 1 million in every month"
print(story.endswith("h"))          # true
print(story.endswith("month"))      # true
print(story.endswith("bye"))        # false



# count  = (how much time the letter/word is use)
story = "once upon a time there was a millioner name fayad who get miilion in every month"
print(story.count("o"))             # o (6 times)
print(story.count("a"))             # a (6 times)
print(story.count("t"))             # t (4 times)
print(story.count("z"))             # z (0 time)
print(story.count("was"))           # was (1 time)
print(story.count("fayad"))         # fayad (1 time)



# find  = (positon in len)
story = "once upon a time there was a millioner name fayad who get 1 miilion in every month"
print(story.find("fayad"))          # 44   position
print(story.find("millioner"))      # 29   position
print(story.find("Big"))            # -1   no position
print(story.find("a"))              # 10   position but in story there was 2 alone (a) so (find) took first one only



# replace
story = "once upon a time there was a millioner name fayad who get 1 miilion in every month"
print(story.replace("fayad","azmain taosif fayad"))     # (fayad) change with (azmain taosif fayad)
print(story.replace("month","week"))                    # (month) change with (week)

