import os
import time
from geolytic_modules.savegl import save_game, load_game
from geolytic_modules.CityClass import CityClass
from geolytic_info.info import geolytic_info 

cmd = os.system
def cls(): cmd('cls')
def titlegame(): print("\n" + ("Geolytic " + geolytic_info['version'] + " - Criado por Raul Schütz").center(100) + "\n" * 2)
def twofloat(arg): return format(arg, '.2f')


class Voltar():
    def __init__(self):
        self.voltar = False
        

class BadInput(Exception): pass
class NegPrev(Exception): pass
class BadValue(Exception): pass


def start():
    cmd('@echo off')
    cmd('title Geolytic')
    cmd('color 3f')
    cmd('mode con: cols=100 lines=45')
    cls()
    titlegame()
    c = CityClass(input("  Escolha o nome de seu município: ").title())
    loading = load_game(c)
    if loading != None:
        c = loading
    while True:
        interface(c)

            
def bad_input():
    print("\n" + "   Comando Invalido", end="\r")
    time.sleep(1)
    print(" " * 19, end="\r")
    

def neg_prev():
    print("\n" + "   Gastos ultrapassam o orçamento", end="\r")
    time.sleep(1.5)
    print(" " * 33, end="\r")
  
    
def interface(c):
    cls()
    c.update_variaveis()
    save_game(c)
    titlegame()
    print(("{} de {}".format(c.classificacao, c.name)).center(100) + "\n" * 3)
    strpop, stridh, strano = "   População Total = {}".format(c.pop), "IDH = {}".format(format(c.idh, '.3f')), "Ano = {}   ".format(c.ano_fundacao + c.t)
    print(strpop + stridh.center(100 - (2 * len(strpop))) + strano.rjust(35 - len(strano)) + "\n")
    print("   Ultimas notícias:" + "\n")
    c.noticias()
    strexvida, strescadulto = "   Expectativa de vida: {} anos".format(format(c.exvida, '.1f')), "Escolaridade Adulta: {}%".format(twofloat((c.escadulto)*100)),
    strfluxoesc, strrenda = ("Fluxo Escolar: {}%".format(twofloat((c.fluxoesc)*100))).ljust(len(strescadulto)), "Renda Média: R$ {}   ".format(twofloat(c.renda))
    print("\n"*2 + "Saúde".center(33) + "Educação".center(34) + "Renda".center(33) + "\n")
    print(strexvida + (strfluxoesc.ljust(len(strescadulto))).center(100 - (len(strexvida)*2)) + strrenda.rjust(len(strescadulto)))
    print(strescadulto.center(100) + "\n"*2)
    strfatrural, strfatind = "   Agropecuária: {}%".format(twofloat(c.fatrural * 100)), "   Atividade Industrial: {}%".format(twofloat(c.fatind * 100)),
    strfatcomer, strfat = "   Comércio e Turismo: {}%".format(twofloat(c.fatcomer * 100)), "   Faturamento Total Municipal: R$ {}".format(twofloat(c.fat))
    strcofre, strinvtotal = "Impostos Recolhidos: R$ {}".format(twofloat(c.imptotal)), "Orçamento Público: R$ {}".format(twofloat(c.cofre))
    strimptotal, strprevisao = "Investimentos Totais: R$ {}".format(twofloat(c.invtotal)), "Débito para o próximo ano: R$ {}   ".format(twofloat(c.cofre - c.invtotal))
    print("   Atividades Econômicas:" + ("Dados da prefeitura:".ljust(len(strprevisao))).rjust(75) + "\n")
    print(strfatrural + (strcofre.ljust(len(strprevisao))).rjust(100 - len(strfatrural)))
    print(strfatind + (strinvtotal.ljust(len(strprevisao))).rjust(100 - len(strfatind)))
    print(strfatcomer + (strimptotal.ljust(len(strprevisao))).rjust(100 - len(strfatcomer)) + "\n")
    print(strfat + strprevisao.rjust(100 - len(strfat)))
    print("\n" * 2) 
    print("   [T] para modificar Carga Tributária") 
    print("   [I] para modificar Investimentos") 
    print("   [P] para pular para o Próximo Ano" + "\n" * 2)
    def inputer():
        the_input = input("   Opção: ").lower()
        try:
            if the_input not in ["t","i","p","reset"]:
                raise BadInput
            if the_input == "t":
                voltar.voltar = False
                while not voltar.voltar:
                    impostos(c)
                return 0
            elif the_input == "i":
                voltar.voltar = False
                while not voltar.voltar:            
                    investimentos(c)
                return 0
            elif the_input == "p":
                if (c.cofre - c.invtotal) < 0: raise NegPrev
                c.next()
                return 0
            elif the_input == "reset":
                os.system(__file__)
        except BadInput:
            bad_input()
        except NegPrev:
            neg_prev()
    inputer()

        
def investimentos(c):
    cls()
    titlegame()
    print(("{} de {}".format(c.classificacao, c.name)).center(100) + "\n" * 3)
    print("   Investimentos:" + "\n")
    print("   [S] para modificar os Investimentos na Saúde (Atual: R$ {})".format(c.invsaude)) 
    print("   [E] para modificar os Investimentos na Educação (Atual: R$ {})".format(c.invesc))
    print("   [C] para modificar os Investimentos no Comécio (Atual: R$ {})".format(c.invcomer))
    print("   [T] para modificar os Investimentos no Turismo (Atual: R$ {})".format(c.invtur))
    print("   [R] para modificar os Investimentos na Reforma Agrária (Atual: R$ {})".format(c.invref))
    print("   [P] para modificar os Investimentos em Pesquisa (Atual: R$ {})".format(c.invpesq) + "\n")
    print("   [V] para voltar ao menu" + "\n")
    def investimento_inputer():
        investimento_input = input("   Opção: ").lower()
        commands = ["s", "e", "c", "t", "r", "p", "v"]
        try:
            if investimento_input not in commands:
                raise BadInput
            if investimento_input == "v":
                voltar.voltar = True
                return 0
            # investimentos = {"s":"c.invsaude", "e":"c.invesc", "c":"c.invcomer", "t":"c.invtur", "r":"c.invref", "p":"c.invpesq"}
            print() 
            formats = ["Investimentos na Saúde", "Investimentos na Educação", "Investimentos no Comécio", 
            "Investimentos no Turismo", "Investimentos na Reforma Agrária", "Investimentos em Pesquisa", 
            "[[[Erro em investimento_inputer(): isto não deveria aparecer]]]"]
            formatar = dict(zip(commands, formats))
            change = int(input("   Modificar {} para (em R$): ".format(formatar[investimento_input])))
            if change < 1: raise BadValue
            # eval(investimentos[investimento_input] + " = inv_change")
            if investimento_input == "s": c.invsaude = change
            elif investimento_input == "e": c.invesc = change
            elif investimento_input == "c": c.invcomer = change
            elif investimento_input == "t": c.invtur = change
            elif investimento_input == "r": c.invref = change
            elif investimento_input == "p": c.invpesq = change
            c.invtotal = c.invsaude + c.invesc + c.invtur + c.invcomer + c.invref + c.invpesq
        except BadValue:
            print("\n" + "   Por favor, coloque apenas valores maiores ou iguais a 1", end="\r")
            time.sleep(1.5)
            print(" " * 58, end="\r")
            investimento_inputer()
        except (BadInput, ValueError):
            bad_input()
            investimento_inputer()
    investimento_inputer()
    
    
def impostos(c):
    cls()
    titlegame()
    print(("{} de {}".format(c.classificacao, c.name)).center(100) + "\n" * 3)
    print("   Impostos:" + "\n")
    print("   [P] para modificar o Imposto de Renda (Atual: {}%)".format(c.taxresid * 100)) 
    print("   [R] para modificar os Tributos sobre Produção Rural (Atual: {}%)".format(c.taxrural * 100))
    print("   [I] para modificar os Tributos sobre Produção Industrial (Atual: {}%)".format(c.taxind * 100))
    print("   [C] para modificar os Tributos sobre Comércio de Produtos (Atual: {}%)".format(c.taxcomer * 100) + "\n")
    print("   [V] para voltar ao menu" + "\n")
    def imposto_inputer():
        imposto_input = input("   Opção: ").lower()
        
        try:
            commands = ["p", "r", "i", "c", "v"]
            if imposto_input not in commands:
                raise BadInput
            if imposto_input == "v":
                voltar.voltar = True
                return 0
            print() 
            formatar = dict(zip(commands,["Imposto de Renda", "Tributos sobre Produção Rural", "Tributos sobre Produção Industrial", 
            "Tributos sobre Comércio de Produtos", "[[[Erro em imposto_inputer(): isto não deveria aparecer]]]"]))
            change = int(input("   Modificar {} para (em %): ".format(formatar[imposto_input]))) / 100
            if change < 0.005 or change > 1: raise BadValue
            elif imposto_input == "p": c.taxresid = change
            elif imposto_input == "r": c.taxrural = change
            elif imposto_input == "i": c.taxind = change
            elif imposto_input == "c": c.taxcomer = change
        except BadValue:
            print("\n" + "   Por favor, coloque apenas valores entre 0.5 e 100", end="\r")
            time.sleep(1.5)
            print(" " * 58, end="\r")
        except (BadInput, ValueError):
            bad_input()
    imposto_inputer()
        
        
    
if __name__ == '__main__':
    voltar = Voltar()
    start()



# Adicionar:
# - Segurança Pública
# - Temperatura, Vegetação... (Clima)
# - Recursos Naturais
# - Qt. de Água na Região

