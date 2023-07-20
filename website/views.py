from flask import Blueprint ,render_template , request ,redirect ,url_for
from flask_login import login_user , login_required , logout_user , current_user
from website.forms import hm , ElectricGuitarForm
from website.dbconnect import get_mysql_guitars
from website.functions import  Jsonify , generate_code
from mysql.connector import Error




views = Blueprint( 'views' , __name__ ) 



@views.route('/departments', methods=['GET','POST'])
@login_required
def departments():
    return render_template("departments.html")







@views.route('/electric' , methods=['GET','POST'])
@login_required
def electric():
    basequery='SELECT * FROM product_catalog.electric_guitars;'
    db =get_mysql_guitars()
    cursor = db.cursor()
    cursor.execute(basequery)
    data = cursor.fetchall()
    
    
    if 'code' in request.form:
        
        code = request.form['code']
        if code.isspace() or code == '':
                 
                 cursor.execute(basequery)
        
        else:
                 cursor.execute(f"SELECT * FROM product_catalog.electric_guitars where product_code='{code}'")
                 data = cursor.fetchall() 


    if 'brand' in request.form:
        
        brand = request.form['brand']
        if brand.isspace() or brand == '':
                 
                 cursor.execute(basequery)
        
        else:
                 cursor.execute(f"SELECT * FROM product_catalog.electric_guitars where brand='{brand}'")
                 data = cursor.fetchall()              
               

    if 'model' in request.form:
        
        model = request.form['model']
        if model.isspace() or model == '':
                 
                 cursor.execute(basequery)
        
        else:
                 cursor.execute(f"SELECT * FROM product_catalog.electric_guitars where model='{model}'")
                 data = cursor.fetchall() 
                             
    
    return render_template("electric.html", data=data  )







@views.route('/acoustic', methods=['GET','POST'])
@login_required
def acoustic():
    basequery='SELECT * FROM product_catalog.acoustic_guitars;'
    db =get_mysql_guitars()
    cursor = db.cursor()
    cursor.execute(basequery)
    data = cursor.fetchall()

    if 'code' in request.form:
        
        code = request.form['code']
        if code.isspace() or code == '':
                 
                 cursor.execute(basequery)
        
        else:
                 cursor.execute(f"SELECT * FROM product_catalog.acoustic_guitars where product_code='{code}'")
                 data = cursor.fetchall() 


    if 'brand' in request.form:
        
        brand = request.form['brand']
        if brand.isspace() or brand == '':
                 
                 cursor.execute(basequery)
        
        else:
                 cursor.execute(f"SELECT * FROM product_catalog.acoustic_guitars where brand='{brand}'")
                 data = cursor.fetchall()              
               

    if 'model' in request.form:
        
        model = request.form['model']
        if model.isspace() or model == '':
                 
                 cursor.execute(basequery)
        
        else:
                 cursor.execute(f"SELECT * FROM product_catalog.acoustic_guitars where model='{model}'")
                 data = cursor.fetchall() 


    return render_template("acoustics.html",data=data)



@views.route('/classical', methods=['GET','POST'])
@login_required
def classical():
   basequery='SELECT * FROM product_catalog.classical_guitars;'
   db =get_mysql_guitars()
   cursor = db.cursor()
   cursor.execute(basequery)
   data = cursor.fetchall()
   if 'code' in request.form:
        
        code = request.form['code']
        if code.isspace() or code == '':
                 
                 cursor.execute()
        
        else:
                 cursor.execute(f"SELECT * FROM product_catalog.classical_guitars where product_code='{code}'")
                 data = cursor.fetchall() 

   if 'brand' in request.form:
        
        brand = request.form['brand']
        if brand.isspace() or brand == '':
                 
                 cursor.execute(basequery)
        
        else:
                 cursor.execute(f"SELECT * FROM product_catalog.classical_guitars where brand='{brand}'")
                 data = cursor.fetchall()              
               

   if 'model' in request.form:
        
        model = request.form['model']
        if model.isspace() or model == '':
                 
                 cursor.execute(basequery)
        
        else:
                 cursor.execute(f"SELECT * FROM product_catalog.classical_guitars where model='{model}'")
                 data = cursor.fetchall() 
 
    
   return render_template("classical.html",data=data)




@views.route('/bass' , methods=['GET','POST'])
@login_required
def bass():
   basequery='SELECT * FROM product_catalog.bass_guitars;'
   db =get_mysql_guitars()
   cursor = db.cursor()
   cursor.execute(basequery)
   data = cursor.fetchall()

   if 'code' in request.form:
        
       code = request.form['code']
       if code.isspace() or code == '':
                 
             cursor.execute(basequery)
        
       else:
            cursor.execute(f"SELECT * FROM product_catalog.bass_guitars where product_code='{code}'")
            data = cursor.fetchall() 



   if 'brand' in request.form:
        
        brand = request.form['brand']
        if brand.isspace() or brand == '':
                 
                 cursor.execute(basequery)
        
        else:
                 cursor.execute(f"SELECT * FROM product_catalog.bass_guitars where brand='{brand}'")
                 data = cursor.fetchall()              
               



   if 'model' in request.form:
        
        model = request.form['model']
        if model.isspace() or model == '':
                 
                 cursor.execute(basequery)
        
        else:
                 cursor.execute(f"SELECT * FROM product_catalog.bass_guitars where model='{model}'")
                 data = cursor.fetchall() 
    

   return render_template("bass.html",data=data)



@views.route('/other')
@login_required
def other():
   db =get_mysql_guitars()
   cursor = db.cursor()
   cursor.execute('SELECT * FROM product_catalog.other;')
   data = cursor.fetchall()
    
   return render_template("other.html",data=data)





@login_required
@views.route('/add_electric', methods=['GET', 'POST'])
def addelectric():
    form = ElectricGuitarForm()
    try:
       db = get_mysql_guitars() 
    except:
       return render_template("databasefail.html")

    if request.method == 'POST' and form.validate_on_submit():
       

        cursor = db.cursor()

        brand = request.form.get('brand')
        model = request.form.get('model')
        shape = request.form.get('shape')
        top = request.form.get('top')
        body = request.form.get('body')
        neck = request.form.get('neck')
        fretboard = request.form.get('fretboard')
        frets = request.form.get('frets')
        strings = request.form.get('strings')
        pickupnum = request.form.get('pickupnum')
        pickuptype = request.form.get('pickuptype')
        bridge = request.form.get('bridge')
        price = request.form.get('price')
        print(brand, model, shape, top, body, neck,fretboard ,frets, strings,pickupnum,pickuptype, bridge, price)

        woods=Jsonify(top, body, neck, fretboard)
        code= generate_code()


        query = '''INSERT INTO product_catalog.electric_guitars
                   (product_code, brand, model, neck_shape, woods, num_of_frets, num_of_strings, num_of_pickups, pickup_type, bridge_type, price, in_stock)
                   VALUES ('{}', '{}', '{}', '{}', '{}', {}, {}, {}, '{}', '{}', {}, 0);'''.format(code, brand, model, shape, woods, frets, strings, pickupnum, pickuptype,bridge, price)
            
            
                
        cursor.execute(query)
        db.commit()
        db.close() 
        return "Guitar successfully added to the database"
    
        
        

        
        

        
    return render_template("addelectric.html", form=form)





@login_required
@views.route('/add_acoustic', methods=['GET', 'POST'])
def addacoustic():
    form = ElectricGuitarForm()
    try:
       db = get_mysql_guitars() 
    except:
       return render_template("databasefail.html")

    if request.method == 'POST' and form.validate_on_submit():
       

        cursor = db.cursor()

        brand = request.form.get('brand')
        model = request.form.get('model')
        shape = request.form.get('shape')
        top = request.form.get('top')
        body = request.form.get('body')
        neck = request.form.get('neck')
        fretboard = request.form.get('fretboard')
        frets = request.form.get('frets')
        strings = request.form.get('strings')
        pickupnum = request.form.get('pickupnum')
        pickuptype = request.form.get('pickuptype')
        bridge = request.form.get('bridge')
        price = request.form.get('price')
        print(brand, model, shape, top, body, neck,fretboard ,frets, strings,pickupnum,pickuptype, bridge, price)

        woods=Jsonify(top, body, neck, fretboard)
        code= generate_code()


        query = '''INSERT INTO product_catalog.acoustic_guitars
                   (product_code, brand, model, neck_shape, woods, num_of_frets, num_of_strings, num_of_pickups, pickup_type, bridge_type, price, in_stock)
                   VALUES ('{}', '{}', '{}', '{}', '{}', {}, {}, {}, '{}',  {}, 0);'''.format(code, brand, model, shape, woods, frets, strings, pickupnum, pickuptype, price)
            
        print(query)    
                
        cursor.execute(query)
        db.commit()
        db.close() 
        return "Guitar successfully added to the database"
    
        
        

        
        

        
    return render_template("addacoustic.html", form=form)

