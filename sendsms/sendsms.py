import requests
import json
import mysql.connector as mysql


smscon = mysql.connect(host="localhost",user="root",password="password",db="tkinter_allapps")
cursor = smscon.cursor()
cursor.execute("select * from room_management")
res = cursor.fetchall()
smscon.close()

share = []
user = []
mobile = []
for i in res:
    mobile.append(i[1])
    user.append(i[0])
    share.append(i[2])

URL = 'https://www.sms4india.com/api/v1/sendCampaign'

# get request
def sendPostRequest(reqUrl, apiKey, secretKey, useType, phoneNo, senderId, textMessage):
  req_params = {
  'apikey':apiKey,
  'secret':secretKey,
  'usetype':useType,
  'phone': phoneNo,
  'message':textMessage,
  'senderid':senderId
  }
  return requests.post(reqUrl, req_params)


for index, item in enumerate(mobile):
    response=sendPostRequest(URL, 'A5X8OJMACQRO8L90LFSZH3XZ1LLEVF6O', 'KA3QQ2K902TKMLST', 'stage', item, 'viswanath', "Hello {}, Your room share is {}".format(user[index],share[index]))

"""
  Note:-
    you must provide apikey, secretkey, usetype, mobile, senderid and message values
    and then requst to api
"""
# print response if you want
print(response.text)#[9:12])
