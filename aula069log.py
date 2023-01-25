#Registro da Execução do Programa
#erros, etapas cumpridas, avisos
#Por que(informação, depuração , registro de #atividades para fins  de Auditoria)
#Onde(tela, arquivo, Banco de Dados)
#Voce pode implementar mas o python ja oferece
#permite salvar em disco,formatar saida,
# Os logs de python fucionam com levels:
#Debug, info,warning, error, critical

def custom_logger(level, message):#funçao com 2 parametros
  import logging  # func de forma hierarquica
  logger = logging.getLogger(__name__)#objeto que vai receber do logging
  if not (len(logger.handlers)): #verificar se handlers ja existe
    logging.basicConfig(level=logging.INFO) #chamar basicConfig
    c_handler = logging.StreamHandler() #criando handlers
    f_handler = logging.FileHandler('file.log') #criando handlers
    format = logging.Formatter('%(asctime)s - %(name)s- %(levelname)s - %(message) s') #formatação 
    c_handler.setFormatter(format)#atribuindo
    f_handler.setFormatter(format)#atribuindo
    logger.addHandler(c_handler)#adicionar handler ao logger
    logger.addHandler(f_handler)#adicionar handler ao logger

  if level == 'debug':
    logger.debug(message)
  elif level == 'info':
    logger.info(message)
  elif level == 'warning':
    logger.warning(message)
  elif level == 'error':
    logger.error(message)
  else:
    logger.critical(message)

custom_logger('error','Parametro errado!')




custom_logger('info','inicio do programa')

lista = [1,2,3]
try:
  print(lista[10])
except:
  custom_logger('error','Indice incorreto!')

custom_logger('info','fim do programa')