from flask import Flask

app = Flask(__name__)


@app.route('/')
def base():
    return 'Миссия Колонизация Марса'


@app.route('/index')
def index():
    return "И на Марсе будут яблони цвести!"


@app.route('/promotion')
def promotion():
    return "Человечество вырастает из детства.  \
           </br>Человечеству мала одна планета. \
           </br>Мы сделаем обитаемыми безжизненные пока планеты. \
           </br>И начнем с Марса! \
           </br>Присоединяйся!"


@app.route('/image_mars')
def image_mars():
    return '''<!doctype html>
                    <html lang="en">
                      <head>
                        <meta charset="utf-8">
                        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                        <link rel="stylesheet" 
                        href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                        integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                        crossorigin="anonymous">
                        <title>Привет, Марс!</title>
                      </head>
                      <body>
                        <h1>Жди нас, Марс!</h1>
                        <p><img src="static/img/mars.png" alt="-"></p>
                        <p><font size="5"
                        <h2>Вот она какая, красная планета</h2>
                      </body>
                    </html>'''


@app.route('/promotion_image')
def promotion_image():
    return '''<!doctype html>
                    <html lang="en">
                      <head>
                        <meta charset="utf-8">
                        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                        <link rel="stylesheet" 
                        href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                        integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                        crossorigin="anonymous">
                        <title>Привет, Марс!</title>
                      </head>
                      <body>
                        <h1>Жди нас, Марс!</h1>
                        <p><img src="static/img/mars.png" alt="-"></p>
                        <p><font size="5"
                        <div class="alert alert-secondary" role="alert">
                        <h2>Человечество вырастает из детства.</h2>
                        </div>
                        <div class="alert alert-success" role="alert">
                        <h3>Человечеству мала одна планета.</h3>
                        </div>
                        <div class="alert alert-secondary" role="alert">
                        <h4>Мы сделаем обитаемыми безжизненные пока планеты.</h4>
                        </div>
                        <div class="alert alert-warning" role="alert">
                        <h5>И начнем с Марса!</h5>
                        </div>
                        <div class="alert alert-danger" role="alert">
                        <h6>Присоединяйся!</h6>
                        </div>
                      </body>
                    </html>'''


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
