import io
import flask
import qrcode

# from datetime import timedelta


app = flask.Flask(__name__)

# app.config['SEND_FILE_MAX_AGE_DEFAULT'] = timedelta(seconds=1)

@app.route('/')

def home():
    # # 第一步：获取要生成二维码的数据
    # data = flask.request.args.get("data")

    # # 第二步：生成二维码图片
    # img = qrcode.make(data)
    # img.save(r"C:\Users\Administrator\Desktop\二维码生成器\static/qr.png")

    # #第三步：在页面上显示二维码图片
    # return '<img src ="/static/qr.png" />'
    #第一次修改

    return flask.render_template('qr_tool.html')

# @app.route('/qr',methods=["POST"])
@app.route('/qr')

def qr():
    # 第一步：获取要生成二维码的数据
    #data = flask.request.form.get("data")
    data = flask.request.args.get("data")

    
    # 第二步：生成二维码图片
    img = qrcode.make(data) 
    bi = io.BytesIO() # 创建一个BytesIO对象，用于二维码图像数据

    #img.save(r"C:\Users\Administrator\qr_tool\static\qrc.png") #保存到文件夹

    img.save(bi,'png') # 通过调用img对象的save方法将二维码图像数据以PNG编码格式写入bi对象管理的内存空间
    bi.seek(0) # 将bi对象内部的位置指针移动到图像数据的起始位置

    # return '<img src ="/static/qrc.png" />'
    return flask.send_file(bi, 'image/png')

if __name__ == '__main__':
    app.run(debug=True)
    # app.run(debug=True,host="0.0.0.0")