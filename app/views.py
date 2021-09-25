from app import app, db
from app.models import Auto
from flask import render_template, request


@app.route('/index')
@app.route('/')
def index():
    
    # Получаем все записи из таблицы Auto
    auto_list = Auto.query.all()

    context = {
        'auto_list': auto_list,
    }

    return render_template('index.html', **context)

@app.route('/auto_detail/<int:auto_id>', methods=['POST', 'GET'])
def auto_detail(auto_id):

    auto = Auto.query.get(auto_id)
    
    context = None
    
    if request.method == 'POST':
        if auto.in_rent_or_free:
            auto.in_rent_or_free = False
        else:
            auto.in_rent_or_free = True 

        db.session.commit()  
    
    #Вывод АККП
    if auto.transmission:
        get_transmission = "Есть"
    else:
        get_transmission = "Нет"

    #Вывод Доступности
    if auto.in_rent_or_free:
        get_in_rent_or_free = "Занят"
        get_button = "Закончить аренду"
    else:
        get_in_rent_or_free = "Свободен"
        get_button = "Арендовать"

    context = {
        'id': auto.id,
        'name': auto.name,
        'auto_description' : auto.description,
        'transmission' : get_transmission,
        'img_url_1': auto.img_url_1,
        'img_url_2': auto.img_url_2,
        'img_url_3': auto.img_url_3,
        'img_url_4': auto.img_url_4,
        'in_rent_or_free': get_in_rent_or_free,
        'get_button': get_button
        }

    return render_template('auto_detail.html', **context)

@app.route('/create_auto', methods=['POST', 'GET'])
def create_auto():
    
    context = None

    if request.method == 'POST':
        
        # Пришел запрос с методом POST (пользователь нажал на кнопку 'Добавить auto')
        # Получаем название auto - это значение поля input с атрибутом name="name"
        auto_name = request.form['name']

        # Получаем описание auto - это значение поля input с атрибутом name="description"
        auto_description = request.form['description']

        # Получаем цену auto - это значение поля input с атрибутом name="price"
        auto_price = request.form['price']

        # Получаем АКПП auto - это значение поля input с атрибутом name="transmission"
        auto_transmission = request.form['transmission']
        if auto_transmission == 'option1':
            auto_transmission = True
        else:
            auto_transmission = False
        # Получаем картинки auto - это значение поля input с атрибутом name="img_url"
        img_url_1 = request.form['img_url_1']  
        img_url_2 = request.form['img_url_2']  
        img_url_3 = request.form['img_url_3']  
        img_url_4 = request.form['img_url_4']  

        # Добавляем auto в базу данных
        db.session.add(Auto(name=auto_name, description=auto_description, price=auto_price, transmission=auto_transmission, img_url_1=img_url_1, img_url_2=img_url_2, img_url_3=img_url_3,img_url_4=img_url_4))

        # сохраняем изменения в базе
        db.session.commit()

        # Заполняем словарь контекста
        context = {
            'method': 'POST',
            'name': auto_name,
            'description' : auto_description,
            'price': auto_price,
            'transmission' : auto_transmission
        }

    elif request.method == 'GET':

        # Пришел запрос с методом GET - пользователь просто открыл в браузере страницу по адресу http://127.0.0.1:5000/create_auto
        # В этом случае просто передаем в контекст имя метода
        context = {
            'method': 'GET',
            'transmission' : 'option1'
        }
    return render_template('create_auto.html', **context)

@app.route('/rental_log')
def rental_log():
    return render_template('rental_log.html')