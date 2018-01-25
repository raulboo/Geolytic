import json
import os

directory = os.path.dirname(os.path.dirname(__file__))   
save_filename = os.path.join(directory ,"geolytic_saves", "saves.json")

def save_game(city):
    with open(save_filename, 'r') as savefile:
        save_data = json.load(savefile)
    
    save_data[city.name] = city.variaveis
    
    with open(save_filename, 'w') as savefile:
        json.dump(save_data, savefile, indent=4)

        
def load_game(city):
    with open(save_filename, 'r') as savefile:
        load_data = json.load(savefile)
    
    try:
        load_city = load_data[city.name]
    except KeyError:
        return None
    
    city.variaveis = load_city
    city.name = load_city["name"]
    city.inttur = load_city["inttur"]
    city.ano_fundacao = load_city["ano_fundacao"]
    city.idh = load_city["idh"]
    city.exvida = load_city["exvida"]
    city.fluxoesc = load_city["fluxoesc"]
    city.renda = load_city["renda"]
    city.doenca_escolhida = load_city["doenca_escolhida"]
    city.classificacao = load_city["classificacao"]
    city.t = load_city["t"]
    city.pop = load_city["pop"]
    city.taxresid = load_city["taxresid"]
    city.taxrural = load_city["taxrural"]
    city.taxind = load_city["taxind"]
    city.taxcomer = load_city["taxcomer"]
    city.fatrural = load_city["fatrural"]
    city.fatind = load_city["fatind"]
    city.fatcomer = load_city["fatcomer"]
    city.invsaude = load_city["invsaude"]
    city.invesc = load_city["invesc"]
    city.invtur = load_city["invtur"]
    city.invcomer = load_city["invcomer"]
    city.invref = load_city["invref"]
    city.invpesq = load_city["invpesq"]
    city.invtotal = load_city["invtotal"]
    city.epid = load_city["epid"]
    city.escadulto = load_city["escadulto"]
    city.escola = load_city["escola"]
    city.popul = load_city["popul"]
    city.epid_last = load_city["epid_last"]
    city.fat = load_city["fat"]
    city.imptotal = load_city["imptotal"]
    city.cofre = load_city["cofre"]
    
    """
    for key, value in load_city:
        city.eval(key) = value
    """
    
    return city
    
    
def delete_game(city):
    with open(save_filename, 'r') as savefile:
        save_data = json.load(savefile)
    
    try:    
        del save_data[city.name]
    except KeyError:
        pass
       
    with open(save_filename, 'w') as savefile:
        json.dump(save_data, savefile, indent=4) 
    
    