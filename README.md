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

Caso a busca por intervalo de datas não encontre nenhum fechamento correspondente, o extrato é gerado com valores zerados. Foi feito dessa maneira para que caso o usuário não faça nenhum lançamento em determinado período não fique um  histórico faltando.

#### Cenário 2: Conciliação com divergência
* **Na classe Conciliacao:** Ao identificar diferença entre os totais, a classe interrompe a execução do código e gera um erro.
* **No classe Extrato:** O extrato verifica se existe pendências e retorna True ou False, sinalizando a existência de divergências entre os totais sem parar a execução.
