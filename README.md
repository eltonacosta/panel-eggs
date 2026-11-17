# Panel Eggs — Java 17+

Eggs genéricos de **Java (JAR)** para **FeatherPanel** e **Pterodactyl**, separados por versão do JDK.

> Estes eggs são para o módulo de **servidores** (FeatherWings no FeatherPanel / Wings no Pterodactyl).
> No **nó web** do FeatherPanel (FeatherQuilld), o equivalente é um **WebPlate**, não um egg.

## Estrutura

```text
programming/
└── java/
    ├── 17/
    │   ├── egg-java-17.json
    │   └── README.md
    ├── 19/
    ├── 21/
    ├── 22/
    ├── 25/
    ├── 26/
    ├── 27/
    └── README.md
```

## Versões incluídas

| Versão | Canal | Imagem Docker | Pasta |
|---|---|---|---|
| 17 | LTS | `ghcr.io/parkervcp/yolks:java_17` | [`programming/java/17`](./programming/java/17/) |
| 19 | non-LTS | `ghcr.io/parkervcp/yolks:java_19` | [`programming/java/19`](./programming/java/19/) |
| 21 | LTS | `ghcr.io/parkervcp/yolks:java_21` | [`programming/java/21`](./programming/java/21/) |
| 22 | non-LTS | `ghcr.io/parkervcp/yolks:java_22` | [`programming/java/22`](./programming/java/22/) |
| 25 | LTS | `ghcr.io/parkervcp/yolks:java_25` | [`programming/java/25`](./programming/java/25/) |
| 26 | non-LTS | `ghcr.io/parkervcp/yolks:java_26` | [`programming/java/26`](./programming/java/26/) |
| 27 | latest (non-LTS) | `ghcr.io/parkervcp/yolks:java_27` | [`programming/java/27`](./programming/java/27/) |

As versões **18, 20, 23 e 24** não estão incluídas porque não existe tag `java_*` correspondente no `ghcr.io/parkervcp/yolks`.

## Como importar no FeatherPanel

1. Entre no painel como administrador.
2. Vá em **Admin → Templates → Realms (Nests)** e crie um Realm, por exemplo `Programming`.
3. Vá em **Admin → Templates → Spells (Eggs)** e use **Import** (importar egg/spell).
4. Selecione o JSON da versão desejada, por exemplo `programming/java/21/egg-java-21.json`, e escolha o Realm `Programming`.
5. Revise as variáveis e salve o Spell.
6. Para criar um servidor: **Admin → Servers → Create Server**, escolha o Realm/Spell, o nó de jogo (no seu caso, **NODE 01**) e os recursos.
7. Abra o servidor → **Files** → envie o arquivo `.jar` para a raiz do servidor.
8. Abra **Startup**, ajuste `JARFILE` para o nome do arquivo (ex.: `app.jar`) e inicie.

### Se o servidor ficar em “Starting”

O egg genérico não conhece o texto que a sua aplicação imprime quando termina de iniciar. Edite a **detecção de startup** do Spell (`config.startup.done`) para uma linha real do log, por exemplo:

```json
{
  "done": "Started"
}
```

O padrão incluído procura por `Done`, `Started`, `Listening on` ou `Server started`.

## Como importar no Pterodactyl

1. **Admin → Nests → Create Nest** (ex.: `Programming`).
2. **Admin → Nests → Import Egg**.
3. Selecione o JSON da versão desejada e o Nest criado.
4. Crie o servidor usando o egg, envie o JAR pelo File Manager, ajuste `JARFILE` e inicie.

## Detalhes do egg

- Startup: `java -Dterminal.jline=false -Dterminal.ansi=true -jar {{JARFILE}}`
- Variável: `JARFILE` (padrão `server.jar`)
- Instalação: não baixa nada; o JAR é enviado pelo gerenciador de arquivos.
- Imagem de instalação: `ghcr.io/parkervcp/yolks:debian`
- As imagens de runtime são públicas, mas o nó precisa conseguir acessar o `ghcr.io` para baixá-las.

## Origem e licença

Baseado no egg **Generic Java** do repositório [`parkervcp/eggs`](https://github.com/parkervcp/eggs), licença MIT.

- Arquivo original: `generic/java/egg-java.json`
- Autor original do egg: `sneaky@sneakyhub.com`
- Copyright (c) 2018 Michael Parker e contribuidores

As modificações deste repositório criam uma variante por versão do Java, restringem a imagem Docker à versão correspondente, ajustam nome/descrição/variável `JARFILE` e simplificam o script de instalação.

Veja [LICENSE](./LICENSE) e [NOTICE.md](./NOTICE.md).
