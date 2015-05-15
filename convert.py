'''
This takes in a json file and outputs the data elements in markdown.

Scripting this for universal changes

'''

import json
from pprint import pprint

import sys
reload(sys)
sys.setdefaultencoding("utf-8")

default_directory = "data_elements"

def elementToRow(dataElement):
    row = "  <tr>\n"
    row = row + "    <td><a href='data_elements/" + dataElement["page_name"] + ".md' title='" + dataElement["name"] + " Details'>" + dataElement["name"] + "</a></td>\n"
    row = row + "    <td>" + dataElement["definition"] + "</td>\n"
    row = row + "    <td>" + dataElement["source"] + "</td>\n"
    row = row + "  </tr>\n"
    return row
    
def elementToPage(dataElement):
    profilePage = "#" + dataElement["name"] + " Profile\n"
    profilePage = profilePage + "Description: " + dataElement["definition"]
    dataElementProfilePage = open(default_directory + "/" + dataElement["page_name"] + ".md", "w")
    dataElementProfilePage.write(profilePage)
    dataElementProfilePage.close()
    
indexPageString = ""

with open("header.md", "r") as headerFile:
	headerText = headerFile.read() #two spaces md newline

indexPageString = indexPageString + headerText

with open('data_interoperability.json') as data_file:
    data = json.load(data_file)
    
for dataElement in data["data_elements"]:
    indexPageString = indexPageString + elementToRow(dataElement)
    elementToPage(dataElement)
    
with open("footer.md", "r") as footerFile:	
    footerText = footerFile.read()

indexPageString = indexPageString + footerText

indexPage = open("Readme_Data_Interoperability.md", "w")
indexPage.write(indexPageString)
indexPage.close()


