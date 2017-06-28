'''
Created on May 19, 2017

@author: stetester
'''
from OSeriesAutomationUtilities.FileSystem.Directory import FileDirectory
from OSeriesAutomationUtilities.XML.XMLFile import XMLFile
import os
from os.path import splitext
import posixpath

"""Tool to update login nodes in xml and exp"""

#filePath = "C:/test/_XML/TPS_80/FunctionalTest/TestData/ServiceRelease/AncillaryCharges/ANCHCHRG_Taxability_Freight_ZeroRate/ANCH_Freight_ZerRate_Situs.out"

# filePath = "C:/test/_XML/TPS_80/FunctionalTest/TestData/Retail_End_To_End/Full/ut5a.out"
for root, dirs, files in os.walk("C:/test/_XML/TPS_80/FunctionalTest/TestData/SmokeTest", topdown=True):
       
    for name in files:
        print(os.path.join(root, name))
        if name.endswith('.html') or name.endswith('pdf') or name.endswith('csv') or name.endswith('dat')  or name.endswith('bak') or name.endswith('txt') or name.endswith('log') or name.endswith('zip') or name.endswith('xx') or name.endswith('doc') or name.endswith('FAIL') or name.endswith('xlsx') or name.endswith('xls'):
            continue
        sourceXML = posixpath.join(root, name)
        xml = XMLFile(sourceXML)
        vertexEnvelope = xml.VertexEnvelope
        username = vertexEnvelope.Login.UserName.text
        password = vertexEnvelope.Login.Password.text
        targetXML = sourceXML.replace('/_XML', "")
        targetXML = posixpath.splitext(targetXML)[0]
        basename = targetXML + ".xml"
        try:
            xmlToOpen = XMLFile(basename)
        except:
            print ('skipped xml')
            pass
        else: 
            vEnvelope = xmlToOpen.VertexEnvelope
            login = vEnvelope.Login
            login.UserName.text = username
            login.Password.text = password
            xmlToWrite = str(xmlToOpen)
            with open(basename, 'w') as fileToOpen:
                fileToOpen.write(xmlToWrite)
        basename2 = targetXML + ".out"
        try:
            xmlToOpen = XMLFile(basename2)
        except:
            pass
        else:
            vEnvelope = xmlToOpen.VertexEnvelope
            login = vEnvelope.Login
            login.UserName.text = username
            login.Password.text = password
            xmlToWrite = str(xmlToOpen)
            with open(basename2, 'w') as fileToOpen:
                fileToOpen.write(xmlToWrite)
        basename3 = targetXML + ".exp"
        try:
            xmlToOpen = XMLFile(basename3)
        except:
            pass
        else:
            vEnvelope = xmlToOpen.VertexEnvelope
            login = vEnvelope.Login
            login.UserName.text = username
            login.Password.text = password
            xmlToWrite = str(xmlToOpen)
            with open(basename3, 'w') as fileToOpen:
                fileToOpen.write(xmlToWrite)
    print 'end of current directory'