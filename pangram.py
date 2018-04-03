import string
import cgi

from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/', methods=['GET'])
def fun():
    if request.method == 'GET':
        return render_template('ispangram.html')

@app.route("/submit", methods = ["POST"])


def ispangram(alphabet=string.ascii_lowercase):  
    str_abc = 'abcdefghijklmnopqrstuvwxyz'
    str_abc = [letter for letter in str_abc]
    str1 = str(request.form['sentence'])
    str2 = [letter for letter in str1]
    for letter in str2:
        if str_abc.count(letter) == 1:
            str_abc.remove(letter)
    if len(str_abc) == 0:
        return render_template('pangram.html')
    else:
        return render_template('notpangram.html')
        
if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0')
	
