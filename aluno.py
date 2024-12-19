class AlunoClass:

  def __init__(self, nome, sobrenome, nota):    

    self.nome = nome
    self.sobrenome = sobrenome
    self.nota = nota

  def mostrarAluno(self):

    return 'Aluno: ' + self.nome + ' ' + self.sobrenome + ' - Nota: ' + str(self.nota);    

  def salvar(self, conexao, colecao):

    aluno_dict = {
      "nome": self.nome,
      "sobrenome": self.sobrenome,
      "nota": self.nota
    }

    resultado = conexao[colecao].insert_one(aluno_dict)
    
    return resultado.acknowledged
