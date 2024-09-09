import time

def tomar_cafe():
    print("estou indo tomar cafe")

def  lavar_a_garrafa():
    print("estou indo lavar a garrafa")

def passar_o_cafe():
    global tem_cafe
    tem_cafe = "SIM"
    print("estou indo passar um novo cafe")


def murcegar_5_minutos():
    print("estou indo trabalhar")

def verifica_se_deu_hora_de_ir_embora():
    print("conferindo se ja acabou o expediente")
    global que_horas_sao
    que_horas_sao += 1
    print("agora sao " + str(que_horas_sao) + " horas")
    time.sleep(5)

def ir_embora_do_escritorio():
    print("estou indo EMBORA, a mala já esta lá foraaa!!!")





# Preparação antes de chegar no trabalho
tem_cafe = "NAO"
que_horas_sao = 9



#==============================================
# ROTINA PRINCIPAL
#==============================================

dic1 = {
    "um": "luciano", 
    "dois": "goncalves", 
    "tres": "rodrigues"
}


for i in dic1:
    print( dic1[i]  )









"""
# começa a rotina de trabalho
print("iniciando a rotina de trabalho")

while(que_horas_sao != 18):

    if (que_horas_sao - 9) % 3 == 0:
        tem_cafe = "NAO"
    
    if tem_cafe == "SIM":
        print("encontramos cafe na cozinha")
    else:
        print("QUERO CAFÉEEEE!!!")
        lavar_a_garrafa()
        passar_o_cafe()
    
    tomar_cafe()

    murcegar_5_minutos()

    verifica_se_deu_hora_de_ir_embora()



print("deu hora de ir embora")
print("vazando daqui!!!")



"""