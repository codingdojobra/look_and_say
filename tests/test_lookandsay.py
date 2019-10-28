import unittest
#from lookandsay import

def retorna_descricao(num):
    descricao_numero = []
    resultado_final = ''
    for i in range(len(num)):
        descricao_numero.append({num[i] : 1})
    for dicionario in descricao_numero:
        for v in dicionario:
            resultado_final += str(dicionario[v]) + str(v)
    return resultado_final

class TestLookAndSay(unittest.TestCase):
    def test_framework(self):
        self.assertTrue(True)

    def test_1(self):
        num = "1"
        esperado = "11"
        self.assertEqual(esperado, retorna_descricao(num))

    def test_2(self):
        num = "11"
        esperado = "21"
        self.assertEqual(esperado, retorna_descricao(num))

    def test_3(self):
        num = "21"
        esperado = "1211"
        self.assertEqual(esperado, retorna_descricao(num))

if __name__ == '__main__':
    unittest.main()
