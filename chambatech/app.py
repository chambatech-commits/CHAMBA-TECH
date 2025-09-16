from flask import Flask, render_template, redirect, url_for, request, session
from datetime import timedelta

app = Flask(__name__)
app.secret_key = 'tu_clave_secreta_aqui' 
app.permanent_session_lifetime = timedelta(days=30)

# Configuración para el manejo de cookies de sesión en desarrollo.
# Es necesario para que la sesión persista en un entorno local.
app.config.update(
    SESSION_COOKIE_SAMESITE='Lax',
    SESSION_COOKIE_SECURE=False  
)

# Datos de productos de ejemplo.
# Aquí puedes expandir tu catálogo.
PRODUCTS = {
    'mouse-gaming-pro': {'name': 'Mouse Gaming Pro', 'price': 250000},
    'mouse-ergonomico': {'name': 'Mouse Ergonómico', 'price': 180000},
    'mouse-inalambrico': {'name': 'Mouse Inalámbrico', 'price': 120000},
    'teclado-mecanico-rgb': {'name': 'Teclado Mecánico RGB', 'price': 500000},
    'teclado-inalambrico': {'name': 'Teclado Inalámbrico Compacto', 'price': 350000},
    'teclado-membrana': {'name': 'Teclado de Membrana', 'price': 100000},
    'monitor-4k-ultra-ancho': {'name': 'Monitor 4K Ultra Ancho', 'price': 2500000},
    'monitor-gaming-144hz': {'name': 'Monitor Gaming 144Hz', 'price': 1500000},
    'monitor-oficina': {'name': 'Monitor de Oficina 24"', 'price': 600000},
    'audifonos-hd': {'name': 'Audífonos con Micrófono HD', 'price': 180000},
    'audifonos-bluetooth': {'name': 'Audífonos Inalámbricos Bluetooth', 'price': 250000},
    'audifonos-ruido': {'name': 'Audífonos con Cancelación de Ruido', 'price': 450000},
    'mousepad-gaming-xl': {'name': 'Mousepad Gaming XL', 'price': 80000},
    'mousepad-ergonomico': {'name': 'Mousepad Ergonómico', 'price': 45000},
    'mousepad-rgb': {'name': 'Mousepad RGB', 'price': 120000},
    'procesador-intel': {'name': 'Procesador Intel Core i9', 'price': 3500000},
    'tarjeta-grafica': {'name': 'Tarjeta Gráfica NVIDIA RTX', 'price': 5000000},
    'memoria-ram': {'name': 'Memoria RAM 16GB', 'price': 300000}
}

# Redirige la ruta principal a la página de inicio.
@app.route('/')
def redirect_to_home():
    return redirect(url_for('home'))

# Ruta para la página de inicio.
@app.route('/chamba-tech')
def home():
    user = session.get('user_id')
    return render_template('index.html', user=user, products=PRODUCTS)

# Rutas para las páginas estáticas principales.
@app.route('/cart.html')
def cart():
    user = session.get('user_id')
    cart_items = session.get('cart', {})
    total = sum(item['price'] * item['quantity'] for item in cart_items.values())
    return render_template('cart.html', user=user, cart_items=cart_items.values(), total=total)

@app.route('/contact.html')
def contact():
    user = session.get('user_id')
    return render_template('contact.html', user=user)

@app.route('/login.html', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        session.permanent = True
        session['user_id'] = email
        return redirect(url_for('home'))
    return render_template('login.html')

@app.route('/register.html', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        email = request.form.get('email')
        session.permanent = True
        session['user_id'] = email
        return redirect(url_for('home'))
    return render_template('register.html')

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('home'))

# Rutas para el carrito de compras.
@app.route('/add_to_cart/<product_id>')
def add_to_cart(product_id):
    if 'cart' not in session:
        session['cart'] = {}
    
    if product_id in session['cart']:
        session['cart'][product_id]['quantity'] += 1
    else:
        product = PRODUCTS.get(product_id)
        if product:
            session['cart'][product_id] = {
                'id': product_id,
                'name': product['name'],
                'price': product['price'],
                'quantity': 1
            }
    session.modified = True
    return redirect(url_for('cart'))

@app.route('/remove_from_cart/<product_id>')
def remove_from_cart(product_id):
    if 'cart' in session and product_id in session['cart']:
        del session['cart'][product_id]
        session.modified = True
    return redirect(url_for('cart'))

# Rutas para las categorías.
@app.route('/categories.html')
def categories():
    user = session.get('user_id')
    return render_template('categories.html', user=user)

@app.route('/mouses.html')
def mouses():
    user = session.get('user_id')
    return render_template('mouses.html', user=user)

@app.route('/teclados.html')
def teclados():
    user = session.get('user_id')
    return render_template('teclados.html', user=user)

@app.route('/audifonos.html')
def audifonos():
    user = session.get('user_id')
    return render_template('audifonos.html', user=user)

@app.route('/monitores.html')
def monitores():
    user = session.get('user_id')
    return render_template('monitores.html', user=user)

@app.route('/mousepads.html')
def mousepads():
    user = session.get('user_id')
    return render_template('mousepads.html', user=user)

@app.route('/componentes.html')
def componentes():
    user = session.get('user_id')
    return render_template('componentes.html', user=user)

if __name__ == '__main__':
    # Para despliegue, usa gunicorn.
    # Para desarrollo local, puedes usar este comando.
    app.run(debug=True)