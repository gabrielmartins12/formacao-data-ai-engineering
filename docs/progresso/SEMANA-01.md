# Progresso de estudos — 04/11/2026

## Situação
- Curso: Formação Data & AI Engineering (48 semanas).
- Semana 01 — Linux e terminal.
- **Aula 01 (teoria): concluída e aprovada.**
- **Aula 02 (laboratório de validação CSV): próxima atividade; preparação de diretórios ainda não confirmada.**

## Avaliações
| Atividade | Nota |
| --- | ---: |
| Exercício 01 — filesystem | 75/100 |
| Exercício 02 — permissões | 85/100 |
| Exercício 03 — processos e pipes | 100/100 |
| Avaliação final da teoria | 90/100 |
| Exercício complementar — tratamento de erros | 85/100 |

Média das cinco atividades: **87/100**. Notas atribuídas durante as correções didáticas.

## Conteúdo abordado
- Filesystem, diretórios, caminhos absolutos e relativos, `pwd`, `cd`, `ls`.
- Permissões `rwx`, `chmod` e execução de scripts.
- Processos, PID, `sleep`, `jobs`, `ps`, `kill`.
- Pipes, redirecionamentos, `grep`, `find`, `wc`, `tail`.
- Bash, variáveis, `export` e noções de ambientes.
- Verificação de arquivo ausente com `[[ ! -f "$ARQUIVO" ]]`, mensagens em stderr e `exit 1`.
- Introdução a `set -euo pipefail` e suas ressalvas.

## Prática confirmada pelo terminal do aluno
No diretório local `~/laboratorio-linux`, o aluno criou e executou `analisar_vendas.sh`, com saída:
```text
Iniciando análise de vendas...
Total de registros:
5
Registros com erro:
2
Análise concluída!
```
Permissões confirmadas por `ls -l`: `-rwxr--r--.` (equivalente a 744, desconsiderando atributos adicionais).

O aluno também relatou a mensagem de arquivo ausente no teste de falha. **Não foi apresentada a saída de `echo $?`**, portanto o código de saída ainda precisa ser confirmado.

**Observação:** os arquivos do laboratório estão na máquina local do aluno; este registro não significa que foram enviados ao GitHub.

## Pontos de atenção
- Distinguir `chmod u+x script.sh` de `./script.sh`.
- Diferenciar mensagens impressas do código de saída do processo.
- Não presumir que `grep "OK"` valida especificamente a coluna status de um CSV.
- Tratar `grep` sem correspondências (status 1) com cuidado ao usar `set -e`.

## Retomada — Semana 01, Aula 02 (3h)
Objetivo curricular: automatizar a validação de arquivos CSV com Shell.

1. Criar a estrutura local:
   ```bash
   cd ~/laboratorio-linux
   mkdir -p validador-csv/{dados,scripts,relatorios}
   cd validador-csv
   find . -type d
   ```
2. Confirmar a saída de `find . -type d` com o professor.
3. Criar datasets sintéticos válidos e inválidos.
4. Implementar verificações de existência, leitura, vazio, cabeçalho e registros, com erros tratados.
5. Executar testes independentes e gerar relatório de validação.
6. Documentar limitações do parsing de CSV via Shell.

Critério da semana: script executável, erros tratados e comandos explicados. Progredir por domínio demonstrado, referência 70/100 sem falhas críticas.
