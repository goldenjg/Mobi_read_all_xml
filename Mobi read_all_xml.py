"""read all xml licenses into table and save to Excel."""
import pandas as pd
import os
import bs4 as bs

table_contents = []


def get_xml_data_all(file_path, plant_code):
    """reads xml files and puts values into global table."""
    # read xml file
    infile = open(file_path, "r")
    contents = infile.read()

    # define fields in xml to read
    soup = bs.BeautifulSoup(contents, 'xml')
    licenses = soup.find_all('license')
    ids = soup.find_all('id')
    users = soup.find_all('user')
    keys = soup.find_all('key')

    # loop thru each xml entriy and append to table
    for i in range(0, len(licenses)):
        z = ids[i].get_text(), users[i].get_text(), keys[i].get_text(), plant_code
        table_contents.append(z)


# create array of directories with xml files
path = 'C:\\Soti\\MobiControl\\SharedFileCache\\LicFiles\\Naurtech'
arr = os.listdir(path)

# loop thru each directory, find the xml file and extract the xml data
for i in arr:
    file_pathx = "C:\\Soti\\MobiControl\\SharedFileCache\\LicFiles\\Naurtech\\" + i + '\\' + i + "_CK71_license.xml"
    #file_pathx = path + '\\' + i + '\\' + i + "_CK71_license.xml"

    if len(i) > 2:
        j = i.split("_")[0]
        file_pathx = "C:\\Soti\\MobiControl\\SharedFileCache\\LicFiles\\Naurtech\\" + i + '\\' + j + "_CK71_license_VTSO.xml"

    if i == "CK":       # in a different file path
        file_path_CK = "C:\\Soti\\MobiControl\\SharedFileCache\\LicFiles\\Naurtech\\CK\\2015_01_07" + "\\" + "license.xml"
        plant_code = ""
        get_xml_data_all(file_path_CK, "CK")  # plant_code)

    elif i == "R5":     # using a different xml file name format
        file_path_R5 = "C:\\Soti\\MobiControl\\SharedFileCache\\LicFiles\\Naurtech\\" + i + "\\" + i + "_MC92_License.xml"
        get_xml_data_all(file_path_R5, i)

    elif i == "VT":     # using a different xml name format
        file_path = "C:\\Soti\\MobiControl\\SharedFileCache\\LicFiles\\Naurtech\\" + i + "\\" + i + "_CK75_license.xml"
        get_xml_data_all(file_path, i)
    else:
        get_xml_data_all(file_pathx, i)


df = pd.DataFrame(table_contents)
df.columns = ["ID", "user", "key", "plant"]
df.to_csv("D:\\All_plants_xml_to_csv_license_data.csv", index=False)
