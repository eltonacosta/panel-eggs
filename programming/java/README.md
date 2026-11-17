# Java 17+ — Eggs genéricos

Eggs para rodar aplicações **Java (JAR)** no módulo de servidores (FeatherWings no FeatherPanel / Wings no Pterodactyl). Cada versão usa a imagem Docker correspondente do `ghcr.io/parkervcp/yolks`.

| Versão | Canal | Imagem Docker | Pasta |
|---|---|---|---|
| 17 | LTS | `ghcr.io/parkervcp/yolks:java_17` | [`17/`](./17/) |
| 19 | non-LTS | `ghcr.io/parkervcp/yolks:java_19` | [`19/`](./19/) |
| 21 | LTS | `ghcr.io/parkervcp/yolks:java_21` | [`21/`](./21/) |
| 22 | non-LTS | `ghcr.io/parkervcp/yolks:java_22` | [`22/`](./22/) |
| 25 | LTS | `ghcr.io/parkervcp/yolks:java_25` | [`25/`](./25/) |
| 26 | non-LTS | `ghcr.io/parkervcp/yolks:java_26` | [`26/`](./26/) |
| 27 | latest (non-LTS) | `ghcr.io/parkervcp/yolks:java_27` | [`27/`](./27/) |

As versões **18, 20, 23 e 24** não estão incluídas porque não existe tag `java_*` correspondente no `ghcr.io/parkervcp/yolks`.

## Escolha da versão

- **17, 21 e 25** são LTS; recomendadas para produção.
- **19, 22 e 26** são non-LTS/históricas.
- **27** é a mais recente disponível no registry no momento.

## O que o egg faz

- Executa `java -Dterminal.jline=false -Dterminal.ansi=true -jar {{JARFILE}}`.
- Não baixa nada na instalação: o JAR é enviado pelo gerenciador de arquivos.
- A variável `JARFILE` aponta para o nome do arquivo JAR.
- A detecção de startup padrão procura por `Done`, `Started`, `Listening on` ou `Server started`; ajuste conforme sua aplicação.

## Importar no FeatherPanel

1. Entre como administrador.
2. Vá em **Admin → Templates → Realms (Nests)** e crie um Realm, por exemplo `Programming`.
3. Vá em **Admin → Templates → Spells (Eggs)** e use **Import**.
4. Selecione o JSON da versão desejada, por exemplo `21/egg-java-21.json`, e escolha o Realm criado.
5. Revise as variáveis e o script de instalação; salve.
6. Para criar o servidor: **Admin → Servers → Create Server**, escolha o Realm/Spell, o nó de jogo e os recursos.
7. Abra o servidor → **Files** → envie o `.jar` para a raiz do servidor.
8. Em **Startup**, ajuste `JARFILE` para o nome do arquivo e inicie.

## Importar no Pterodactyl

1. **Admin → Nests → Create Nest** (ex.: `Programming`).
2. **Admin → Nests → Import Egg**.
3. Selecione o JSON e o Nest criado.
4. Crie o servidor usando o egg, envie o JAR pelo File Manager, ajuste `JARFILE` e inicie.

## Se o servidor ficar em “Starting”

O egg genérico não conhece o texto que a sua aplicação imprime quando termina de iniciar. Edite a detecção de startup do Spell (`config.startup.done`) para uma linha real do log, por exemplo:

```json
{
  "done": "Started"
}
```

## Verificação de integridade

Antes de importar, confira o hash do egg a partir da raiz do repositório:

```bash
./scripts/verify.sh
```

O arquivo `SHA256SUMS` contém o hash de cada JSON. Se um egg for alterado sem atualização do hash, a verificação falha.

## Observações

- Estes eggs são para o módulo de **servidores** (FeatherWings/Wings).
- No nó web do FeatherPanel (FeatherQuilld), o equivalente é um **WebPlate**, não um egg.
- As imagens de runtime são públicas, mas o nó precisa conseguir acessar o `ghcr.io` para baixá-las.

## Origem e licença

Baseado no egg **Generic Java** do repositório [`parkervcp/eggs`](https://github.com/parkervcp/eggs), licença MIT.

- Arquivo original: `generic/java/egg-java.json`
- Autor original do egg: `sneaky@sneakyhub.com`
- Copyright (c) 2018 Michael Parker e contribuidores

As modificações deste repositório criam uma variante por versão do Java, restringem a imagem Docker à versão correspondente, ajustam nome/descrição/variável `JARFILE` e simplificam o script de instalação.

Veja [LICENSE](../../LICENSE) e [NOTICE.md](../../NOTICE.md).
