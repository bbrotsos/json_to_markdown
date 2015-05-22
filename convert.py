'''
This takes in a json file and outputs the data elements in markdown.

Scripting this for universal changes


'''

import json
from pprint import pprint

import sys
reload(sys)
sys.setdefaultencoding("utf-8")

def elementToRow(dataElement, default_directory):
    row = "  <tr>\n"
    row = row + "    <td><a href='" + default_directory + "/" + dataElement["page_name"] + ".md' title='" + dataElement["name"] + " Details'>" + dataElement["name"] + "</a></td>\n"
    row = row + "    <td>" + dataElement["definition"] + "</td>\n"
    row = row + "    <td>" + dataElement["source"] + "</td>\n"
    row = row + "  </tr>\n"
    return row

def enumeratedValueToTable(enumeratedValue):
    tableString = "<tr><td>" + enumeratedValue["value_item"] + "</td>"
    tableString = tableString + "<td>" + enumeratedValue["value_definition"] + "</td></tr>"
    return tableString
    
def elementToPage(dataElement, default_directory):
    profilePage = "#" + dataElement["name"] + " Profile\n"
    profilePage = profilePage + "Description: " + dataElement["definition"]
    if "enumeration" in dataElement:
        tableString = "<table>\n"
        tableString = tableString + "<thead><tr><th scope='col'><a href='ValueItem.md'>Value Item</a></th><th scope='col'><a href='ValueDefinition.md'>Value Meaning</a></th></tr></thead>"  
    	for enumeratedValue in dataElement["enumeration"]:
    	     tableString = tableString + enumeratedValueToTable(enumeratedValue)
        
        tableString = tableString + "</table>"
        profilePage = profilePage + tableString
    else:
        tableString = "<table><thead><tr><th scope='col'>Property</th><th scope='col'>Definition</th></tr>"
        tableString = tableString + "<tr><td><a href='DataTypeCode.md'>Data Type Code</a></td><td>" + dataElement["data_type_code"] + "</td></tr>"
        tableString = tableString + "<tr><td><a href='MinimumLengthNumber.md'>Minimum Length Number</a></td><td>" + str(dataElement["min_length"]) + "</td></tr>"
        tableString = tableString + "<tr><td><a href='MaximumLengthNumber.md'>Maximum Length Number</a></td><td>" + str(dataElement["max_length"]) + "</td></tr>"
        tableString = tableString + "<tr><td><a href='RepresentationClass.md'>Representation Class Code</a></td><td>" + dataElement["representation_class"] + "</td></tr>"
        
        tableString = tableString + "</table>"
        profilePage = profilePage + tableString
    if "comments" in dataElement:
        profilePage = profilePage + dataElement["comments"]    
    dataElementProfilePage = open(default_directory + "/" + dataElement["page_name"] + ".md", "w")
    dataElementProfilePage.write(profilePage)
    dataElementProfilePage.close()
    
def createDataElementListingPage(headerFile, footerFile, jsonInput, outputFile, default_directory):
	indexPageString = ""
	with open(headerFile, "r") as headerFile:
		headerText = headerFile.read() #two spaces md newline
	indexPageString = indexPageString + headerText

	with open(jsonInput) as data_file:
		data = json.load(data_file)
    
	for dataElement in data["data_elements"]:
		print ("Processing " + dataElement["name"] + "...")
		indexPageString = indexPageString + elementToRow(dataElement, default_directory)
		elementToPage(dataElement, default_directory)
    
	with open(footerFile, "r") as footerFile:	
		footerText = footerFile.read()

	indexPageString = indexPageString + footerText

	indexPage = open(outputFile, "w")
	indexPage.write(indexPageString)
	indexPage.close()

#create iso elements
createDataElementListingPage("header.md", "footer.md", "data_interoperability.json", "Readme_Data_Interoperability.md", "data_elements")
createDataElementListingPage("swagger_header.md", "swagger_footer.md", "swagger.json", "swagger_elements.md", "swagger_elements")
createDataElementListingPage("mvtd_header.md", "mvtd_footer.md", "mvtd.json", "tabular_data.md", "mvtd_elements")



