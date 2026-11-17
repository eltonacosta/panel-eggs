# Java 17+ — Eggs genéricos

Esta pasta contém eggs genéricos para rodar aplicações **Java (JAR)** no módulo de servidores (FeatherWings/Pterodactyl). Cada versão usa a imagem Docker correspondente do `ghcr.io/parkervcp/yolks`.

| Versão | Canal | Imagem Docker | Pasta |
|---|---|---|---|
| 17 | LTS | `ghcr.io/parkervcp/yolks:java_17` | [`17/`](./17/) |
| 19 | non-LTS | `ghcr.io/parkervcp/yolks:java_19` | [`19/`](./19/) |
| 21 | LTS | `ghcr.io/parkervcp/yolks:java_21` | [`21/`](./21/) |
| 22 | non-LTS | `ghcr.io/parkervcp/yolks:java_22` | [`22/`](./22/) |
| 25 | LTS | `ghcr.io/parkervcp/yolks:java_25` | [`25/`](./25/) |
| 26 | non-LTS | `ghcr.io/parkervcp/yolks:java_26` | [`26/`](./26/) |
| 27 | latest (non-LTS) | `ghcr.io/parkervcp/yolks:java_27` | [`27/`](./27/) |

## Escolha da versão

- **17, 21 e 25** são LTS; recomendadas para produção.
- **19, 22 e 26** são non-LTS/históricas.
- **27** é a mais recente disponível no registry no momento.
- **18, 20, 23 e 24** não estão incluídas porque não existe tag `java_*` correspondente no `ghcr.io/parkervcp/yolks`.

## O que o egg faz

- Executa `java -Dterminal.jline=false -Dterminal.ansi=true -jar {{JARFILE}}`.
- Não baixa nada na instalação: o JAR é enviado pelo gerenciador de arquivos.
- A variável `JARFILE` aponta para o nome do arquivo JAR.
- A detecção de startup padrão procura por `Done`, `Started`, `Listening on` ou `Server started`; ajuste conforme sua aplicação.

## Importação

Veja o [README principal](../../../README.md) para o passo a passo no FeatherPanel e no Pterodactyl.

> Estes eggs são para o módulo de **servidores de jogo** (FeatherWings). No nó web (FeatherQuilld), o equivalente é um **WebPlate**, não um egg.
