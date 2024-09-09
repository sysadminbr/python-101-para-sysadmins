#------------------------------------------------
# Chuck norris é o carah!
#------------------------------------------------

import random
import requests

chave_api_whatsapp = "B6D711F8DE4D4FD5936544120E713976"
url_api_whatsapp = "http://192.168.100.123:8080/message/sendText/tmp1"


TODAS_AS_FRASES_DO_CHUCK = [	
	"Chuck Norris era um dos personagens originais do jogo “Street Fighter II”. Ele só foi removido porque todos os botões faziam ele dar um roundhouse kick. Quando perguntaram sobre essa falha do jogo, Chuck Norris respondeu: “Que falha do jogo?",
	"Chuck Norris uma vez comeu 72 Kg de carne em uma hora. Ele passou os primeiros 45 minutos fazendo sexo com a garçonete.",
	"O título original para Star Wars era “Skywalker: Texas Ranger”, estrelando Chuck Norris.",
	"O Triângulo das Bermundas era um quadrado até Chuck Norris dar um roundhouse kick em um dos cantos.",
	"A maioria das pessoas tem 23 pares de cromossomos. Chuck Norris tem 72. Todos venenosos.",
	"Chuck Norris não usa relógio. Ele decide que horas são.",
	"Quando Chuck Norris joga War, George Bush se esconde debaixo da cama.",
	"Quando Chuck Norris quer comer um ovo, ele quebra a galinha.",
	"O pulso de Chuck Norris é medido na Escala Richter.",
	"A Teoria do Caos se baseia na Teoria de Norris. Não são as asas de uma borboleta que causam tempestades do outro lado do mundo. São roundhouse kicks de Chuck Norris enquanto ele treina.",
	"Na China, acredita-se que pêlos da barba de Chuck Norris são afrodisíacos.",
	"Chuck Norris às vezes levita. É a Terra se afastando por alguns momentos dele… de medo.",
	"Chuck Norris usa Tabasco como colírio.",
	"Chuck Norris não é politicamente correto. Ele é correto. Sempre.",
	"Chuck Norris não joga bem. Jogar é para crianças.",
	"Pense em uma mulher gostosa. Chuck Norris já comeu.",
	"Quando Chuck Norris joga Banco Imobiliário ele afeta a economia mundial.",
	"Ataques do coração são a principal causa de morte de homens de 45 a 65 anos, mas Chuck Norris ainda é a causa principal de morte de homens de 0 a 125 anos.",
	"As 7 maravilhas do mundo moderno são: a mão direita e esquerda de Chuck Norris, seu pé direito e esquerdo, seu cinturão, seu chapéu e sua barba.",
	"Quando Chuck Norris espirra, ele não diz “Atchiiiin”, ele diz “MORRAM TODOS!”. E isto realmente acontece.",
	"As maiores causas de morte nos Estados Unidos são: 1) Ataque cardíaco, 2) Chuck Norris, 3) Câncer.",
	"O vento deslocado por um roundhouse kick de Chuck Norris pode ser sentido a 2 milhões de kilômetros de distância.",
	"Chuck Norris pode espirrar com os olhos abertos.",
	"Chuck Norris consegue lamber seu cotovelo.",
	"Chuck Norris pode ganhar em black jack (21) com apenas uma carta.",
	"Chuk Norris não tem casa. Ele escolhe uma casa e seus moradores se mudam.",
	"Quando urina, Chuck Norris pode facilmente perfurar titânio.",
	"Chuck Norris inventou o preto. Na verdade, ele inventou todas as cores conhecidas. Exceto o rosa. Tom Cruise inventou essa.",
	"Chuck Norris inventou o sexo, as drogas e o rock n’ roll. Nessa ordem.",
	"70% do corpo humano é água. 70% do corpo de Chuck Norris é seu pênis",
	"Chuck Norris não segue tendências. As tendências seguem Chuck Norris. Aí então, as tendências acabam. Afinal, ninguém segue Chuck Norris impunemente.",
	"Uma vez Chuck Norris mijou num isqueiro. Nascia o lança-chamas.",
	"Quando Chuck Norris recebe os impostos, ele manda de volta folhas brancas com uma foto dele agachado, pronto para atacar. Chuck Norris não teve que pagar impostos nunca. Nunca!",
	"Quando Chuck Norris faz flexões, ele não levanta o próprio peso. Ele empurra o planeta.",
	"Chuck Norris entrou para o Clube da Luta. O Clube perdeu.",
	"Chuck Norris separou com sucesso gêmeos siameses com apenas um roundhouse kick.",
	"Para evitar Chuck Norris, um raio nunca cai no mesmo lugar.",
	"Chuck Norris é tão poderoso que faz qualquer vírus ficar doente. Ele é responsável pela erradicação da varíola.",
	"Arqueologistas desenterraram um velho dicionário inglês de 1230. Ele define “vítima” como “aquele que encontra Chuck Norris”.",
	"O Muro de Berlim caiu. Chuck Norris não se apóia mais nos muros para mijar.",
	"Chuck Norris pode segurar o fôlego por nove anos.",
	"Não existe a tecla Control no teclado de Chuck Norris. Chuck Norris está sempre no controle.",
	"Chuck Norris e tão forte que ele enfiou a faca no olho e a faca que ficou cega.",
	"Sobreviver a um ataque de Chuck Norris seria o mesmo que acertar 4 vezes seguidas na loteria. 4 vezes !!!",
	"Chuck Norris não toma banho, ele ameaça a sujeira com um  roundhouse kick, e ela vai embora.",
	"O seriado 24 horas era pra ser estreiado por Chuck Norris, mais o problema é que ele resolvia tudo em 5 minutos.",
	"Chuck norris faz gol olímpico no pebolim",
	"Chuck Norris não pega gripe suína,a gripe suína pega Chuck Norris",
	"Chuck Norris jogou roleta russa com o sua bazooka totalmente carregada e venceu!!!",
	"Chuk Norris não liga o chuveiro, ele encara ele até ele chorar.",
	"Chuck Norris nunca vai morrer de ataque cardíaco. Seu coração não é tolo o bastante para “atacar” Chuck Norris.",
	"Chuck Norris não usa sal de frutas. Ele usa antraz.",
]



frase_escolhida = random.choice(TODAS_AS_FRASES_DO_CHUCK)

resultado_api = requests.post(
    url=url_api_whatsapp,
    headers={"apikey": chave_api_whatsapp},
    json={
        "number": "5531997350000",
        "textMessage": {
            "text": frase_escolhida
        }
    }

)


print(f'a frase escolhida de chuck foi: \n{frase_escolhida}')

