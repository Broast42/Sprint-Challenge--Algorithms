'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word, count=0):
    
    # TBC
    #if length of word is less than 2 return count -- base case
    if len(word) < 2:
        return count
    #if word at index 0 is = t and word at index 1 is h 
    if word[0] == 't' and word[1] == 'h':
        #add 1 to count
        count += 1
    #remove the first letter of the word
    word = word[1::]
    #call count_th with new trimed word and new count
    return count_th(word, count)
    
#print(count_th('ththth'))
