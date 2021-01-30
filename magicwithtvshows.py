import requests

 
#todo: make this a cli or gui app where i can just drop url
#todo: syntehsize api request for use in cli app
#todo: add structure to the output file


#extract
def getEpisodeData(url):
    mrRobot=requests.get(url)
    return mrRobot.json()       #gives the data in json

#transform and load function
def showMagic(datum):
    episodeNames=[]
    episodeSummary=[]
    episodeImage=[]
    #mrRobot.json*() gave me a dictionary so datum will be a dict
    #def showDeets():
    nameOfShow=datum["name"]
    network_name=datum["network"]["name"]
    statusofShow=datum["status"]
    premierDate=datum["premiered"]
    showImage=datum["image"]["medium"]
    showSummary=datum["summary"]
    episodes=datum["_embedded"]["episodes"] #_embedded is a dictionary with episode names, reference the key in embedded using its name and square brackets
        

    for key in episodes:
        episodeNames.append(key["name"])
        episodeSummary.append(key["summary"])
        episodeImage.append(key["image"]["original"])


        #return nameOfShow,network_name,statusofShow,premierDate,showImage, episodes, showSummary, episodeSummary, episodeImage, episodeNames

#load data into file
    filename=nameOfShow+".txt"

    with open(filename, 'w') as f:
        f.write("Showname:"+nameOfShow+"\n")
        f.write("Network Name:"+network_name+"\n")
        f.write("statusofShow:"+statusofShow+"\n")
        f.write("Premier Date:"+premierDate+"\n")
        f.write("Show Summary:"+showSummary+"\n")
        f.write("Show Image:"+showImage+"\n")
        f.write("\n")
        f.write("\n")
        f.write("\n")

        for i in range(len(episodes)):
            f.write("Episode Name:"+episodeNames[i]+"\n")
            f.write("Episode Summary:"+episodeSummary[i]+"\n")   
            f.write("Episode Image:"+episodeImage[i]+"\n")
            f.write("\n")
            f.write("\n")
            f.write("\n") 
            f.write("\n")
            f.write("\n")
            f.write("\n")
        f.write("Thats it"+"\n")


    #print(len(datum))          #use that json file, find key network, then save it to network_info variable
    #network_timezone = datum["network"]["country"]["timezone"]    #network info is another dictionary   
    #print(network_info["id"])       #this prints the value associated with key id in network info dict
    #country_name=network_info["country"]    #country is another dict in the dict network_info
    #print(country_name["name"])
    

    #for i in range(len(datum)):        ##does not work, cant iterate through datum because data file has keys and values, not multiple json objects                                 ##to refer to its data, you need to use the keys from the file 
        #return datum[i]                ##to refer to its data, you need to use the keys from the file





if __name__ == "__main__":
    #getMrRobotData()
    showMagic(getEpisodeData("https://api.tvmaze.com/singlesearch/shows?q=mr-robot&embed=episodes"))
    showMagic(getEpisodeData("https://api.tvmaze.com/singlesearch/shows?q=better-call-saul&embed=episodes"))
    showMagic(getEpisodeData("https://api.tvmaze.com/singlesearch/shows?q=Homeland&embed=episodes"))
    
    
    
    
