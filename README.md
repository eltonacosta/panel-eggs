# Panel Eggs

Repositório centralizado de eggs para **FeatherPanel** e **Pterodactyl**.

O objetivo é manter os eggs em um único local controlado, versionado e auditável, reduzindo a dependência de arquivos espalhados por fontes não verificadas. A proposta não é substituir uma auditoria de segurança, mas dar uma base rastreável: cada egg tem origem, histórico e hash.

## Conteúdo

- `programming/java/` — eggs genéricos para aplicações Java (JAR), versões 17 a 27.

## Segurança e integridade

- Curadoria e revisão manual antes de cada commit.
- Estrutura versionada; alterações ficam registradas no histórico Git.
- `SHA256SUMS` com o hash de cada egg, para verificação antes da importação.
- Scripts de instalação revisados; sem downloads remotos opacos ou código ofuscado.
- Imagens Docker públicas e declaradas explicitamente no egg.
- Contribuições passam por revisão; qualquer alteração em um egg exige atualização do hash.
- Checksums ajudam a detectar alterações indevidas, mas não autenticam sozinhos o autor. Para garantia mais forte, use commits assinados/tags e revise o histórico.

Detalhes do modelo de segurança e das limitações: [SECURITY.md](./SECURITY.md).

## Verificar a integridade

```bash
./scripts/verify.sh
```

Ou manualmente:

```bash
sha256sum -c SHA256SUMS
```

## Importar

**FeatherPanel**

1. **Admin → Templates → Realms (Nests)** → crie o Realm desejado.
2. **Admin → Templates → Spells (Eggs)** → **Import** → selecione o JSON e o Realm.
3. Revise variáveis e script de instalação antes de salvar.

**Pterodactyl**

1. **Admin → Nests** → crie o Nest desejado.
2. **Admin → Nests → Import Egg** → selecione o JSON.

Antes de importar, verifique o hash e leia o script de instalação e as variáveis. O passo a passo detalhado está em [`programming/java/README.md`](./programming/java/README.md).

## Contribuir

- Abra um PR com o JSON, a origem/licença e o hash atualizado.
- Não envie scripts obfuscados, downloads de URLs não declaradas ou comandos destrutivos.
- Prefira imagens oficiais e versões explícitas.
- Descreva a finalidade do egg e o que ele executa.

## Licença

MIT. Veja [LICENSE](./LICENSE) e [NOTICE.md](./NOTICE.md).
