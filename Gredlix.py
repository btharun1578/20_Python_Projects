def left_or_right(puzzel_matrix,words):
    #here only checking the words in rows
    words_formed=[]
    #Here we are cerating the words formed left to right and right to left and checking with the words  
    for each_list in puzzel_matrix:
        row_word="".join(each_list) #getting a word formed by left to right
        reverse_row_word="".join(each_list[::-1]) #getting a word formed by right to left 
        words_formed.extend([row_word,reverse_row_word])
    for each_word in words:
        for each_formed_word in words_formed:
            if(each_word in each_formed_word):
                #print(each_word)
                found_words.append(each_word)
                break
    #removing the find letters to search fast in upcoming process
    
    for each_word in found_words:
        words.remove(each_word) 

    if(word2 in found_words):
        length1=0
        length2=len(word2)
        length3=0
        #print("It is in Horizontal Way")

        for each_list in puzzel_matrix:
            row_word="".join(each_list) #getting a word formed by left to right
            reverse_row_word="".join(each_list[::-1]) #getting a word formed by right to left 
            if(word2 in row_word):
                #print("It is in front row")
                index=row_word.index(word2)
                #print(index)
                length1=index-length1
                length3=len(puzzel_matrix)-length1-length2
                #NEw list of found array
                x=[]
                #print(length1,length2,length3)
                x1=[" " for i in range(length1)]
                x2=[i for i in word2]
                x3=[" " for i in range(length3)]
                x.extend(x1)
                x.extend(x2)
                x.extend(x3)
                output_list.append(x)
            elif(word2 in reverse_row_word):
                #print("It isin the Back word")
                index=reverse_row_word.index(word2)
                #print(index)
                start=len(puzzel_matrix)-index-len(word2)
                end=start+len(word2)
                x=[]
                x1=[" " for i in range(start)]
                x2=[i for i in word2]
                x3=[" " for i in range(index)]
                x.extend(x1)
                x.extend(x2)
                x.extend(x3)
                output_list.append(x)
            else:
                lista=[" " for i in range(len(puzzel_matrix))]
                #print(lista)
                output_list.append(lista)

#-----------------------------------------------------------------------
def display_column(column,row):
    length=len(puzzel_matrix)
    word_length=len(word2)+row
    print(word_length)

    for i in range(length):
        lista=[]
        for j in range(length):
            if(j==column and (i>=row and i<word_length)):
                lista.append(puzzel_matrix[i][j])
            else:
                lista.append(" ")
        output_list.append(lista)

def display_reverse_column(column_index,start,end):
    #print(column_index,start,end)
    for i in range(len(puzzel_matrix)):
        lista=[]
        for j in range(len(puzzel_matrix)):
            if(j==column_index and(i>=start and i<end)):
                lista.append(puzzel_matrix[i][j])
            else:
                lista.append(" ")
        output_list.append(lista)

#------------------------------------------------------------------------



def top_or_bottom(puzzel_matrix,words):
    
    #here only checking the words in columns
    words_formed=[]
    #Here we are cerating the words formed top to bottom and bottom to top and checking with the words
    for each_column_index in range(len(puzzel_matrix[0])):
        formed_word=""
        for each_word_in_column in range(len(puzzel_matrix)):
            formed_word+=puzzel_matrix[each_word_in_column][each_column_index]
        #----------------------------------------------------------------------------
        if(word2 in formed_word):
            #print(f"It found in column index{each_column_index}")
            row_index=formed_word.index(word2)
            #print(row_index)
            display_column(each_column_index,row_index)


        #---------------------------------------------------------------------
        reverse_word=formed_word[::-1]
        if(word2 in reverse_word):
            index=reverse_word.index(word2)
            print(index)
            start=len(puzzel_matrix)-index-len(word2)
            end=start+len(word2)
            display_reverse_column(each_column_index,start,end)
        words_formed.extend([formed_word,reverse_word])
        

    for each_word in words:
        for each_formed_word in words_formed:
            if(each_word in each_formed_word):
                #print(each_word)
                found_words.append(each_word)
                break
    #removing the find letters to search fast in upcoming process
    #print(found_words)
    for each_word in found_words:
        if(each_word in words):
            words.remove(each_word) 

    #display the word only:
    if(word2 in found_words):
        #print("It in columns")
        pass
#------------------------------------------------------------------------------------------------------
def display_top_left_to_bottom_right(key,values): # from top_left to right_bottom
    if(word2 in values):
        index=values.index(word2)
        max_word=index+len(word2)
        print(max_word)
        print(index)
        for each_row_index in range(len(puzzel_matrix)):
            lista=[]
            for each_column_index in range(len(puzzel_matrix[0])):
                summ=each_row_index-each_column_index
                if(key==summ and (each_row_index>=index and each_row_index<max_word)):
                    lista.append(puzzel_matrix[each_row_index][each_column_index])
                else:
                    lista.append(" ")
            output_list.append(lista)

def display_bottom_right_to_top_left(key,values): # from_bottom_right_to_top_left
    if(word2 in values):
        index=values.index(word2)
        start=len(values)-index-len(word2)
        end=start+len(word2)
        #print(end)
        #print(start)
        #print(index)
        for each_row_index in range(len(puzzel_matrix)):
            lista=[]
            for each_column_index in range(len(puzzel_matrix[0])):
                summ=each_row_index-each_column_index
                if(key==summ and (each_row_index>=start and each_row_index<end)):
                    lista.append(puzzel_matrix[each_row_index][each_column_index])
                else:
                    lista.append(" ")
            output_list.append(lista)     


#---------------------------------------------------------------------------------


def diagnol_top_left_or_bottom_right(puzzel_matrix,words):
    words_formed=[]
    dict_to_store_words={}
    
    for each_row_index in range(len(puzzel_matrix)):
        for each_column_index in range(len(puzzel_matrix[0])):
            summ=each_row_index-each_column_index
            if summ in dict_to_store_words:
                dict_to_store_words[summ]+=puzzel_matrix[each_row_index][each_column_index]
            else:
                dict_to_store_words[summ]=puzzel_matrix[each_row_index][each_column_index]
    #print(dict_to_store_words)

    for key,values in dict_to_store_words.items():
        #print(key,values)
        display_top_left_to_bottom_right(key,values)
        reversed_word=values[::-1]
        display_bottom_right_to_top_left(key,reversed_word)
        words_formed.extend([values,reversed_word])
    #print(words_formed)

    

    for each_word in words:
        for each_formed_word in words_formed:
            if(each_word in each_formed_word):
                #print(each_word)
                found_words.append(each_word)
                break
    #removing the find letters to search fast in upcoming process

    #print(found_words)
    for each_word in found_words:
        if(each_word in words):
            words.remove(each_word) 

#-------------------------------------------------------------------------------------------------------
def display_top_right_to_left_bottom(key,values):
    if(word2 in values):
        start=values.index(word2)
        end=start+len(word2)
        
        for each_row_index in range(len(puzzel_matrix)):
            lista=[]
            for each_column_index in range(len(puzzel_matrix[0])):
                summ=each_row_index+each_column_index
                if(key==summ and (each_row_index>=start and each_row_index<end)):
                    lista.append(puzzel_matrix[each_row_index][each_column_index])
                else:
                    lista.append(" ")
            output_list.append(lista)
    
def dislay_bottom_left_to_top_right(key,values):
    if(word2 in values):
        index=values.index(word2)
        start=len(values)-index-len(word2)
        end=start+len(word2)
        
        for each_row_index in range(len(puzzel_matrix)):
            lista=[]
            for each_column_index in range(len(puzzel_matrix[0])):
                summ=each_row_index+each_column_index
                if(key==summ and (each_row_index>=start and each_row_index<end)):
                    lista.append(puzzel_matrix[each_row_index][each_column_index])
                else:
                    lista.append(" ")
            output_list.append(lista)
#-------------------------------------------------------------------------------------------------------
    
def diagnol_top_right_or_bottom_left(puzzel_matrix,words):
    words_formed=[]
    dict_to_store_words={}
    count=0
    for each_row_index in range(len(puzzel_matrix)):
        for each_column_index in range(len(puzzel_matrix[0])):
            summ=each_row_index+each_column_index
            if summ in dict_to_store_words:
                dict_to_store_words[summ]+=puzzel_matrix[each_row_index][each_column_index]
            else:
                dict_to_store_words[summ]=puzzel_matrix[each_row_index][each_column_index]
    #print(dict_to_store_words)
    for key,values in dict_to_store_words.items():
        display_top_right_to_left_bottom(key,values)
        reversed_word=values[::-1]
        dislay_bottom_left_to_top_right(key,reversed_word)

        words_formed.extend([values,reversed_word])
    #print(words_formed)

    for each_word in words:
        for each_formed_word in words_formed:
            if(each_word in each_formed_word):
                #print(each_word)
                found_words.append(each_word)
                break
    #removing the find letters to search fast in upcoming process
    #print(found_words)
    for each_word in found_words:
        if(each_word in words):
            words.remove(each_word) 

def check_words_in_all_direction(puzzel_matrix,words):
    left_or_right(puzzel_matrix,words)
    top_or_bottom(puzzel_matrix,words)
    diagnol_top_left_or_bottom_right(puzzel_matrix,words)
    diagnol_top_right_or_bottom_left(puzzel_matrix,words)

puzzel_matrix=[ ['c', 'l', 'a', 's', 's', 'e', 's', 'm', 'o', 'p'],
                ['h', 't', 'i', 'd', 'm', 'i', 'y', 'u', 'i', 'e'],
                ['h', 'e', 'b', 'z', 'b', 'e', 'p', 't', 't', 'l'], 
                ['e', 's', 'r', 'l', 'm', 'm', 'p', 'a', 'e', 'b'], 
                ['a', 'a', 'a', 'e', 'o', 'd', 'a', 'b', 'r', 'i'], 
                ['r', 'f', 'c', 'h', 'd', 'c', 'h', 'l', 'a', 'x'], 
                ['r', 'u', 'o', 'h', 'u', 'o', 'k', 'e', 't', 'e'], 
                ['a', 'r', 'b', 'h', 'l', 'a', 'c', 's', 'o', 'l'], 
                ['y', 'p', 'p', 'y', 'e', 'i', 'n', 's', 'r', 'f'], 
                ['e', 's', 's', 't', 'c', 'e', 'j', 'b', 'o', 's']]


word2=input("Please enter the word:")
words=[]
words.append(word2)
print(words)
no_of_words=len(words)
found_words=[]
not_found_words=[]
output_list=[]
print(output_list)


    
    
check_words_in_all_direction(puzzel_matrix,words)

if(len(found_words)==no_of_words):
    print("All the letters Found")
else:
    statement="Found Letters are:"
    joined_letters=",".join(found_words)
    print(statement+joined_letters)

    statement="Not Found Letter:"
    not_joined_letters=",".join(words)
    print(statement+not_joined_letters)

for i in output_list:
    print("[",end=" ")
    for j in i:
        print(j,end=" ")
    print("]",end=" ")
    print()
