from flask import Flask, redirect, url_for, request,render_template
app = Flask(__name__)

@app.route('/')
def index():
   return render_template("index.html")

@app.route('/ff',methods = ['POST', 'GET'])
def ff():
   return render_template("form.html")

@app.route('/form',methods = ['POST', 'GET'])
def form():
   # age gender trp cholestrol fbs ecg thalaz exong old peak slope
   name=request.form['name']
   age=request.form['age']
   sex=request.form['sex']
   trp=request.form['trp']
   cholestrol=request.form['cholesterol']
   fbs=request.form['fbs']
   ecg=request.form['Ecg']
   Thalaz=request.form['Thalaz']
   Exong=request.form['Exong']
   Oldpeak=request.form['Old Peak']
   slope=request.form['slope']
   # your calculation code need to write here where final result need to be stroed in a variable name result and assign the result value to the rrr below your can change the rrr to u choice
   return render_template("result.html",name=name,age=age,sex=sex,trp=trp,cholestrol=cholestrol,fbs=fbs,ecg=ecg,Thalaz=Thalaz,Exong=Exong,Oldpeak=Oldpeak,slope=slope,rrr=0)
   # return '%s %s %s %s %s %s %s %s %s %s ' %age %sex %trp %cholestrol %fbs %ecg %Thalaz %Exong %Oldpeak %slope
   # return '%s %s %s %s %s %s %s %s %s %s ' %(age,sex,trp,cholestrol,fbs,ecg,Thalaz,Exong,Oldpeak,slope)
   # return 'Hello World’
#    return redirect(url_for('final',age=age,sex=sex,trp=trp,cholestrol=cholestrol,fbs=fbs,ecg=ecg,Thalaz=Thalaz,Exong=Exong,Oldpeak=Oldpeak,slope=slope))
# @app.route('/result/<age>/<sex>/<trp>/<cholestrol>/<fbs>/<ecg>/<Thalaz>/<Exong>/<Oldpeak>/<slope>',)
# def final(age,sex,trp,cholestrol,fbs,ecg,Thalaz,Exong,Oldpeak,slope):
#       # return '%s %s %s %s %s %s %s %s %s %s ' %(age,sex,trp,cholestrol,fbs,ecg,Thalaz,Exong,Oldpeak,slope)
#       return '<html><head><script>alert({{age}})</script></head></html>'

if __name__ == '__main__':
   app.run(debug=True)