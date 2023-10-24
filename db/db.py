from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Sequence, Boolean, Double
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

# Cria um objeto de conexão
engine = create_engine("postgresql://admin:admin@postgres:5432/database")


# Cria uma classe de modelo de usuário
Base = declarative_base()


class Usuario(Base):
    __tablename__ = "usuario"
    id = Column(Integer, Sequence("user_id_seq"), primary_key=True)
    nome = Column(String(50))
    sobrenome = Column(String(50))
    email = Column(String(120), unique=True)


class OrdemServico(Base):
    __tablename__ = "ordem_servico"
    id = Column(Integer, Sequence("user_id_seq"), primary_key=True)
    title = Column(String(50))
    geojson = Column(String(50))
    lat = Column(Double)
    lng = Column(Double)
    relator = Column(String(50))
    date = Column(String)
    status = Column(Boolean)


# Cria a tabela no banco de dados
Base.metadata.create_all(engine)


# Adiciona um usuário à tabela
def add_user(n, s, e):
    Session = sessionmaker(bind=engine)
    session = Session()

    novo_usuario = Usuario(nome=n, sobrenome=s, email=e)
    session.add(novo_usuario)
    session.commit()


# Adiciona um usuário à tabela
def add_Ordem(ordem):
    Session = sessionmaker(bind=engine)
    session = Session()
    nova_ordem = OrdemServico(
        title=ordem.title,
        geojson=ordem.geojson,
        lat=ordem.lat,
        lng=ordem.lng,
        relator=ordem.relator,
        date=ordem.date,
        status=ordem.status,
    )
    session.add(nova_ordem)
    session.commit()
