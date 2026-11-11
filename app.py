from helpers.application import app

from controllers.instituicaoEnsinoController import instituicao_ensino_bp
from controllers.indexController import index_bp

app.register_blueprint(instituicao_ensino_bp)
app.register_blueprint(index_bp)

def main(arg=[]):
    app.run(debug=True)
