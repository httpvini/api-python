from flask import render_template
import connexion

# Cria a instancia da aplicação com connexion
app = connexion.App(__name__, specification_dir='./')

#Lê o arquivo swagger.yml para configurar os endpoints
app.add_api('swagger.yml')

@app.route('/')
def home():
    return render_template('home.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
