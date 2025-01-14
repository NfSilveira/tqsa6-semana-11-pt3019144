import unittest
from aluno import AlunoClass 
from turma import TurmaClass
from conexao import ConexaoClass
import mongomock #Projeto: https://github.com/mongomock/mongomock


class alunoTest(unittest.TestCase):

  @mongomock.patch(servers=(('localhost.com', 27017),))
  def setUp(self):

    print('Teste', self._testMethodName, 'sendo executado...')

    self.aluno = AlunoClass('Fabio', 'Teixeira', 10)
    self.turma = TurmaClass()
    self.turma.cadastrarAlunos([self.aluno])
    self.conexao = ConexaoClass.conexaoMongoDB(self, url = 'localhost.com', banco = 'faculdade')

  def test_salvarAluno(self):

    cliente_mock = mongomock.MongoClient()
    conexao_mock = cliente_mock['faculdade']
    mock_colecao = conexao_mock['alunos']
    
    # Salva o aluno usando o método salvar
    resultado = self.aluno.salvar(conexao=conexao_mock, colecao='alunos')

    # Verifica se o aluno foi salvo corretamente
    self.assertTrue(resultado, "Aluno não foi salvo corretamente!")

  def test_salvarTurma(self):   

    resposta = self.turma.salvar(conexao = self.conexao, colecao = 'turma') 

    self.assertEqual(True, resposta, 'Turma cadastrada incorretamente!')

if __name__ == "__main__":
  unittest.main()