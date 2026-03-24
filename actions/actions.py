import requests
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

class ActionConverterMoeda(Action):

    def name(self):
        return "action_converter_moeda"

    def run(self, dispatcher, tracker, domain):
        valor = tracker.get_slot("valor")
        origem = tracker.get_slot("moeda_origem")
        destino = tracker.get_slot("moeda_destino")

        if valor is None or not origem or not destino:
            dispatcher.utter_message(
                text="Por favor, informe o valor, a moeda de origem e a de destino."
            )
            return []

        mapa = {
            "real": "BRL", "reais": "BRL",
            "dolar": "USD", "dólar": "USD", "dólares": "USD",
            "euro": "EUR"
        }

        origem_code = mapa.get(str(origem).lower(), origem.upper())
        destino_code = mapa.get(str(destino).lower(), destino.upper())

        try:
            url = f"https://economia.awesomeapi.com.br/json/last/{origem_code}-{destino_code}"
            response = requests.get(url)

            if response.status_code != 200:
                dispatcher.utter_message(text="Erro ao acessar a API.")
                return []

            data = response.json()
            par = f"{origem_code}{destino_code}"

            if par in data:
                taxa = float(data[par]["bid"])
                resultado = float(valor) * taxa

                dispatcher.utter_message(
                    text=f"Cotação atual:\n"
                         f"1 {origem_code} = {taxa:.2f} {destino_code}\n\n"
                         f"{float(valor):.2f} {origem_code} = {resultado:.2f} {destino_code}"
                )
            else:
                dispatcher.utter_message(
                    text=f"Não encontrei a conversão de {origem_code} para {destino_code}."
                )

        except Exception as e:
            dispatcher.utter_message(text="Erro ao consultar a AwesomeAPI.")
            print(f"Erro técnico: {e}")

        return []