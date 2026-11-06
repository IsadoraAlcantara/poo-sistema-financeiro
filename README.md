# Sistema Financeiro - Decisões de Projeto

---

### 1. No Fechamento, os lançamentos originais foram copiados ou referenciados? Por quê?

**Resposta:**  
Os lançamentos foram copiados para manter a integridade dos dados. Quando os lançamentos são limpados da classe Conta os dados não são perdidos. O fechamento atua como o histórico de um período.

---

### 2. Conciliacao virou uma classe própria ou um método de Fechamento? Por quê?

**Resposta:**  
A Conciliacao foi implementada como uma classe própria, pois dessa maneira conciliacao pode atuar de forma independente de fechamento, podendo ser reutilizado em outros momentos para confeir se os dados informados conferem com a realidade.

---

### 3. O que acontece quando não há lançamentos no período, ou quando a conciliação não bate?

**Resposta:**

#### Cenário 1: Sem lançamentos no período

Caso a busca por intervalo de datas não encontre nenhum fechamento correspondente, o extrato é gerado com valores zerados. O sistema foi desenvolvido dessa maneira para que, se o usuário não realizar nenhum lançamento em determinado período, não haja lacunas no histórico.

#### Cenário 2: Conciliação com divergência
* **Na classe Conciliacao:** Ao identificar diferença entre os totais, a classe interrompe a execução do código e gera um erro.
* **No classe Extrato:** O extrato verifica se existe pendências e retorna True ou False, sinalizando a existência de divergências entre os totais sem parar a execução.

---

### 4. Uma Aplicacao guarda a estratégia como atributo, ou ela é passada como parâmetro na hora de calcular o rendimento?

**Resposta:**  
A aplicação guarda a estratégia como atributo, pois a estratégia é algo intrínseco de uma aplicação. Apenas faz sentido uma aplicação financeira existir se ela possuir uma estratégia vinculada.

---

### 5. As interfaces são separadas ou são mesmo conceito com nomes diferentes?

**Resposta:**  
As interfaces criadas para aplicações financeiras possuem a mesma estratégia, pois conceitualmente executam as mesmas funcionalidades.

---

### 6. Qual método foi selecionado?

**Resposta:**  

#### Leitor: Simple Factory

Foi escolhido o método simple factory porque a única informação que diferencia um leitor do outro era o formato, não existindo uma hierarquia de classes criadoras, apenas um método central responsável por fabricar a estratégia de leitura correta. Dessa forma, podendo ser resolvido com ifs.

#### Importador: Simple Factory

Para escolher de qual banco um arquivo foi importado, foi utilizado simple factory, já que apenas um dado diferencia o banco de origem.

#### Exportador: Factory Method

Foi decidido a utilização de factory method, pois cada tipo de exportação possui uma família própria de documentos com comportamentos e estrutura de dados distintos.

---

### 7. Nos seus serviços, o que é injetado e o que ainda é criado internamente? Por quê?

**Resposta:**  

#### Injetado: 

A classe ServicoImportacao recebe o CriadorImportador via Injeção de Dependência no construtor. Da mesma forma, o CriadorImportador recebe o Leitor, e o ImportadorBanco recebe a sua dependência de leitura. Essas dependências representam serviços com comportamento de negócio e infraestrutura. Injetá-los é fundamental para manter o baixo acoplamento, permitir a manutenção de código.

#### Criado internamente:
As classes Extrato, Fechamento, Receita, Despesa e ExtratoBrutoDTO são instanciados diretamente dentro do fluxo de execução. Esses objetos são entidades de domínio e não serviços. Eles representam o estado da aplicação. Tentar injetar entidades de domínio via construtor inflaria a arquitetura sem benefício prático.

--

### 8. Onde está sua raiz de composição?
A raiz de composição se encontra no arquivo servico_importacao

--

### 9. Que colaborador você conseguiria substituir hoje sem editar nenhum serviço?
É possível substituir o Leitor e o ExportadorExtrato, já que o ServicoImportacao e os importadores dependem apenas de interfaces abstratas. Caso sejam adicionadas novas classes a interface Leitor ou ExportadorExtrato, o ServicoImportacao funcionará sem necessidade de alterar código já testado.
