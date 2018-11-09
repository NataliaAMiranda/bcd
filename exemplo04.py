from sqlalchemy import create_engine, and_, or_, Column, Integer, String, ForeignKey
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

engine = create_engine("sqlite:///lab05-ex0.sqlite")
Session = sessionmaker(bind=engine)
Base = declarative_base()


class Pessoa(Base):
    __tablename__ = 'Pessoa'
    idPessoa = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String)


class Telefone(Base):
    __tablename__ = 'Telefone'

    idTelefone = Column(Integer, primary_key=True, autoincrement=True)
    numero = Column(String)
    idPessoa = Column(Integer, ForeignKey('Pessoa', 'idPessoa'))
    pessoa = relationship('Pessoa,idPessoa')

    def __init__(self, numero, pessoa):
        self.numero = numero
        self.pessoa = pessoa


if __name__ == '__main__':
    # gerando o esquema do banco de dados
    Base.metadata.create_all(engine)

    # Em JAVA: Session session = new Session();
    session = Session()

    juca = Pessoa('Juca')

    juca.nome = 'Joca'

    session.add(juca)
    session.commit()
    session.close()
