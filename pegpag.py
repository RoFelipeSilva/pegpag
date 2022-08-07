from flask import Flask, make_response
from markupsafe import escape
from flask import render_template
from flask import request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/cad/usuario")
def usuario():
    return render_template('usuario.html', titulo="Usuário")

@app.route("/cad/caduser", methods=['POST'])
def caduser():
    return request.form

@app.route("/anuncio")
def anuncio():
    return render_template('anuncio.html', titulo="Anúncio")

@app.route("/anuncio/comprar")
def comprar():
    return render_template('comprar.html', titulo="Comprar")

@app.route("/anuncio/vender")
def vender():
    return render_template('vender.html', titulo="Publicar anúncio")

@app.route("/anuncio/cadanuncio", methods=['POST'])
def cadanuncio():
    return request.form

@app.route("/anuncio/perguntar")
def perguntar():
    return render_template('perguntar.html', titulo="perguntar")

@app.route("/anuncio/cadperguntar", methods=['POST'])
def cadperguntar():
    return request.form

@app.route("/anuncio/favoritos")
def favoritos():
    return render_template('favoritos.html')

@app.route("/config/categorias")
def categorias():
    return render_template('categorias.html', titulo="Cadastrar Categoria")

@app.route("/config/cadcategorias", methods=['POST'])
def cadcategorias():
    return request.form

@app.route("/relatorios")
def relatorios():
    return render_template('relatorios.html')

@app.route("/relatorios/vendas")
def relVendas():
    return render_template('relvendas.html', titulo="Relatório de vendas")

@app.route("/relatorios/compras")
def relCompras():
    return render_template('relcompras.html', titulo="Relatório de compras")

@app.route("/cad/contato")
def contato():
    return render_template('contato.html', titulo="Formlário de Contato")

@app.route("/cad/cadmsg", methods=['POST'])
def cadmsg():
    return request.form

@app.route("/adicfavoritos")
def adicfavoritos():
    return render_template('adicfavoritos.html')