from flask import Flask, render_template
app = Flask(__name__,static_folder='static')
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ciel')
def ciel():
    return render_template('ciel.html')

@app.route('/etud-sup')
def etudsup():
    return render_template('etud-sup.html')


@app.route('/snir')
def snir():
    return render_template('snir.html')

if __name__ == '__main__':
    app.run()






# Avec le code d’exemple mis en place, générez 3 routes 
# « /ciel », « /snir » et « /etudes-sup » menant à 3 pages 
# « ciel.html », « snir.html » et « etudes-sup.html »
# que vous aurez produit au préalable.