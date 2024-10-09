
def inverter_string(s):
    string_invertida = ""

    for i in range(len(s) - 1, -1, -1):
        string_invertida += s[i]  
    
    return string_invertida

entrada = input("Informe uma string para inverter (ou pressione Enter para usar a string padrão): ")

if entrada == "":
    entrada = "Exemplo de string"

resultado = inverter_string(entrada)

print("String invertida:", resultado)
