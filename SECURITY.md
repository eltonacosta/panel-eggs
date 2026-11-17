# Segurança

Este repositório reúne eggs para FeatherPanel/Pterodactyl com o objetivo de reduzir a exposição a arquivos adulterados ou de origem desconhecida. As medidas abaixo diminuem o risco; elas não substituem auditoria, revisão de código e boas práticas no painel.

## Modelo de ameaça

- Egg JSON alterado para executar comandos, baixar conteúdo remoto ou expor dados.
- Script de instalação com download opaco, ofuscação ou comando destrutivo.
- Alteração silenciosa de um egg já publicado.
- Importação de egg de fonte não confiável diretamente no painel.

## Controles

- Estrutura versionada e histórico Git de todas as mudanças.
- Revisão manual antes de aceitar um egg ou alteração.
- `SHA256SUMS` com hash SHA-256 de cada egg; a verificação falha se o conteúdo mudar sem atualização do manifesto.
- Validação automática dos campos obrigatórios do formato PTDL e do script de instalação.
- Scripts de instalação sem downloads remotos opacos; o conteúdo precisa ser legível e justificável.
- Imagens Docker públicas e declaradas no próprio egg.

## Verificação antes de importar

```bash
./scripts/verify.sh
```

Ou:

```bash
sha256sum -c SHA256SUMS
```

Confira também:

- O script de instalação do egg.
- As variáveis e os valores padrão.
- A imagem Docker usada.
- O histórico do commit que alterou o arquivo.

## Limitações

- O hash detecta alteração do arquivo no repositório, mas não prova sozinho quem o alterou. Para uma garantia mais forte, use commits assinados, tags assinadas e proteção de branch.
- A verificação não audita a imagem Docker upstream; revise a origem e o digest/tag da imagem.
- Um egg revisado ainda executa código dentro do container do servidor. Aplique permissões mínimas e mantenha o painel e o daemon atualizados.

## Reportar um problema

Abra uma issue no repositório descrevendo o egg, o arquivo e o comportamento suspeito. Não inclua tokens, senhas ou dados de clientes.
