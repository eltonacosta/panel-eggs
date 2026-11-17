# Java 19 — Generic JAR

- **Egg:** `egg-java-19.json`
- **Docker:** `ghcr.io/parkervcp/yolks:java_19`
- **Canal:** non-LTS
- **Startup:** `java -Dterminal.jline=false -Dterminal.ansi=true -jar {{JARFILE}}`
- **Variável:** `JARFILE` (padrão `server.jar`)

## Como usar

1. Importe este JSON como **Spell/Egg** no painel.
2. Crie um servidor usando esse Spell/Egg.
3. Envie o arquivo `.jar` para a raiz do servidor pelo gerenciador de arquivos.
4. Ajuste a variável `JARFILE` para o nome exato do arquivo.
5. Inicie o servidor.

Se o servidor ficar preso em `Starting`, ajuste a **detecção de startup** do Spell para uma linha que sua aplicação imprime quando estiver pronta.
