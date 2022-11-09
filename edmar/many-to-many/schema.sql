CREATE TABLE IF NOT EXISTS atracoes (
  id INTEGER PRIMARY KEY,
  nome TEXT NOT NULL,
  descricao text NOT NULL,
  tipo text NOT NULL,
  horarios text NOT NULL
);

CREATE TABLE IF NOT EXISTS roteiros (
  id INTEGER PRIMARY KEY,
  nome TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS atracao_roteiros (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  atracao_id INTEGER,
  roteiro_id INTEGER,
  FOREIGN KEY(atracao_id) REFERENCES atracao(id),
  FOREIGN KEY(roteiro_id) REFERENCES roteiro(id)
);