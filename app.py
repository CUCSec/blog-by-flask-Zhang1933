from flask import Flask,render_template
from pathlib import Path

app=Flask(__name__)

@app.route("/")
def homePage():
   
    return render_template("home.html")

@app.route("/about")
def about():

    return render_template("about.html")


@app.route("/articles_list")
def article_list():
  
    article_list=[str(x) for x in  (Path('./data').glob("**/*.txt"))]
    return render_template("articles_list.html",list=article_list)


@app.route("/<path:url_path>")
def article_display(url_path):
   
    with open(r"{}".format(url_path),"r",encoding="utf-8")as f:
        data=f.readlines()
    return render_template("articles.html",article=data)


if __name__ == "__main__":
    app.run(debug=True)