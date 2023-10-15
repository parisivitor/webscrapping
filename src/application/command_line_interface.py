import time
import sys
from domain.aerodromo.factory.aerodromo_factory import AerodromoFactory

def initialize_system():
     icao =  input('Digite o ICAO do aeródromo que deja pesquisar ou "sair" para sair: ').upper()
     if len(icao) != 4:
          print(f"Aeródromo é um acronimo de 4 letras\n  O digitado('{icao}') contaim {len(icao)} letras")
          return initialize_system()
     if icao == 'SAIR':
          print('Saindo!')
          time.sleep(2)
          sys.exit()
     return icao


def main():
     icao = initialize_system()
     start_time = time.time()
     aerodromo = AerodromoFactory.create_aerodromo(icao)
     if aerodromo is False:
          print('Não encontramos nenhuma informação referente ao ICAO digitado')
          main()
     else:
          print(aerodromo)

          end_time = time.time()
          total_time = end_time - start_time
          print(f"Tempo total de execução: {total_time} segundos")


if __name__ == "__main__":
     main()
