from flask import Flask,redirect,url_for


app=Flask(__name__)

@app.route("/")
def welcome():
    return "hello world"

@app.route("/results/<int:score>")
def results(score):
    re="sucess" if score> 50 else "fail"
    
    return f"""
    <!DOCTYPE html>
        <html>
        <body>
        <h2>{re} </h2>
        </body>
        </html>
        """



if __name__ =="__main__":
    app.run()