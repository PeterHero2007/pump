from flask import Flask,request,render_template

app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def index():
    if request.method == 'POST':
        print(request.data)
        if request.data == b"water":
            status = "正在浇水"
            with open(r'.\status.txt','w',encoding="utf-8") as file:
                file.write(status)
            print("water")
        elif request.data == b"stop":
            status = "停止浇水"
            with open(r'.\status.txt','w',encoding="utf-8") as file:
                file.write(status)
            print('stop')
        return render_template('index.html',is_watering=status)
    if request.method == 'GET':
        with open(r'.\status.txt','r',encoding="utf-8") as file:
            status = file.read()
        return render_template('index.html',is_watering=status)

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=80)