sen = input("Sentence: ")

screen_width = 80

text_len = len(sen)

box_width= text_len + 6

left_margin = (screen_width - box_width) // 2

print()

print(' '*left_margin +'+'+'-'*(box_width-2) +'+')

print(' '*left_margin +'|'+sen +'|')

print(' '*left_margin +'+'+'-'*(box_width-2) +'+')
