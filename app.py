from flask import Flask,render_template,redirect,request

siva=Flask(__name__)

l=[{"id":1,"name":"sakthi","course":"design"},{"id":2,"name":"siva","course":"js"},{"id":3,"name":"pradeep","course":"python"},{"id":4,"name":"yugi","course":"react"}]

@siva.route("/",methods=["post","get"])
def fun():
    id=request.form.get("id")
    name=request.form.get("name")
    course=request.form.get("course")
    dic={"id":id,"name":name,"course":course}
    l.append(dic)
    return render_template("index.html",z=l)

if __name__=="__main__":
    siva.run(debug=True)