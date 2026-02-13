# NarrAI Provisionador

## Objetivo

O **NarrAI Provisionador** tem como objetivo fornecer um sistema *full stack* desenvolvido em **Python** utilizando **Flask**, projetado para ser executado em um ambiente de *captive portal* no Raspberry Pi.

A aplicação é responsável por permitir que o usuário realize o provisionamento inicial do dispositivo através de uma interface web acessível ao conectar-se à rede Wi-Fi do equipamento. Por meio dessa interface, o usuário pode:

- Configurar a rede Wi-Fi à qual o dispositivo deverá se conectar (modo STA)
- Selecionar e configurar um dispositivo Bluetooth para conexão de aúdio recebendo as descrições de áudio

A solução foi concebida para funcionar de forma embarcada, integrando-se à infraestrutura de Access Point, DHCP e DNS previamente configurada no sistema operacional do dispositivo. Para saber mais sobre a infraestrutura implementada acesse:

[Provisionamento via Captive Portal](./docs/captive-portal.md)

## Autores

- Gustavo Camargo Domingues
- Leticia Zanellatto de Oliveira
- Lyncon Baez
- Thaynara Nascimento de Jesus 
