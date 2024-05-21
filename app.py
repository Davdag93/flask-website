from flask import Flask

app = Flask(__name__)

# Definiamo cosa visualizzare sull'homepage del sito SSR
@app.route("/")
def hello_world():
    return "Hello World!"
    
# In questo modo eseguiamo l'app in locale usando "host='0.0.0.0.'" e
# con "debug=True" l'app si aggiornerà automaticamente ad ogni cambiamento
if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)