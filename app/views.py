from app import app, db
from app.models import Auto, Arenda
from flask import render_template, request
from datetime import datetime


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
            date_rent = auto.date
            time_rent = (datetime.now().replace(microsecond=0) - auto.date).seconds
            cost_of_rent = round((time_rent/60)*auto.price,2)
            auto.date = datetime.now().replace(microsecond=0)
            auto.in_rent_or_free = False
            # Добавляем Arenda в базу данных
            db.session.add(Arenda(auto_id = auto.id, date_free = datetime.now().replace(microsecond=0), date_rent=date_rent, in_rent_or_free = auto.in_rent_or_free, time_rent=time_rent, cost_of_rent=cost_of_rent))
            
            auto.count_rent = db.session.query(Arenda).filter_by(auto_id = auto.id).count()
            
        else:
            auto.date = datetime.now().replace(microsecond=0)
            auto.in_rent_or_free = True 
            time_rent = 0
        
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
    #Вывод аренды
    rent_list = Arenda.query.filter_by(auto_id = auto.id)
    total_time = 0
    for time in rent_list:
        total_time += time.time_rent
    auto.all_time_rent = round(total_time/60,2)
    auto.total_cost_of_rent = round(auto.price*total_time/60,2)
    db.session.commit()

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
        'get_button': get_button,
        'rent_list':rent_list,
        'total_cost_of_rent': auto.total_cost_of_rent
        }

    return render_template('auto_detail.html', **context)

@app.route('/del_auto/<int:auto_id>', methods=['POST'])
def del_auto(auto_id):

    auto = Auto.query.get(auto_id)
    rent_list = Arenda.query.filter_by(auto_id = auto.id)
    context = {
        'id': auto.id,
        'name': auto.name
        }
    for rent in rent_list:
        db.session.delete(rent) 
    
    db.session.delete(auto)
    db.session.commit()

    return render_template('del_auto.html', **context)

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
        # В этом случае просто передаем в контекст имя метода и АККП по умолчанию
        context = {
            'method': 'GET',
            'transmission' : 'option1'
        }
    return render_template('create_auto.html', **context)

@app.route('/change_auto/<int:auto_id>', methods=['POST', 'GET'])
def change_auto(auto_id):

    auto = Auto.query.get(auto_id)
    
    if request.method == 'POST':
        
        # Пришел запрос с методом POST (пользователь нажал на кнопку 'Изменить')
        # Получаем новое название auto - это значение поля input с атрибутом name="name"
        new_auto_name = request.form['name']

        # Получаем новое описание auto - это значение поля input с атрибутом name="description"
        new_auto_description = request.form['description']

        # Получаем новую цену auto - это значение поля input с атрибутом name="price"
        new_auto_price = request.form['price']

        # Получаем новое АКПП auto - это значение поля input с атрибутом name="transmission"
        new_auto_transmission = request.form['transmission']
        if new_auto_transmission == 'option1':
            new_auto_transmission = True
        else:
            new_auto_transmission = False
        # Получаем новые картинки auto - это значение поля input с атрибутом name="img_url"
        new_img_url_1 = request.form['img_url_1']  
        new_img_url_2 = request.form['img_url_2']  
        new_img_url_3 = request.form['img_url_3']  
        new_img_url_4 = request.form['img_url_4']  

        if new_auto_name:
            auto.name = request.form['name']
        if new_auto_price:
            auto.price = request.form['price']
        if new_auto_description:
            auto.description = request.form['description']
        auto.transmission = new_auto_transmission
        if new_img_url_1:
            auto.img_url_1 = request.form['img_url_1']
        if new_img_url_2:
            auto.img_url_2 = request.form['img_url_2']
        if new_img_url_3:
            auto.img_url_3 = request.form['img_url_3']
        if new_img_url_4:
            auto.img_url_4 = request.form['img_url_4']
        # сохраняем изменения в базе
        db.session.commit()

        # Заполняем словарь контекста
        context = {
            'id': auto.id,
            'name': auto.name,
            'price': auto.price,
            'auto_description' : auto.description,
            'transmission' : auto.transmission,
            'img_url_1': auto.img_url_1,
            'img_url_2': auto.img_url_2,
            'img_url_3': auto.img_url_3,
            'img_url_4': auto.img_url_4
        }

    elif request.method == 'GET':

        context = {
            'id': auto.id,
            'name': auto.name,
            'price': auto.price,
            'auto_description' : auto.description,
            'transmission' : auto.transmission,
            'img_url_1': auto.img_url_1,
            'img_url_2': auto.img_url_2,
            'img_url_3': auto.img_url_3,
            'img_url_4': auto.img_url_4
            }
               
    return render_template('change_auto.html', **context)

@app.route('/rental_log')
def rental_log():
    auto_list = Auto.query.all()
        
    context = {
        'auto_list': auto_list,
    }
    return render_template('rental_log.html', **context)