# Bot_Contadores_Impressora

O Bot_Contadores_Impressoras desenvolvido em python tem como objetivo automatizar o processo de coleta e organização de dados das impressoras locadas da prefeitura municipal de Imbé, assim sendo somando os contadores com numero de copias e impressões e em caso de impressoras coloridas faz a soma separando os contadores por cores ao final do processo realiza um Screenshot da tela com os contadores originais da pagina web da impressora

## Requisitos

* Biblioteca PlayWright
* Acesso as impressoras em uma rede própria

## Passo a passo

* Preencher as informações sobre a impressora no arquivo "Impressoras.json" dentro da pasta Json.

      {
      "impressoras" : {
          "impressora_1" : {
              "item" : "Item de empenho ou id da impressora",
              "link" : "Link de acesso para a pagina web da impressora",
              "modelo" : "modelo da impressora",
              "xpath" : "xpath do contador",
              "caminho" : "o caminho para onde vai a copia do screenshot com o contador"
          }
      }

## Modelos de impressora suportado

* Ricoh SP3510
* Ricoh SP3710
* Ricoh M320f
* Ricoh M310
* Ricoh SP377
* Ricoh SP5200
* Ricoh MP C2003
* Ricoh MP C2503
* Samsung M4070
* Samsung M5360
* HP Laser MFP 432
