import requests




cat_ids=[]

#this is to extract the data
def getcatdata(url):
    cat_aas=requests.get(url)
    return cat_aas.json()
    #return cat_aas.text
    #print(cat_aas.text) #you can use .status_code to get the status code, text to get the text 
    #dir(cat_aas) will give methods and properties assocaited with requests module


#this is to transform the data

##cat_data[0]['id'] references the id key in the 1st element of that json file
def transform_cats(cat_data,which):
    #cat_ids=[]

    for cat in cat_data:
        cat_ids.append(cat["id"])      #finds the id of each cat and prints it

    return cat_ids[which]

#this is to load the data
def load_cat(which,names):
    #no1=int(which)
    cat_home="https://cataas.com/cat/"+str(which)
    print(str(cat_home))
    cat_pic=requests.get(cat_home)
    if cat_pic.status_code==200:
        print ("Success!")
        with open(r"cat" + str(names)+".jpg",'wb') as catboi:
            catboi.write(cat_pic.content)
    


#actual request here
result=getcatdata('https://cataas.com/api/cats?tags=cute')
for x in range(len(result)):
    cat_name=transform_cats(result,x)
    load_cat(cat_name,x)
#print(str(result))


