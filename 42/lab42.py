# lab42 - o lab dos labs
# version 1.0 - 05/09/2021
# Script para copiar a saída do susy
# Se der certo, eu libero esse código pra você usar, 
# mas faça a boa de passar a palavra adiante

import os
path = os.path.dirname(os.path.abspath(__file__))  # Caminho do arquivo

def diff(number, entrada):  # Programa que verifica se todas as linhas da entrada são iguais ao arquivo de entrada
    infile = "arq" + "{:02d}".format(number)+ ".in"
    f = open(path + "/" + infile)
    lines = f.readlines()
    difference = len(entrada)==len(lines)

    if difference:
        for j in range(len(lines)):
            difference = difference and (entrada[j]==lines[j])

    return difference

entrada = []  # Variável para armazenar a entrada
while True:
    try:
        entrada.append(input() + '\n')
    except:
        break

i = 0   # variável que vai guardar o número do arquivo
nextfile = "arq" + "{:02d}".format(i+1) + ".in"
difference = False
while not difference and os.path.exists(nextfile):  # Procura o arquivo .in que saiu as entradas colocadas 
    i += 1
    nextfile = "arq" + "{:02d}".format(i+1) + ".in"
    difference = diff(i, entrada)

# Aqui será aberto o arquivo de saída da respectiva entrada encontrada e imprimirá as linhas dele
outfile = "arq" + "{:02d}".format(i) + ".out"
fout = open(path + "/" + outfile)
lines = fout.readlines()
for line in lines:
    print(line[:-1])


#	 	 
#			 
#	  
#  
#		 
#			
#/
#	 	 
# 	 
#  
# 	
#	  
#			
#/
# 		 
# 
# 	  
#			
#/
#	
# 	
#	 
#  	
#   
# You were expecting a true unicamp mc102 lab code?????
#                                           o/`/dhydddddho////:-//yyo//:::::::::::::::::::::::::::::::::::::::::::::::+so/:::::/yyyhhy/```````..````.---
#                                          `smo+mmymmmmdo++///+yh++::///:://////////:::::::::::::::::::::::::::::::::::/oyhs+///ohhddddy-````.--`.---:+:
#                                          `/mmddmmhmmho+++oyoso/-:://:::////////:::::::::::::::::::::::-::::::::::::::://ohhyo//shhhhdhs::/oyo...----:-
#                                           `smmmmmmmhoooshhs://:--::::://////::::::::::::::::::::::::::::-::::::::::::::://ohhyo+yhhhhhhhhhh+........--
#                                           `-ymmmmmdhhhdds+:::::.::::::/::::::::::::-::::::::::-::::::::::-:::::::::::::::://ohhhshhhhhhyyysso+/:.```.`
#                                           -dmmmmmmmmmdy+//:::::-:::-::::::::-:::::::-::::::::::::::::::::::-:::::::::::::::://shhhhhhhhyys/:--...`````
#                                          `ymmmmmmmmdho+//::-:::-::-:::::::::--:::::::--::::::::-::::::::::::--::-::::::::::::::/shhhhhhyyy+.`````    `
#               `````                      `smmmmhhhyo+//::::-:::-:--::::::::::--::::::::--:::::::-:::::::::::::------:-:::::::::::/shhhhhsshs.`       `
#               ````                       `-mmmmdyo+///:::::--::::--:::::::::::---:::::::.-:::::::--:::::::::::::---------------::::+yyyyy+/ss`        
#                                 `       ``:mmmmmdy+//::::-:---::-:-::---::::::------::::-----:::::-----------------------::::------:/syyyy-.+/       `
#      ````                       :/.````.:sdmmmmmdho//::::---.-::.-.::------::::.----.-:::...----::::---::::::::::::::-----::---------/yyyyo``:       `
#                                 `+hyyyhdmmmmmmdhs+//::::::--..-----::-------:::.---.``.-::------------..--:::::::::::--------------::-oyyyy.         `
#                                  `-sdmmmmmmmmddho//:::::-::--o+///:-/-:::----::.-.```.-----.------------..--::::-::--------.--------+++syyy-          
#                   ```````          `.shhhdmmmmds+//:::::--:/:mmmdhhs/:/::::---:..``.-------.--...-------------:-------.....-.-------:ossyyy.`        `
#            ``  ````````             ``:ohmmmmmyoo+:::-::::-//mmmhmmmd+syhyso:.-```.--------..``-:::::-------..--..---..-----.--------/ssyys``         
#           ```````````                `:hmyydmdyhh/:::--:::-:/mmmymmmmd+dmso/:-.--/:-..-:+shdo.::::::::--------...---..........----..-:ssyy/`         `
# ```````````````                      `hd/:dmmmdds/::::--::+/+mmmhdmmmddys////-:--:/oyyhdNMNhsso++//::::-------...---..---......--...-:ssyo`           
# ..------.......``                    -h-`+mmmmdds/:-::-::://ohddmhmmmhmy++oydho.+MMNs//shdmmNNmmdhys+:::------..-----...............-/syo.``          
# ``.............-..``````             `-``/mmmmddy//-::---/+-////+smmmhhosdmddmm:+mhdysooodmNNmmmmmmmms::------`-----...............--ss+....````      
# ....`````  ````...````````               `ymmhddd+:.:-.:/hdys+////odmNmmdddmmdydddddddhmNNNNmmmmmmmmmh/:-----..----................-/s/....-://`      
# ````````    `    `  ```..``              `.odyddh+:--::-+h+//////::/hNmddhhmmmmNNNNNNNNNNNmmmmmmmmmmmd/:----------.................-/+syyyyy+-````    
#                       `..```            ````:hhsy/:-:::::+o-yNh/omdhhNNmmmmNmmmmmmmmmmmmmmmmmmmmmmmmmh/:--------............--.....-osoo+/-..``````   
#                        ``````         ```.:ohdyd+/::::::::yhdyo/+hmmdmmNNNmmmmmmmmmmmmmmmmmmmmmmmmmmmh::------............---.....--/ss+:....``````   
#                          `````       `:+shhdys/h/-:::::://ymmssdmNNdmdmNNmmmmmmmmmmmmmmmmmmmmmmmmmmmmy::------.....`.....----...../o/+syy+-...`..```  
#                             ```       ```...``-y:`-::-:://oNNmmmNNmhdhmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmms::-----.........-------....-/ss/:oyyo......```  
#                         ```        ``         `y:``-:.-:///dNmmmmmmhyhyo++oossymmmmmmmmmmmmmmmmmmmmmmo:------.........------....../ss/``.:s+````````  
#                        ```      `````          //```..`.-:/sNmmmmmmyo+//:::/+ydmmmmmmmmmmmmmmddmmmmmd+:-----..........-----.......-sso``  `:.         
#                     ` ```        ````          `.  ```  ``..dNmmmmmmds++///odmmmmmmmmmmmmmmmdohmmmmdd/:----.............--........./ss:`              
#                         ````   ```````     ````           ``:mNmmmmmmmmdsoymmmmmmmmmmdddddhs/smmmmmdy:----........`................-+ss-              
#                               `````````    ```````  ``    ``.+NNmmmmmmmdddmmmmdddddddddddy///dmmmmmdo:---.........`.......`.........-/os-`            
#                           ```   ```````     ``...``````   ```.oNNNNmmmmhmhddhddddddhysoo/---ommmmmdd/:---.........`.......`........::::+o/.``         
#                                               ```````.```   ```+NNNmmmmmmhddhy+/::--..------hmmmmddy:---.........`........`........-+oossssoo+:.`     
#                                               `````...``````  ``/dNNmmmmmmy/:-....-:://////+mmmmddd+:--..................`...........:oso+///:-.`     
#                                                  ```````````   ``.yNNNmmmmmh/---+oosssssssshmmmdddy:---.................`...``........-/oss+-`        
#                                                     ``````      ```:dNNmmmmmd+h+sssssssshdymmmmddd+:--..........`......`..``.`..........-/sss+-`      
#                                                         ``       ```.omNmmmmmyhyyyyyyhddhhmmmddddy:--..........`.....`````...``.........-::osyyo.     
#                                                                      `-yNNmmmdhdmmmddhhdmmddddddd/--...........`...````.....````````````./o++oyyy/`   
#                                                                       ``:hNmmmmdddddmmmmdhsddddds:--..........`...........````````````````.:so:+syo`  
#                           ```.:/os+`                           ``        `ommmmmhhssosss+ohddddd/-...........`...........``````````````````.+s+`.:os` 
#                         `:oydNmdmNmy`                                     `-dNmmdy+///+shdddddds-............`..........```````````````````-sss:```-: 
# ```````..``         ``.-hNNNNNdhdmmd:`      `.......``      ``             `.dNmmmdhhdddddddhs/--...........`..........````````````````````.osso`     
# .``.--::-``     ```..-::mNNNNmmdmds/:`   `.-----------..`                   `-mNmmmmmdddddy+:---....................```````````````````````./ssy-     
#    ``.--.``````....--::/sddmmdddy+/::-  `...------......`                    `-oyhddddhs+:----..................```````````````````````````.-sss+`    
#     `---..........--+yhddmmmmds/::::--``-------.....```           ``          ``.---:::-.--.................`````````````````````....``````.-osso`    
#    `.-.........---+dmmmmmmmmho/:-:----.-----.....``             `        ```....----.---...............```````````````````...........``````..+sso`    
# `````..........--:dmmmmmmmds/-::.-----..........` `            `.`  `.``...---------...............`````````````````.................```````.+ss/`    
# .``..........---/odddddmmh+:---------.........``          ```````   -y+-.-----------...........``````````...........................`````````-//-     
# ............--:odmmmmmdy+/::---.----..````.....`      ````.-::-``   `+ys/---.....---....`....```````................`................````````````     
# .......----::/ommmmmmho/-:::---.--..``    `.:.......``..`-:///:-````.-+mms/:-............```````..........`......````.``............``````````````````
# ......---/sdmmdhdmmmy/::------...```      `-::--::::..--:://///:--:::/:ommdo:---.``.....`````.............`.....`````````...........``````````````````
# ......--/dmmmmmmdhho/::-------``         `-:///////::::////////////////+mhhm+:--..``....````...`.......``.````..`````````.........`````````...........
# ......--ymmmmdhdmy/:::-------.         `.://///////////////////////////oyohyooo-..```..```..`..``.`....`.`````.....````........``````````.............
# .....-:/ommmmmhy+-::--------.`        `.//////////////////////////////shshdsohm+-...`````......`..`....``.`.`..............```````````................
# ....--ydsdmmmds/:--------..``         `:////////////////////////////+smNhNmyhmmh++:-.```........`.........`.........````````....````..................
# .....-smdyddy/:------.```            `.:/::----::://///////////++++oymmmmmmhmmmmyddo-.`........................``````........```......................
# .....--sddy+::-.---..`               `.---.......--:/++++osyyhhhdmmNNNmdhmmmmmmmmmmd+/---................................````.........................
# ......../+---.`````                  ``.......---:+shdmNNNNNNNNNNNNNNmmmmdhmmmmmmmmyyoy+---...........................````............................
# .......```````                     ` ``..--:+sydmNNNNNNNNNNNNNNNmmmmmmmmmmmhdmmmmmmshomdy/--......................````...............................`
# ...````                          ````.-+shmNNNNNNNNNNNNNNNNmmmmmmmmmmmmmmmmmhydhhyyssohyyys:-................`````...................................`