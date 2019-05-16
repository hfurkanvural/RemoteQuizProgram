from flask import Flask, render_template, request
app = Flask(__name__)

from socket import *

serverName="<ServerName>"
serverPort="<ServerPort>"

clientSocket=socket(AF_INET,SOCK_STREAM)

clientSocket.connect((serverName,serverPort))


@app.route('/',methods = ['POST', 'GET'])
def student():
	modifiedMessage=clientSocket.recv(1024)
	message= modifiedMessage.decode("utf-8")
	return render_template('student.html', message= message)

@app.route('/result',methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
	   items = request.form
	   result = items['Name']
	   print(result)
	   clientSocket.send(result.encode())
	   modifiedMessage=clientSocket.recv(1024)
	   message= modifiedMessage.decode("utf-8")
	   if (message == "User is not registered!"): 
		   clientSocket.close()
	   return render_template("result.html", message= message)

@app.route('/result2',methods = ['POST', 'GET'])
def result2():
   if request.method == 'POST':
	   items = request.form
	   result = items['Answer1']
	   print(result)
	   clientSocket.send(result.encode())
	   modifiedMessage=clientSocket.recv(1024)
	   message= modifiedMessage.decode("utf-8")
	   return render_template("result2.html", message= message)

@app.route('/result3',methods = ['POST', 'GET'])
def result3():
   if request.method == 'POST':
	   items = request.form
	   result = items['Answer2']
	   print(result)
	   clientSocket.send(result.encode())
	   modifiedMessage=clientSocket.recv(1024)
	   message= modifiedMessage.decode("utf-8")
	   return render_template("result3.html", message= message)
 

@app.route('/result4',methods = ['POST', 'GET'])
def result4():
   if request.method == 'POST':
	   items = request.form
	   result = items['Answer3']
	   print(result)
	   clientSocket.send(result.encode())
	   modifiedMessage=clientSocket.recv(1024)
	   message= modifiedMessage.decode("utf-8")
	   return render_template("result4.html", message= message)
 

@app.route('/result5',methods = ['POST', 'GET'])
def result5():
   if request.method == 'POST':
	   items = request.form
	   result = items['Answer4']
	   print(result)
	   clientSocket.send(result.encode())
	   modifiedMessage=clientSocket.recv(1024)
	   message= modifiedMessage.decode("utf-8")
	   return render_template("result5.html", message= message)
 

@app.route('/finalResult',methods = ['POST', 'GET'])
def finalResult():
   if request.method == 'POST':
	   items = request.form
	   result = items['Answer5']
	   print(result)
	   clientSocket.send(result.encode())
	   modifiedMessage=clientSocket.recv(1024)
	   message= modifiedMessage.decode("utf-8")
	   clientSocket.close()
	   return render_template("finalResult.html", message= message)
 
if __name__ == '__main__':
   app.run(debug = True) 
