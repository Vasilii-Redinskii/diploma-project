from fpdf import FPDF
 
def save_pdf(Condenser_name, Condenser_description, length, width, height, weight, fan, number_fan, noise, air_flow, max_temp,min_temp, Parameter_noise,Parameter_freon,Parameter_cool,Parameter_humidity,capacity_point,img_url_1,img_url_2):
    
    pdf = FPDF(orientation='P', unit='mm', format='A4')
    pdf.add_page()
    pdf.add_font('DejaVu', '', 'app/static/assets/font/DejaVuSansCondensed.ttf', uni=True)
    pdf.set_font('DejaVu', '', 20)
    
    H1=8
    H2=15
    #Head pdf file
    pdf.image('app/static/assets/images/logo_alterra.jpg', x=10, y=8, w=15)
    pdf.set_text_color(10, 130, 180)
    pdf.cell(200, 10, txt=Condenser_name, ln=1, align="C")
    pdf.set_line_width(1)
    pdf.set_draw_color(10, 130, 180)
    pdf.line(10, 20, 200, 20)

    #Body
    pdf.ln(5)
    pdf.set_font('DejaVu', '', 16)
    pdf.set_text_color(0, 0, 0)
    pdf.cell(200, H2, txt="Описание конденсатора.", ln=1, align="L")
    pdf.set_draw_color(170, 200, 210)
    pdf.line(10, 37, 80, 37)

    pdf.set_font('DejaVu', '', 12)
    pdf.cell(200, H1, txt=f"  {Condenser_description}", ln=1, align="L")
    pdf.cell(200, H1, txt=f"  Габариты (мм): {length} х {width} х {height}", ln=1, align="L")
    pdf.cell(200, H1, txt=f"  Вес (кг): {weight}", ln=1, align="L")
    pdf.cell(200, H1, txt=f"  Установлены вентиляторы: {fan} - {number_fan} шт.", ln=1, align="L")
    pdf.cell(200, H1, txt=f"  Максимальный уровень шума на 10м: {noise} д(Б)А", ln=1, align="L")
    pdf.cell(200, H1, txt=f"  Расход воздуха: {air_flow} куб.м в час", ln=1, align="L")
    pdf.set_font('DejaVu', '', 16)
    pdf.cell(200, H2, txt="Расчетные параметры:", ln=1, align="L")
    pdf.line(10, 100, 75, 100)
    pdf.set_font('DejaVu', '', 12)
    pdf.cell(200, H1, txt=f"  Температура конденсации: {max_temp} °С", ln=1, align="L")
    pdf.cell(200, H1, txt=f"  Температура окружающей среды: {min_temp} °С", ln=1, align="L")
    pdf.cell(200, H1, txt=f"  Уровень шума: {Parameter_noise} д(Б)А", ln=1, align="L")
    pdf.cell(200, H1, txt=f"  Тип фреона: {Parameter_freon}", ln=1, align="L")
    pdf.cell(200, H1, txt=f"  Переохлаждение: {Parameter_cool}", ln=1, align="L")
    pdf.cell(200, H1, txt=f"  Относительная влажность: {Parameter_humidity}%", ln=1, align="L")
    pdf.cell(200, H1, txt="  Δt перегрева на нагнетании = 35°C", ln=1, align="L")
    pdf.set_font('DejaVu', '', 16)
    pdf.cell(200, H2, txt=f"Расчетная производительность: {capacity_point} кВт", ln=1, align="L")
    pdf.line(10, 170, 130, 170)
    pdf.cell(200, H2, txt="Контакты:", ln=1, align="L")
    pdf.line(10, 186, 40, 186)
    pdf.set_font('DejaVu', '', 12)
    pdf.cell(200, H1, txt="  Тел: +7 (812) 920-03-75", ln=1, align="L")
    pdf.cell(200, H1, txt="  E-mail: info@alterra.com.ru", ln=1, align="L")
    #Add image
    pdf.image(f'app/static/assets/images/condenser/{img_url_1}', x=110, y=30, w=100)
    pdf.image(f'app/static/assets/images/condenser/{img_url_2}', x=110, y=90, w=100)


    #End pdf file
    pdf.line(10, 265, 200, 265)
    pdf.set_text_color(10, 130, 180)
    pdf.ln(65)
    pdf.set_font('DejaVu', '', 12)
    pdf.cell(200, 5, txt='''Общество с ограниченной ответственностью «АЛТЕРРА» ''', ln=20, align="C")

    
    pdf.output("add_image.pdf",'F')
 
#if __name__ == '__main__':
    #save_pdf('AKN 2482', 'Condenser AKN 2482',500,600,900,1200,910,6,80,65000,48,21,60,'R404',0,40,787.2,'1.jpg','3.jpg')

