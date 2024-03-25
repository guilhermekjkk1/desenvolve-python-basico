from datetime import datetime

def exibir_data_hora_formatada():
    # Obter a data e hora atuais
    agora = datetime.now()
    
    # Formatar a data
    data_formatada = agora.strftime("%d/%m/%Y")
    
    # Formatar a hora
    hora_formatada = agora.strftime("%H:%M")
    
    # Exibir a data e hora formatadas
    print("Data:", data_formatada)
    print("Hora:", hora_formatada)

if __name__ == "__main__":
    exibir_data_hora_formatada()
