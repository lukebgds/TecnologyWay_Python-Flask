from database import db # Importa a inst�ncia do SQLAlchemy

class Inscritos(db.Model): # Define um modelo de dados chamado "Inscritos"
    __tablename__ = 'Inscritos' # Nome da tabela no banco de dados
    id = db.Column(db.Integer, primary_key=True) # Coluna 'id' do tipo inteiro e chave prim�ria
    email = db.Column(db.String(120), unique=True, nullable=False)  # Coluna 'email' do tipo string, �nico e n�o nulo

    def __init__(self, email): # M�todo inicializador para a classe Inscritos
        self.email = email # Define o atributo 'email' ao criar uma inst�ncia do modelo