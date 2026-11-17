# Aviso de origem

Este repositório contém obras derivadas do egg **Generic Java** do projeto
[`parkervcp/eggs`](https://github.com/parkervcp/eggs).

## Upstream

- Repositório: <https://github.com/parkervcp/eggs>
- Arquivo: `generic/java/egg-java.json`
- Licença: MIT
- Copyright (c) 2018 Michael Parker `<parker@parkervcp.com>` e contribuidores
- Autor original do egg: `sneaky@sneakyhub.com`

## Modificações deste repositório

- Geração de uma variante por versão do Java: 17, 19, 21, 22, 25, 26 e 27.
- `docker_images` restrito à imagem `ghcr.io/parkervcp/yolks:java_<versão>`.
- Nome, descrição, autor e metadados ajustados para identificar a versão.
- Variável `JARFILE` com padrão `server.jar` e limite maior de caracteres.
- Script de instalação mínimo, sem download automático: o JAR é enviado pelo
  gerenciador de arquivos do painel.

Consulte o [LICENSE](./LICENSE) para os termos completos.
