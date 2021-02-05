import os

print("hello world, how are you?")

data_file = "MasterQuizHighscoreTest.txt"
#is_file_empty = (os.path.isfile(data_file)==False) or (os.stat(data_file).st_size == 0)
#if (is_file_empty):

result = open(data_file,"r").readlines()
print ("data: "+result(0))
open(data_file,"w")
f.write("9");
data_file.close()
    
