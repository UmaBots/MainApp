#### Este arquivo contém testes para avaliar se o seu bot se comporta conforme o esperado.
#### Se você quiser saber mais, consulte os documentos: https://rasa.com/docs/rasa/user-guide/testing-your-assistant/

## caminho feliz 1
* saudar: olá!
  - utter_greet
* mood_great: incrível
  - utter_happy

## caminho feliz 2
* saudar: olá!
  - utter_greet
* mood_great: incrível
  - utter_happy
* adeus: adeus!
  - utter_goodbye

## caminho triste 1
* saudar: olá
  - utter_greet
* mood_unhappy: não é bom
  - utter_cheer_up
  - utter_did_that_help
* afirmar: sim
  - utter_happy

## caminho triste 2
* saudar: olá
  - utter_greet
* mood_unhappy: não é bom
  - utter_cheer_up
  - utter_did_that_help
* negar: não realmente
  - utter_goodbye

## caminho triste 3
* saudar: oi
  - utter_greet
* mood_unhappy: muito terrível
  - utter_cheer_up
  - utter_did_that_help
* negar: não
  - utter_goodbye

## diga adeus
* adeus: adeus!
  - utter_goodbye

## bot challenge
* bot_challenge: você é um bot?
  - utter_iamabot
