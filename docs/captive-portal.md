# Provisionamento via Captive Portal

Um *captive portal* é um mecanismo amplamente utilizado para provisionamento de rede, no qual o dispositivo cliente é redirecionado automaticamente para uma página web antes de obter acesso completo à internet. Esse modelo é comum em redes corporativas, hotéis, aeroportos e também em dispositivos IoT durante o processo inicial de configuração.

O funcionamento baseia-se na detecção automática de conectividade realizada pelo sistema operacional do cliente. Cada sistema operacional executa requisições HTTP específicas para URLs conhecidas a fim de validar se há acesso pleno à internet. Caso a resposta recebida não seja a esperada (por exemplo, um código HTTP 204 ou um conteúdo específico), o sistema interpreta que está em uma rede com *captive portal* e abre automaticamente um navegador embutido.

Exemplos de verificações de conectividade:

- **Android** → `http://connectivitycheck.gstatic.com/generate_204`
- **Windows** → `http://www.msftconnecttest.com/connecttest.txt`
- **macOS / iOS** → `http://captive.apple.com`
- **Linux (NetworkManager)** → `http://nmcheck.gnome.org/check_network_status.txt`

Como cada sistema valida conectividade utilizando endpoints distintos, a solução precisa interceptar qualquer requisição HTTP e redirecionar o cliente corretamente.

---

## Arquitetura da Solução no Raspberry Pi

A solução implementada no Raspberry Pi Zero 2 W utiliza uma arquitetura de *AP + Captive Portal* para permitir o provisionamento da rede Wi-Fi.

### Criação da Interface Virtual `ap0`

A interface física principal é a `wlan0`. A partir dela, é criada uma interface virtual chamada `ap0`. Isso permite que o dispositivo opere simultaneamente como:

- **STA (Station)** → Conectado a uma rede Wi-Fi existente.
- **AP (Access Point)** → Oferecendo uma rede própria para provisionamento.

Essa abordagem é especialmente importante em cenários onde o dispositivo precisa manter conectividade enquanto ainda permite reconfiguração.

### Inicialização do Access Point com `hostapd`

Para transformar a interface `ap0` em um ponto de acesso funcional, foi utilizado o `hostapd`.

O `hostapd` é responsável por:

- Configurar o SSID da rede
- Definir parâmetros de segurança (WPA2, senha, etc.)
- Gerenciar beacon frames e autenticação

Com isso, o Raspberry passa a anunciar uma rede Wi-Fi própria à qual o usuário pode se conectar para realizar o provisionamento.

### Configuração de DHCP e DNS

Após a criação da rede Wi-Fi, é necessário fornecer DHCP e DNS.

O DHCP é responsável por:

- Atribuir endereço IP ao cliente
- Definir gateway padrão
- Informar qual servidor DNS deve ser utilizado

Sem DHCP, o cliente não teria parâmetros de rede válidos para comunicação.

Já o DNS resolve nomes de domínio para endereços IP. No contexto de *captive portal*, o DNS tem um papel estratégico: ele pode ser utilizado para redirecionar qualquer domínio solicitado pelo cliente para o IP do Access Point.

A solução utiliza o `dnsmasq`, que atua simultaneamente como:

- Servidor DHCP
- Servidor DNS

A configuração adotada implementa **DNS hijacking**, ou seja:

```

address=/#/<IP_DO_AP>

````

Essa diretiva força todas as requisições DNS a retornarem o endereço IP do Access Point (`ap0`). Dessa forma, independentemente da URL que o sistema operacional tente acessar para verificar conectividade, a requisição será direcionada ao Raspberry Pi.

### Servidor Flask e Redirecionamento HTTP

No IP associado à interface `ap0`, está sendo executado um servidor HTTP implementado em Flask, escutando na porta 80.

Fluxo de funcionamento:

1. O cliente conecta à rede Wi-Fi do Raspberry.
2. O DHCP fornece IP, gateway e DNS.
3. O sistema operacional realiza sua verificação de conectividade.
4. O DNS retorna sempre o IP do AP.
5. A requisição HTTP chega ao servidor Flask.
6. O servidor responde com **HTTP 302 (Found)** redirecionando para o endereço do captive portal.

Com isso, independentemente da URL originalmente solicitada pelo sistema operacional, o cliente é redirecionado para a página de provisionamento.

---

## Considerações Técnicas

Essa abordagem é robusta porque:

* Independe da URL específica usada pelo sistema operacional
* Funciona com Android, Windows, macOS e Linux
* Não depende de acesso externo à internet
* Permite provisionamento totalmente offline

Essa arquitetura é especialmente adequada para imagens customizadas baseadas em Buildroot, onde todos os serviços podem ser inicializados automaticamente no boot, garantindo experiência determinística e tempo de inicialização reduzido.