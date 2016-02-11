#Following code tests BMC's running openBMC image using REST API calls
###################################################
def GET(url):
        try:
                getOutput=requests.get(url,verify=False)
                return getOutput
        except requests.exceptions.RequestException as e:    # This is the correct syntax
                print e
                # Handle optput assignment / Different Errors here

def POST(url):
        try:
                postOutput = requests.post(url, json=payload)
                return postOutput
        except requests.exceptions.RequestException as e:
                print e

####################################################

import requests
import json
serverNumber=22

######################################################
# Returns 'True' / 'False' based on if the card was present or not respectively

def isHWPresent(url):
	response=GET(url)
        jsonResponse = response.json()
        parsedData=jsonResponse['data']
        return parsedData['present']			# Returns 'True' / 'False' based on if the card was present or not respectively 

#####################################################
# 32 DIMM slots present in Barreleye

dimmList=[]
def getDimmInventory():
	dimmInventoryUrl="https://10.127.89.2"+str(serverNumber)+"/org/openbmc/inventory/system/chassis/motherboard/dimm"
	for dimmNumber in range(32):
		dimmPresenceStatus=isHWPresent(dimmInventoryUrl+str(dimmNumber))		
		dimmList.append(dimmPresenceStatus)
	print dimmList

#######################################################

temperatureURL="https://10.127.89.2"+str(serverNumber)+"/org/openbmc/sensors/temperature/"
ambient=temperatureURL+'ambient'

#######################################################
########################################################

chassisControl="https://10.127.89.2"+str(serverNumber)+"/org/openbmc/control/chassis0/action/"
powerOn=chassisControl+'powerOn'
powerOff=chassisControl+'powerOff'
reboot=chassisControl+'reboot'

#######################################################

def getValue(url):
	response=GET(url)
	jsonResponse = response.json()
	parsedData=jsonResponse['data']
	return parsedData['value']

def controlMethod(url):
	payload = {'data': []}
	response=POST(url)
	

def getDimmTemperatures():
	for dimmNumber in range(32):
		if dimmList[dimmNumber]=='True':
			print getValue(temperatureURL+'dimm'+str(dimmNumber))

getDimmInventory()
getDimmTemperatures()


#curl -k -H "Content-Type: application/json" -X POST -d "{\"data\": []}" https://[ip address]/org/openbmc/control/chassis0/action/powerOn


#for i in range(1,10):
#	print getValue(tempURL)

