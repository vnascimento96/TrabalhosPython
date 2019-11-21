def jurosCompostos (investimento, taxa, numeses):
    jurosCompostos = investimento * (1 + taxa )** numeses
    return jurosCompostos

def porc(jurosCompostos, investimento):
    porc = jurosCompostos - investimento
    return porc
    
        
      
