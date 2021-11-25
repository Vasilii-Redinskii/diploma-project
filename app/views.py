from app import app, db
from app.models import Condenser, Capacity, New_Capacity
from flask import render_template, request
from datetime import datetime


@app.route('/index')
@app.route('/')
def index():
    
    # Получаем все записи из таблицы Condenser
    condenser_list = Condenser.query.filter_by(low_noise = False)

    context = {
        'condenser_list': condenser_list,
    }

    return render_template('index.html', **context)


@app.route('/condenser_detail/<int:Condenser_id>', methods=['POST', 'GET'])
def condenser_detail(Condenser_id):

    condenser = Condenser.query.get(Condenser_id)
    #capacity_list = Capacity.query.filter_by(Condenser_id = Condenser.id)

    if request.method == 'POST':
        
        # Пришел запрос с методом POST (пользователь нажал на кнопку 'Добавить точку')
        
        Capacity_max_temp = request.form['max_temp']
        Capacity_min_temp = request.form['min_temp']
        Capacity_point = request.form['capacity']

        check_name = str(condenser.id) + str(Capacity_max_temp) + str(Capacity_min_temp)
        condenser_list = Condenser.query.all() 

        # Добавляем Condenser в базу данных
        db.session.add(Capacity(
            condenser_id=condenser.id,
            max_temp=Capacity_max_temp, 
            min_temp=Capacity_min_temp,
            capacity_point=Capacity_point,
            delta_temp=int(Capacity_max_temp) - int(Capacity_min_temp),
            check_name = str(condenser.id) + str(Capacity_max_temp) + str(Capacity_min_temp) + str(Capacity_point)))
            
        # сохраняем изменения в базе
        db.session.commit()

    capacity_list = Capacity.query.filter_by(condenser_id = Condenser_id)
        #elif request.method == 'GET':
        # Пришел запрос с методом GET - пользователь просто открыл в браузере страницу по адресу http://127.0.0.1:5000/create_Condenser
        
    context = {
        'id': condenser.id,
        'name': condenser.name,
        'description' : condenser.description,
        'length': condenser.length,
        'width': condenser.width,
        'height': condenser.height,
        'weight': condenser.weight,
        'fan' : condenser.fan,
        'number_fan': condenser.number_fan,
        'air_flow': condenser.air_flow,
        'noise' : condenser.noise, 
        'low_noise' : condenser.low_noise,
        'img_url_1': condenser.img_url_1,
        'img_url_2': condenser.img_url_2,
        'capacity_list': capacity_list
        }

    return render_template('condenser_detail.html', **context)


@app.route('/create_condenser', methods=['POST', 'GET'])
def create_condenser():
    
    context = None

    if request.method == 'POST':
        
        # Пришел запрос с методом POST (пользователь нажал на кнопку 'Добавить Condenser')
        # Получаем название Condenser - это значение поля input с атрибутом name="name"
        Condenser_name = request.form['name']

        # Получаем описание Condenser - это значение поля input с атрибутом name="description"
        Condenser_description = request.form['description']

        # Получаем длину Condenser - это значение поля input с атрибутом name="length"
        Condenser_length = request.form['length']

        # Получаем ширину Condenser - это значение поля input с атрибутом name="width"
        Condenser_width = request.form['width']

        # Получаем высоту Condenser - это значение поля input с атрибутом name="height"
        Condenser_height = request.form['height']

        # Получаем вес Condenser - это значение поля input с атрибутом name="weight"
        Condenser_weight = request.form['weight']

        # Получаем артикул вентилятора Condenser - это значение поля input с атрибутом name="fan"
        Condenser_fan = request.form['fan']

        # Получаем кол-во вентиляторов Condenser - это значение поля input с атрибутом name="number_fan"
        Condenser_number_fan = request.form['number_fan']

        # Получаем расход воздуха Condenser - это значение поля input с атрибутом name="air_flow"
        Condenser_air_flow = request.form['air_flow']

        # Получаем уровень шума Condenser - это значение поля input с атрибутом name="noise"
        Condenser_noise = request.form['noise']

        # Определяем малошумность Condenser - это значение поля input с атрибутом name="low_noise"
        Condenser_low_noise = request.form['low_noise']
        if Condenser_low_noise == 'option1':
            Condenser_low_noise = True
        else:
            Condenser_low_noise = False
        # Получаем картинки Condenser - это значение поля input с атрибутом name="img_url"
        img_url_1 = request.form['img_url_1']  
        img_url_2 = request.form['img_url_2']  
        
        # Добавляем Condenser в базу данных
        db.session.add(Condenser(
            name=Condenser_name,
            description=Condenser_description, 
            length=Condenser_length,
            width=Condenser_width,
            height=Condenser_height,
            weight=Condenser_weight,
            fan=Condenser_fan,
            number_fan=Condenser_number_fan,
            air_flow=Condenser_air_flow,
            noise=Condenser_noise, 
            low_noise=Condenser_low_noise, 
            img_url_1=img_url_1, 
            img_url_2=img_url_2))

        # сохраняем изменения в базе
        db.session.commit()

        # Заполняем словарь контекста
        context = {
            'method': 'POST',
            'name': Condenser_name,
            'description' : Condenser_description,
            'length': Condenser_length,
            'width': Condenser_width,
            'height': Condenser_height,
            'weight': Condenser_weight,
            'fan' : Condenser_fan,
            'number_fan': Condenser_number_fan,
            'air_flow': Condenser_air_flow,
            'noise' : Condenser_noise, 
            'low_noise' : Condenser_low_noise
        }

    elif request.method == 'GET':

        # Пришел запрос с методом GET - пользователь просто открыл в браузере страницу по адресу http://127.0.0.1:5000/create_Condenser
        # В этом случае просто передаем в контекст имя метода и АККП по умолчанию
        context = {
            'method': 'GET',
            'low_noise' : 'option1'
        }
    return render_template('create_condenser.html', **context)


@app.route('/choose_condenser', methods=['POST', 'GET'])
def choose_condenser():
    capacity_list = Capacity.query.all()
    results = []
    condenser_id = []
    coef = 0.0028
    
    # Функция проверяет что введеная производительность меньше производительности конденсатора
    # в соответсвующей ей точке температур
    def add_line(Capa_point, capa_cond, max_temp):
        # определяем дельту введеной максимальной температуры и максимальной температуры конденсатора
        delta_max_temp = max_temp - capa.max_temp
        # индексируем мощьность конденсатора на дельту максимальных температур
        Capacity_point = capa_cond*delta_max_temp*coef + capa_cond
        # определяем разность дельт температур конденсатора и введеной точки
        delta_delta = capa.delta_temp - new_delta_temp
        
        if Capa_point <= Capacity_point:
        # если введеная производительность меньше производительностиконденсатора добавляем точку в список               
                            results.append({'condenser': Condenser.query.get(capa.condenser_id).name, 
                                            'img': Condenser.query.get(capa.condenser_id).img_url_1,
                                            'air_flow': Condenser.query.get(capa.condenser_id).air_flow, 
                                            'noise': Condenser.query.get(capa.condenser_id).noise, 
                                            'delta_temp': capa.delta_temp, 
                                            'capacity':Capacity_point,
                                            'delta_max_temp':delta_max_temp,
                                            'max_temp': max_temp,
                                            'min_temp': Capacity_min_temp,
                                            'delta': delta_delta,
                                            'condenser_id': Condenser.query.get(capa.condenser_id).id})
                            # добавляем айди конденсатора в список исключений                
                            condenser_id.append(capa.condenser_id)
                               

    # Определяет произодительность конденсатора, соответсвующую введеной дельте температур 
    #по двум точкам заданых дельт температур конденсатора 
    def find_capa (delta_max_list, delta_min_list):
        delta_max = delta_max_list.delta_temp
        capa_max = delta_max_list.capacity_point
        delta_min = delta_min_list.delta_temp
        capa_min = delta_min_list.capacity_point
        # определяем коэф дельты температур
        coef_delta = (new_delta_temp-delta_min)/(delta_max-delta_min)
        # находим производительность конденсатора при текущей дельте температур
        capa_result = coef_delta*(capa_max-capa_min)+capa_min
        # сравниваем производительность пользователя с полученной производительностью конденсатора
        add_line(Capacity_point,capa_result,Capacity_max_temp)


    if request.method == 'POST':
        
        # Пришел запрос с методом POST (пользователь нажал на кнопку 'Задать точку')
        
        Capacity_max_temp = int(request.form['max_temp'])
        Capacity_min_temp = int(request.form['min_temp'])
        Capacity_point = float(request.form['capacity'])  

        # Определяем дельту введенных температур
        new_delta_temp=Capacity_max_temp - Capacity_min_temp
        
        # Проверяем равенство текущей дельты температур и дельты температур в списке  
        # и ищем точки производительности конденсаторов больше введеной точки
        for capa in capacity_list:
            if new_delta_temp == capa.delta_temp:
                add_line(Capacity_point, capa.capacity_point, Capacity_max_temp)
        # снова проходим по списку производительностей конденсаторов
        for capa in capacity_list:
            # проверяем нет ли конденсатора в списке исключений  
            if capa.condenser_id not in condenser_id: 
                # определяем на каком отрезке от центральной точки дельта т=15 будем искать нашу точку
                if (new_delta_temp < 15 and capa.delta_temp <= 15):
                    # введеная дельта т меньше 15, определяем список точек производительности конденсатора меньше 15
                    delta_max_list = Capacity.query.filter_by(delta_temp = 15, condenser_id = capa.condenser_id).first()
                    delta_min_list = Capacity.query.filter_by(delta_temp = 10, condenser_id = capa.condenser_id).first() 
                    # определяем производительность конденсатора в соответствующую нашей дельте температур 
                    find_capa(delta_max_list, delta_min_list)

                elif (new_delta_temp > 15 and capa.delta_temp > 15):
                     # введеная дельта т больше 15, определяем список точек производительности конденсатора больше 15
                    delta_min_list = Capacity.query.filter_by(delta_temp = 15, condenser_id = capa.condenser_id).first()
                    delta_max_list = Capacity.query.filter_by(delta_temp = 20, condenser_id = capa.condenser_id).first() 
                    # определяем производительность конденсатора в соответствующую нашей дельте температур  
                    find_capa(delta_max_list, delta_min_list)
        # выводим полученный список конденсаторов с нужной производиткльностью
        context = {
                'results' : results,
                'cond_id' : condenser_id
                }

    elif request.method == 'GET':

        context = {
            'method': 'GET',
        }
          
    return render_template('choose_condenser.html', **context)
