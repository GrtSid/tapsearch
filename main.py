from flask import Flask,render_template,request,redirect,url_for
from collections import defaultdict
app=Flask(__name__)
def tapsearch(st,word):
    d=defaultdict(list)
    d.clear()
    l1=st
    l=0
    for i in l1:
        l=l+1
        i=i.split(" ")
        for k in i:
            if (len(d[k])>0):
                if((d[k][-1]==l)):
                    continue
            d[k.lower()].append(l)
    word=word.lstrip(" ")
    return(d[word])
@app.route('/')
def hello_world():
    return render_template('index.html')
@app.route('/output',methods=['POST','GET'])
def output():
    if (request.method=='POST'):
        st=request.form['userInput']
        h=st.split('  ')
        h=h[::2]
        word=request.form['word']
        word=word.lower()
        out= (tapsearch(h,word))
        return render_template('output.html',out=out)
