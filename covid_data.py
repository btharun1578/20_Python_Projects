'''

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, OCaml, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

'''
def change_list_to_string(lista):
    final_list=[]
    for i in lista:
        final_list.append(str(i))
    #print(final_list)
    return " ".join(final_list)
    
    
    
def encryption_level_two(data,original_list):
    encrypted_result_level_two=[]
    for i in original_list:
        length=len(i) #length=5
        increment=length*100 #500
        if(i not in [" ","."]):
            for j in data[i]:#getting each word data from dict []
                encrypted_result_level_two.append(j+increment)
        else:
            encrypted_result_level_two.extend(data[i])
    output2=change_list_to_string(encrypted_result_level_two)
    print(f"{input1}- this text will become  {output2}")
    print("Sum of Level-2 Data:",sum(encrypted_result_level_two))
    print("**********************************")
    
    
def encryption_level_one(list1):
    encrypted_result_level_one=[]
    level_two_data={}
    for i in list1:
        result = []
        for char in i:
            if char.islower():
                result.append(ord(char) - ord('a') + 1)
            elif char.isupper():
                result.append(ord(char) - ord('A') + 27)
            elif char == '.':
                result.append(99)
            elif char.isspace():
                result.append(0)
        encrypted_result_level_one.extend(result)
        level_two_data[i]=result
        #print(level_two_data)
    output1=change_list_to_string(encrypted_result_level_one)
    print(f"{input1}- this text will become  {output1}")
    print("Sum of Level-1 Data:",sum(encrypted_result_level_one))
    print("**********************************")
    #print(level_two_data)
    encryption_level_two(level_two_data,list1)
    
        
def sorting_order(partition):
    sorting=[]
    final_result_level_3=[]
    dicta={}   #{1:[],2:[],3=[,and,has,the ],5:["covid"],6:["crisis","taught"]}

    
    for i in partition:
        if i not in [" ","."]:
            sorting.append(i)
    #print(sorting)
    for i in sorting:
        l=len(i)
        if l in dicta:
            dicta[l].append(i)
        else:
            dicta[l]=[i]
    #print(dicta)
    dicta_ordered_keys=sorted(dicta.keys()) #3,5,6
    for i in dicta_ordered_keys:
        words=dicta[i]
        alpha_order=sorted(words)
        final_result_level_3.extend(alpha_order)
    print("The ordered result of Level-3:"," ".join(final_result_level_3))
    
    
def partition_into_words(name):
    partition = []
    separation = ""
    
    for i in name:
        if i not in [" ", "."]:
            separation += i
        else:
            partition.append(separation)
            separation = i
            partition.append(separation)
            separation=""
    if separation:
        partition.append(separation)

    #print(partition)    
    encryption_level_one(partition)
    sorting_order(partition)
    
input1="COVID crisis has taught us several lessons and together we have overcome this great challenge. The COVID pandemic sent shock waves through the world economy and triggered the largest global economic crisis in more than a century. The crisis led to a dramatic increase in inequality within and across countries. Preliminary evidence suggests that the recovery from the crisis will be as uneven as its initial economic impacts, with emerging economies and economically disadvantaged groups needing much more time to recover from pandemic-induced losses of income and livelihoods. Now there is a sense of introspection in people. India has emerged stronger."
partition_into_words(input1)