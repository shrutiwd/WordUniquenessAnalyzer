# To find the unique words from the file

class Unique_words:
    
    ''' A class to find the unique words from the file '''

    def __init__(self, file_name, output_file):

        ''' Intializing instance variables '''

        self.file_name = file_name
        self.output_file = output_file

    def unique(self):

        ''' Allows user to find the unique words from the desired file '''
        unique_list = []
        file = open(self.file_name,'r')
        lst = list(file)

        # create the list by spliting the words
        for i in lst:
            lst1 = i.split()
            
            # find the unique words
            for j in lst1:
                if j not in unique_list:
                    unique_list.append(j)
##                    print(unique_list)
                else:
                    pass
        print("Unique words: ", unique_list)
        print(f"Data saved in {self.output_file}")

        # To write the unique words in the file 
        file1 = open(self.output_file, 'w')
        uniq = [file1.write(str(u) + '\n') for u in unique_list]


# user inputs
file_name = input("Enter the file name from which the unique words to be found with .txt extension: ")
output_file = input("Enter the file name to save the unique words with .txt extension: ")


# calling the method
uw = Unique_words(file_name, output_file)
uw.unique()
        
