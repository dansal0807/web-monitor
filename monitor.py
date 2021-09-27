import requests

def web_monitor(weblink):
    request = requests.Session()
    r = request.get(weblink)
    response = r.status_code 
    if response < 200 :
        print("Reposta informativa: Tudo ocorreu bem até agora e o cliente deve continuar com a requisição ou ignorar se já concluiu o que gostaria.")
    elif 200 <= response < 300:
        print("Resposta de sucesso: Esta requisição foi bem sucedida. Seu servidor está ocorrendo bem.")
    elif 300 <= response < 400:
        print("Resposta de redirecionamento: A requisição tem mais de uma resposta possível. User-agent ou o user deve escolher uma delas. Não há maneira padrão para escolher uma das respostas.")
    elif 400 <= response < 500:
        print("Resposta de erro do cliente: Bad request -  o servidor não entendeu a requisição, pois está com uma sintaxe inválida.")
    elif 500 <= response < 505:
        print("Resposta de erro do servidor: Internal server error - O servidor encontrou uma situação com a qual não sabe lidar.")


while True:
    ask = input("diga-me o link do site que você deseja monitorar:\n")
    print("...\n")
    web_monitor(ask)
    