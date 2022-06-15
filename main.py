import pandas as pd                                                             #import library pandas for working Exel
path_file = 'Book1.xlsx'                                                        #set exel file in path variable
df = pd.read_excel(path_file)                                                   #set Exel in deta fram
province_list = ["تهران", "مركزی" , "مازندران"]                                 #create list of province for check has in list or not
for index, row in enumerate(df.values[:50]):                                     #loop over exel file

       if row[0] in province_list:                                               #check has cell in list1 or not

               df.at[index, 'check_province'] = "province"                    #type province in row[index]
               print(f"[INFO] Successfully modified index: {index} which contains {row[0]}")
df.to_excel(path_file)                                                            #save to exel file






