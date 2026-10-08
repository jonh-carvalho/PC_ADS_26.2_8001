# MODELO DE DESIGN (DIAGRAMAS DE SEQUÊNCIA/COMUNICAÇÃO)

## CONSOLIDAÇÃO DA ARQUITETURA

## [NOME DO PROJETO] - [DESCRIÇÃO CURTA DO PROJETO]

---

| **Informação do Documento** | |
| :--- | :--- |
| **Projeto** | [Nome do Projeto] |
| **Documento** | Modelo de Design (Diagramas de Sequência/Comunicação) - Consolidação da Arquitetura |
| **Versão** | 1.0 |
| **Data** | [DD/MM/AAAA] |
| **Status** | Em Desenvolvimento |
| **Responsável** | [Nome do Grupo] |
| **Disciplina** | Projeto de Cloud - Semana 7 |
| **Fase RUP/UP** | Elaboration |

---

## 1. INTRODUÇÃO

### 1.1. Propósito

Este documento apresenta o **Modelo de Design (Diagramas de Sequência/Comunicação)** para a consolidação da arquitetura da plataforma **[NOME DO PROJETO]** na AWS. O modelo demonstra as **interações entre os componentes** em fluxos críticos do sistema, validando a coerência da arquitetura projetada nas semanas anteriores e servindo como base para a implementação.

O modelo é derivado diretamente dos seguintes artefatos:
- **Documento de Visão** (Semana 1) - Seção "Recursos do Produto (Arquitetura AWS)"
- **Documento de Requisitos Suplementares** (Semana 2) - Seções "Desempenho" e "Disponibilidade"
- **Modelo de Casos de Uso Arquiteturais** (Semana 3) - UC-ARQ-XXX
- **Modelo de Análise (Pacotes/Subsistemas)** (Semana 4) - Pacotes de Segurança
- **Modelo de Análise (Classes) - RDS** (Semana 5) - `DatabaseInstance`, `ReadReplica`, `BackupPolicy`
- **Modelo de Análise (Classes) - EC2** (Semana 6) - `ComputeInstance`, `AutoScalingGroup`, `LoadBalancer`

### 1.2. Escopo

O modelo abrange os **fluxos críticos** do projeto, demonstrando as interações entre os componentes. Os fluxos a serem modelados devem ser selecionados com base nos requisitos não-funcionais e nos casos de uso arquiteturais.

**Sugestão de fluxos a modelar (adapte conforme o projeto):**

| **#** | **Fluxo Sugerido** | **Descrição** | **Prioridade** |
| :--- | :--- | :--- | :--- |
| 1 | **Ingestão de Dados** | Entrada de dados (IoT, API, formulário). | Crítica |
| 2 | **Requisição Principal** | Usuário → LB → Compute → Database → Resposta. | Crítica |
| 3 | **Autenticação** | Login, validação de credenciais, geração de token. | Alta |
| 4 | **Deploy Automatizado** | CI/CD pipeline (GitHub → CodePipeline → Compute). | Média |
| 5 | **Failover do Banco** | Falha na AZ primária → Promoção do standby. | Alta |
| 6 | **Upload de Arquivos** | Armazenamento de mídia (S3 + CDN). | Média |

**Fora do escopo:** Fluxos de Big Data (EMR, Redshift), que serão tratados em disciplinas posteriores.

### 1.3. Definições e Siglas

| **Sigla** | **Definição** |
| :--- | :--- |
| **UML** | Unified Modeling Language |
| **ALB** | Application Load Balancer |
| **NLB** | Network Load Balancer |
| **ASG** | Auto Scaling Group |
| **EC2** | Elastic Compute Cloud |
| **RDS** | Relational Database Service |
| **S3** | Simple Storage Service |
| **CDN** | Content Delivery Network |
| **JWT** | JSON Web Token |
| **MFA** | Multi-Factor Authentication |
| **TPS** | Transactions Per Second |
| **RPO** | Recovery Point Objective |
| **RTO** | Recovery Time Objective |
| **SLA** | Service Level Agreement |
| **LGPD** | Lei Geral de Proteção de Dados |

### 1.4. Referências

- Documento de Visão - [NOME DO PROJETO] (v1.0)
- Documento de Requisitos Suplementares - [NOME DO PROJETO] (v1.0)
- Modelo de Casos de Uso Arquiteturais - [NOME DO PROJETO] (v1.0)
- Modelo de Análise (Pacotes/Subsistemas) - [NOME DO PROJETO] (v1.0)
- Modelo de Análise (Classes) - RDS - [NOME DO PROJETO] (v1.0)
- Modelo de Análise (Classes) - EC2 - [NOME DO PROJETO] (v1.0)
- UML Distilled (Martin Fowler)
- AWS Well-Architected Framework - Operational Excellence Pillar

---

## 2. VISÃO GERAL DOS FLUXOS CRÍTICOS

### 2.1. Mapa de Fluxos

| **Fluxo** | **Descrição** | **Ator** | **Componentes Principais** | **Prioridade** | **Requisitos** |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Fluxo 1 | [Descrição] | [Ator] | [Componentes] | [Prioridade] | [Requisitos] |
| Fluxo 2 | [Descrição] | [Ator] | [Componentes] | [Prioridade] | [Requisitos] |
| Fluxo 3 | [Descrição] | [Ator] | [Componentes] | [Prioridade] | [Requisitos] |
| Fluxo 4 | [Descrição] | [Ator] | [Componentes] | [Prioridade] | [Requisitos] |
| Fluxo 5 | [Descrição] | [Ator] | [Componentes] | [Prioridade] | [Requisitos] |
| Fluxo 6 | [Descrição] | [Ator] | [Componentes] | [Prioridade] | [Requisitos] |

### 2.2. Diagrama de Contexto Geral

```plantuml
@startuml
title Diagrama de Contexto Geral - [NOME DO PROJETO]

skinparam componentBackgroundColor #E3F2FD
skinparam actorBackgroundColor #FFF3E0

actor "[Ator 1]" as A1
actor "[Ator 2]" as A2
actor "[Ator 3]" as A3
actor "[Ator 4]" as A4

rectangle "[NOME DO PROJETO] - AWS" {
  component "[Componente 1]" as C1
  component "[Componente 2]" as C2
  component "[Componente 3]" as C3
  component "[Componente 4]" as C4
  component "[Componente 5]" as C5
  component "[Componente 6]" as C6
  component "[Componente 7]" as C7
  component "[Componente 8]" as C8
  component "[Componente 9]" as C9
}

A1 --> C1 : [Ação 1]
A2 --> C2 : [Ação 2]
A3 --> C3 : [Ação 3]
A4 --> C9 : [Ação 4]

C1 --> C2
C2 --> C3
C3 --> C4
C4 --> C5
C5 --> C6
C6 --> C7
C7 --> C8
C8 --> C9

@enduml
```

**Substitua os placeholders** com os componentes reais do seu projeto (ex: API Gateway, Lambda, ALB, EC2, RDS, DynamoDB, S3, Cognito, CodePipeline, CloudWatch).

---

## 3. ESPECIFICAÇÃO DOS FLUXOS

---

### 3.1. FLUXO 1: [NOME DO FLUXO 1]

#### 3.1.1. Descrição

[Descrever o fluxo em detalhes: quem inicia, qual o objetivo, quais componentes estão envolvidos.]

**Exemplo:** O [Ator] envia [dados/ação] para a plataforma [NOME DO PROJETO]. O processamento é feito de forma [serverless/IaaS], garantindo [requisitos].

#### 3.1.2. Requisitos Atendidos

| **Requisito** | **Valor** | **Fonte** |
| :--- | :--- | :--- |
| [Requisito 1] | [Valor] | Requisitos Suplementares |
| [Requisito 2] | [Valor] | Requisitos Suplementares |
| [Requisito 3] | [Valor] | Requisitos Suplementares |
| [Requisito 4] | [Valor] | Requisitos Suplementares |

#### 3.1.3. Diagrama de Sequência

```plantuml
@startuml
title Fluxo 1: [Nome do Fluxo] - [NOME DO PROJETO]

actor "[Ator]" as Ator
participant "[Participante 1]" as P1
participant "[Participante 2]" as P2
participant "[Participante 3]" as P3
participant "[Participante 4]" as P4
participant "[Participante 5]" as P5

== [Fase 1] ==
Ator -> P1: [Mensagem 1]
activate P1

P1 -> P1: [Processamento interno]

P1 -> P2: [Mensagem 2]
activate P2

P2 -> P3: [Mensagem 3]
activate P3
P3 --> P2: [Retorno]
deactivate P3

P2 -> P4: [Mensagem 4]
activate P4
P4 --> P2: [Retorno]
deactivate P4

alt [Condição de Falha]
  P2 -> P5: [Mensagem de Alerta]
  activate P5
  P5 --> P2: [Confirmação]
  deactivate P5
  P2 --> P1: [Erro]
else [Sucesso]
  P2 --> P1: [Sucesso]
end

deactivate P2
P1 --> Ator: [Resposta]
deactivate P1

opt [Condição Opcional]
  P2 -> P5: [Notificação]
  activate P5
  P5 --> P2: [Confirmação]
  deactivate P5
end

@enduml
```

#### 3.1.4. Diagrama de Comunicação

```plantuml
@startuml
title Fluxo 1: Comunicação - [Nome do Fluxo]

skinparam objectBackgroundColor #E3F2FD

object "[Ator]" as Ator
object "[Participante 1]" as P1
object "[Participante 2]" as P2
object "[Participante 3]" as P3
object "[Participante 4]" as P4
object "[Participante 5]" as P5

Ator -right-> P1 : 1: [Mensagem 1]
P1 -right-> P2 : 2: [Mensagem 2]
P2 -right-> P3 : 3: [Mensagem 3]
P3 -left-> P2 : 4: [Retorno]
P2 -right-> P4 : 5: [Mensagem 4]
P4 -left-> P2 : 6: [Retorno]
P2 -down-> P5 : 7: [Notificação]
P2 -left-> P1 : 8: [Resposta]
P1 -left-> Ator : 9: [Resposta Final]

@enduml
```

#### 3.1.5. Tabela de Mensagens

| **#** | **De** | **Para** | **Mensagem** | **Protocolo** | **Requisito** |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | [Ator] | [P1] | [Mensagem] | [Protocolo] | [Requisito] |
| 2 | [P1] | [P2] | [Mensagem] | [Protocolo] | [Requisito] |
| 3 | [P2] | [P3] | [Mensagem] | [Protocolo] | [Requisito] |
| 4 | [P3] | [P2] | [Retorno] | [Protocolo] | - |
| 5 | [P2] | [P4] | [Mensagem] | [Protocolo] | [Requisito] |
| 6 | [P4] | [P2] | [Retorno] | [Protocolo] | - |
| 7 | [P2] | [P5] | [Notificação] | [Protocolo] | - |
| 8 | [P2] | [P1] | [Resposta] | [Protocolo] | - |
| 9 | [P1] | [Ator] | [Resposta Final] | [Protocolo] | - |

#### 3.1.6. Riscos e Mitigações

| **Risco** | **Probabilidade** | **Impacto** | **Mitigação** |
| :--- | :--- | :--- | :--- |
| [Risco 1] | [Alta/Média/Baixa] | [Alto/Médio/Baixo] | [Mitigação] |
| [Risco 2] | [Alta/Média/Baixa] | [Alto/Médio/Baixo] | [Mitigação] |
| [Risco 3] | [Alta/Média/Baixa] | [Alto/Médio/Baixo] | [Mitigação] |

---

### 3.2. FLUXO 2: [NOME DO FLUXO 2]

#### 3.2.1. Descrição

[Descrever o fluxo em detalhes.]

#### 3.2.2. Requisitos Atendidos

| **Requisito** | **Valor** | **Fonte** |
| :--- | :--- | :--- |
| [Requisito 1] | [Valor] | Requisitos Suplementares |
| [Requisito 2] | [Valor] | Requisitos Suplementares |
| [Requisito 3] | [Valor] | Requisitos Suplementares |
| [Requisito 4] | [Valor] | Requisitos Suplementares |

#### 3.2.3. Diagrama de Sequência

```plantuml
@startuml
title Fluxo 2: [Nome do Fluxo] - [NOME DO PROJETO]

actor "[Ator]" as Ator
participant "[Participante 1]" as P1
participant "[Participante 2]" as P2
participant "[Participante 3]" as P3
participant "[Participante 4]" as P4

== [Fase 1] ==
Ator -> P1: [Mensagem 1]
activate P1

P1 -> P2: [Mensagem 2]
activate P2

alt [Cache Hit]
  P2 -> P3: [Consulta ao Cache]
  activate P3
  P3 --> P2: [Dados em Cache]
  deactivate P3
else [Cache Miss]
  P2 -> P4: [Consulta ao Banco]
  activate P4
  P4 --> P2: [Resultado]
  deactivate P4
  P2 -> P3: [Atualizar Cache]
  activate P3
  P3 --> P2: [OK]
  deactivate P3
end

P2 --> P1: [Resposta]
deactivate P2
P1 --> Ator: [Resposta Final]
deactivate P1

@enduml
```

#### 3.2.4. Diagrama de Comunicação

```plantuml
@startuml
title Fluxo 2: Comunicação - [Nome do Fluxo]

skinparam objectBackgroundColor #E3F2FD

object "[Ator]" as Ator
object "[Participante 1]" as P1
object "[Participante 2]" as P2
object "[Participante 3]" as P3
object "[Participante 4]" as P4

Ator -right-> P1 : 1: [Mensagem 1]
P1 -right-> P2 : 2: [Mensagem 2]
P2 -right-> P3 : 3: [Cache]
P3 -left-> P2 : 4: [Hit/Miss]
P2 -right-> P4 : 5: [Banco]
P4 -left-> P2 : 6: [Resultado]
P2 -left-> P1 : 7: [Resposta]
P1 -left-> Ator : 8: [Resposta Final]

@enduml
```

#### 3.2.5. Tabela de Mensagens

| **#** | **De** | **Para** | **Mensagem** | **Protocolo** | **Requisito** |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | [Ator] | [P1] | [Mensagem] | [Protocolo] | [Requisito] |
| 2 | [P1] | [P2] | [Mensagem] | [Protocolo] | [Requisito] |
| 3 | [P2] | [P3] | [Consulta Cache] | [Protocolo] | - |
| 4 | [P3] | [P2] | [Hit/Miss] | [Protocolo] | - |
| 5 | [P2] | [P4] | [Consulta Banco] | [Protocolo] | [Requisito] |
| 6 | [P4] | [P2] | [Resultado] | [Protocolo] | - |
| 7 | [P2] | [P1] | [Resposta] | [Protocolo] | - |
| 8 | [P1] | [Ator] | [Resposta Final] | [Protocolo] | - |

#### 3.2.6. Riscos e Mitigações

| **Risco** | **Probabilidade** | **Impacto** | **Mitigação** |
| :--- | :--- | :--- | :--- |
| [Risco 1] | [Alta/Média/Baixa] | [Alto/Médio/Baixo] | [Mitigação] |
| [Risco 2] | [Alta/Média/Baixa] | [Alto/Médio/Baixo] | [Mitigação] |
| [Risco 3] | [Alta/Média/Baixa] | [Alto/Médio/Baixo] | [Mitigação] |

---

### 3.3. FLUXO 3: [NOME DO FLUXO 3]

#### 3.3.1. Descrição

[Descrever o fluxo em detalhes.]

#### 3.3.2. Requisitos Atendidos

| **Requisito** | **Valor** | **Fonte** |
| :--- | :--- | :--- |
| [Requisito 1] | [Valor] | Requisitos Suplementares |
| [Requisito 2] | [Valor] | Requisitos Suplementares |
| [Requisito 3] | [Valor] | Requisitos Suplementares |

#### 3.3.3. Diagrama de Sequência

```plantuml
@startuml
title Fluxo 3: [Nome do Fluxo] - [NOME DO PROJETO]

actor "[Ator]" as Ator
participant "[Participante 1]" as P1
participant "[Participante 2]" as P2
participant "[Participante 3]" as P3
participant "[Participante 4]" as P4

== [Fase 1] ==
Ator -> P1: [Mensagem 1]
activate P1

P1 -> P2: [Mensagem 2]
activate P2

alt [Credenciais Válidas]
  P2 -> P3: [Assume Role]
  activate P3
  P3 --> P2: [Credentials]
  deactivate P3
  
  P2 -> P2: [Gerar Token]
  P2 --> P1: [Token]
  P1 -> P4: [Validar Token]
  activate P4
  P4 --> P1: [Autenticado]
  deactivate P4
  P1 --> Ator: [HTTP 200]
else [Credenciais Inválidas]
  P2 --> P1: [HTTP 401]
  P1 --> Ator: [HTTP 401]
end

deactivate P2
deactivate P1

@enduml
```

#### 3.3.4. Diagrama de Comunicação

```plantuml
@startuml
title Fluxo 3: Comunicação - [Nome do Fluxo]

skinparam objectBackgroundColor #E3F2FD

object "[Ator]" as Ator
object "[Participante 1]" as P1
object "[Participante 2]" as P2
object "[Participante 3]" as P3
object "[Participante 4]" as P4

Ator -right-> P1 : 1: [Mensagem 1]
P1 -right-> P2 : 2: [Mensagem 2]
P2 -right-> P3 : 3: [Assume Role]
P3 -left-> P2 : 4: [Credentials]
P2 -left-> P1 : 5: [Token]
P1 -right-> P4 : 6: [Validar]
P4 -left-> P1 : 7: [Autenticado]
P1 -left-> Ator : 8: [HTTP 200]

@enduml
```

#### 3.3.5. Tabela de Mensagens

| **#** | **De** | **Para** | **Mensagem** | **Protocolo** | **Requisito** |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | [Ator] | [P1] | [Mensagem] | [Protocolo] | [Requisito] |
| 2 | [P1] | [P2] | [Mensagem] | [Protocolo] | [Requisito] |
| 3 | [P2] | [P3] | [Assume Role] | [Protocolo] | [Requisito] |
| 4 | [P3] | [P2] | [Credentials] | [Protocolo] | - |
| 5 | [P2] | [P1] | [Token] | [Protocolo] | [Requisito] |
| 6 | [P1] | [P4] | [Validar] | [Protocolo] | - |
| 7 | [P4] | [P1] | [Autenticado] | [Protocolo] | - |
| 8 | [P1] | [Ator] | [HTTP 200] | [Protocolo] | - |

#### 3.3.6. Riscos e Mitigações

| **Risco** | **Probabilidade** | **Impacto** | **Mitigação** |
| :--- | :--- | :--- | :--- |
| [Risco 1] | [Alta/Média/Baixa] | [Alto/Médio/Baixo] | [Mitigação] |
| [Risco 2] | [Alta/Média/Baixa] | [Alto/Médio/Baixo] | [Mitigação] |
| [Risco 3] | [Alta/Média/Baixa] | [Alto/Médio/Baixo] | [Mitigação] |

---

### 3.4. FLUXO 4: [NOME DO FLUXO 4]

#### 3.4.1. Descrição

[Descrever o fluxo em detalhes.]

#### 3.4.2. Requisitos Atendidos

| **Requisito** | **Valor** | **Fonte** |
| :--- | :--- | :--- |
| [Requisito 1] | [Valor] | Requisitos Suplementares |
| [Requisito 2] | [Valor] | Requisitos Suplementares |
| [Requisito 3] | [Valor] | Requisitos Suplementares |

#### 3.4.3. Diagrama de Sequência

```plantuml
@startuml
title Fluxo 4: [Nome do Fluxo] - [NOME DO PROJETO]

actor "[Ator]" as Ator
participant "[Participante 1]" as P1
participant "[Participante 2]" as P2
participant "[Participante 3]" as P3
participant "[Participante 4]" as P4
participant "[Participante 5]" as P5
participant "[Participante 6]" as P6

== [Fase 1] ==
Ator -> P1: [Mensagem 1]
activate P1

P1 --> P2: [Webhook]
deactivate P1

activate P2
P2 -> P1: [Source]
P1 --> P2: [Code]

P2 -> P3: [Build]
activate P3
P3 -> P3: [Install Dependencies]
P3 -> P3: [Run Tests]
P3 -> P4: [Push Image]
activate P4
P4 --> P3: [Image Registered]
deactivate P4
P3 --> P2: [Build Success]
deactivate P3

P2 -> P5: [Deploy]
activate P5
P5 -> P6: [Health Check]
activate P6
P6 --> P5: [Healthy]
deactivate P6
P5 --> P2: [Deployed]
deactivate P5

P2 -> Ator: [Aprovação Manual]
Ator -> P2: [Approve]

P2 -> P6: [Switch Traffic]
activate P6
P6 --> P2: [Traffic Switched]
deactivate P6

P2 --> Ator: [Deploy Complete]
deactivate P2

@enduml
```

#### 3.4.4. Diagrama de Comunicação

```plantuml
@startuml
title Fluxo 4: Comunicação - [Nome do Fluxo]

skinparam objectBackgroundColor #E3F2FD

object "[Ator]" as Ator
object "[Participante 1]" as P1
object "[Participante 2]" as P2
object "[Participante 3]" as P3
object "[Participante 4]" as P4
object "[Participante 5]" as P5
object "[Participante 6]" as P6

Ator -right-> P1 : 1: [Mensagem 1]
P1 -right-> P2 : 2: [Webhook]
P2 -right-> P3 : 3: [Build]
P3 -right-> P4 : 4: [Push Image]
P2 -right-> P5 : 5: [Deploy]
P5 -right-> P6 : 6: [Health Check]
Ator -down-> P2 : 7: [Approve]
P2 -right-> P6 : 8: [Switch Traffic]
P2 -left-> Ator : 9: [Complete]

@enduml
```

#### 3.4.5. Tabela de Mensagens

| **#** | **De** | **Para** | **Mensagem** | **Protocolo** | **Requisito** |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | [Ator] | [P1] | [Mensagem] | [Protocolo] | [Requisito] |
| 2 | [P1] | [P2] | [Webhook] | [Protocolo] | - |
| 3 | [P2] | [P3] | [Build] | [Protocolo] | [Requisito] |
| 4 | [P3] | [P4] | [Push Image] | [Protocolo] | - |
| 5 | [P2] | [P5] | [Deploy] | [Protocolo] | - |
| 6 | [P5] | [P6] | [Health Check] | [Protocolo] | - |
| 7 | [Ator] | [P2] | [Approve] | [Protocolo] | - |
| 8 | [P2] | [P6] | [Switch Traffic] | [Protocolo] | - |
| 9 | [P2] | [Ator] | [Complete] | [Protocolo] | - |

#### 3.4.6. Riscos e Mitigações

| **Risco** | **Probabilidade** | **Impacto** | **Mitigação** |
| :--- | :--- | :--- | :--- |
| [Risco 1] | [Alta/Média/Baixa] | [Alto/Médio/Baixo] | [Mitigação] |
| [Risco 2] | [Alta/Média/Baixa] | [Alto/Médio/Baixo] | [Mitigação] |
| [Risco 3] | [Alta/Média/Baixa] | [Alto/Médio/Baixo] | [Mitigação] |

---

### 3.5. FLUXO 5: [NOME DO FLUXO 5]

#### 3.5.1. Descrição

[Descrever o fluxo em detalhes.]

#### 3.5.2. Requisitos Atendidos

| **Requisito** | **Valor** | **Fonte** |
| :--- | :--- | :--- |
| [Requisito 1] | [Valor] | Requisitos Suplementares |
| [Requisito 2] | [Valor] | Requisitos Suplementares |
| [Requisito 3] | [Valor] | Requisitos Suplementares |

#### 3.5.3. Diagrama de Sequência

```plantuml
@startuml
title Fluxo 5: [Nome do Fluxo] - [NOME DO PROJETO]

actor "[Ator]" as Ator
participant "[Participante 1]" as P1
participant "[Participante 2]" as P2
participant "[Participante 3]" as P3
participant "[Participante 4]" as P4
participant "[Participante 5]" as P5

== Operação Normal ==
Ator -> P1: [Mensagem 1]
activate P1
P1 -> P2: [Mensagem 2]
activate P2
P2 --> P1: [Resposta]
deactivate P2
P1 --> Ator: [Resposta]
deactivate P1

== Falha Detectada ==
P1 -> P1: [Falha detectada]
activate P1
P1 -> P3: [Métrica]
deactivate P1

P3 -> P3: [Alarme disparado]
P3 -> P4: [Publicar alerta]
activate P4
P4 --> P3: [Confirmação]
deactivate P4

== Failover Automático ==
P3 -> P2: [Promover]
activate P2
P2 -> P2: [Assumir papel]
P2 -> P5: [Atualizar endpoint]
activate P5
P5 --> P2: [Endpoint atualizado]
deactivate P5
P2 --> P3: [Failover concluído]
deactivate P2

== Retomada ==
Ator -> P5: [Resolver endpoint]
activate P5
P5 --> Ator: [Novo endpoint]
deactivate P5

Ator -> P2: [Conexão]
activate P2
P2 --> Ator: [Dados]
deactivate P2

@enduml
```

#### 3.5.4. Diagrama de Comunicação

```plantuml
@startuml
title Fluxo 5: Comunicação - [Nome do Fluxo]

skinparam objectBackgroundColor #E3F2FD

object "[Ator]" as Ator
object "[Participante 1]" as P1
object "[Participante 2]" as P2
object "[Participante 3]" as P3
object "[Participante 4]" as P4
object "[Participante 5]" as P5

Ator -right-> P1 : 1: [Mensagem 1]
P1 -right-> P2 : 2: [Mensagem 2]
P1 -down-> P3 : 3: [Métrica]
P3 -down-> P4 : 4: [Alerta]
P3 -right-> P2 : 5: [Promover]
P2 -right-> P5 : 6: [Atualizar]
Ator -right-> P5 : 7: [Resolver]
P5 -left-> Ator : 8: [Novo Endpoint]
Ator -right-> P2 : 9: [Conexão]

@enduml
```

#### 3.5.5. Tabela de Mensagens

| **#** | **De** | **Para** | **Mensagem** | **Protocolo** | **Requisito** |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | [Ator] | [P1] | [Mensagem] | [Protocolo] | [Requisito] |
| 2 | [P1] | [P2] | [Mensagem] | [Protocolo] | [Requisito] |
| 3 | [P1] | [P3] | [Métrica] | [Protocolo] | - |
| 4 | [P3] | [P4] | [Alerta] | [Protocolo] | - |
| 5 | [P3] | [P2] | [Promover] | [Protocolo] | [Requisito] |
| 6 | [P2] | [P5] | [Atualizar] | [Protocolo] | - |
| 7 | [Ator] | [P5] | [Resolver] | [Protocolo] | - |
| 8 | [P5] | [Ator] | [Novo Endpoint] | [Protocolo] | - |
| 9 | [Ator] | [P2] | [Conexão] | [Protocolo] | [Requisito] |

#### 3.5.6. Riscos e Mitigações

| **Risco** | **Probabilidade** | **Impacto** | **Mitigação** |
| :--- | :--- | :--- | :--- |
| [Risco 1] | [Alta/Média/Baixa] | [Alto/Médio/Baixo] | [Mitigação] |
| [Risco 2] | [Alta/Média/Baixa] | [Alto/Médio/Baixo] | [Mitigação] |
| [Risco 3] | [Alta/Média/Baixa] | [Alto/Médio/Baixo] | [Mitigação] |

---

### 3.6. FLUXO 6: [NOME DO FLUXO 6]

#### 3.6.1. Descrição

[Descrever o fluxo em detalhes.]

#### 3.6.2. Requisitos Atendidos

| **Requisito** | **Valor** | **Fonte** |
| :--- | :--- | :--- |
| [Requisito 1] | [Valor] | Requisitos Suplementares |
| [Requisito 2] | [Valor] | Requisitos Suplementares |
| [Requisito 3] | [Valor] | Requisitos Suplementares |

#### 3.6.3. Diagrama de Sequência

```plantuml
@startuml
title Fluxo 6: [Nome do Fluxo] - [NOME DO PROJETO]

actor "[Ator]" as Ator
participant "[Participante 1]" as P1
participant "[Participante 2]" as P2
participant "[Participante 3]" as P3
participant "[Participante 4]" as P4
participant "[Participante 5]" as P5

== [Fase 1] ==
Ator -> P1: [Mensagem 1]
activate P1

P1 -> P2: [Mensagem 2]
activate P2

P2 -> P2: [Processamento interno]
P2 -> P3: [GenerateDataKey]
activate P3
P3 --> P2: [Data Key]
deactivate P3

P2 -> P4: [PutObject]
activate P4
P4 --> P2: [Success]
deactivate P4

P2 --> P1: [Resposta]
deactivate P2
P1 --> Ator: [Resposta Final]
deactivate P1

== [Fase 2] ==
Ator -> P5: [Acesso]
activate P5
P5 -> P4: [GetObject]
activate P4
P4 --> P5: [Objeto]
deactivate P4
P5 --> Ator: [Objeto]
deactivate P5

@enduml
```

#### 3.6.4. Diagrama de Comunicação

```plantuml
@startuml
title Fluxo 6: Comunicação - [Nome do Fluxo]

skinparam objectBackgroundColor #E3F2FD

object "[Ator]" as Ator
object "[Participante 1]" as P1
object "[Participante 2]" as P2
object "[Participante 3]" as P3
object "[Participante 4]" as P4
object "[Participante 5]" as P5

Ator -right-> P1 : 1: [Mensagem 1]
P1 -right-> P2 : 2: [Mensagem 2]
P2 -right-> P3 : 3: [GenerateDataKey]
P3 -left-> P2 : 4: [Data Key]
P2 -right-> P4 : 5: [PutObject]
P2 -left-> P1 : 6: [Resposta]
Ator -right-> P5 : 7: [Acesso]
P5 -right-> P4 : 8: [GetObject]
P4 -left-> P5 : 9: [Objeto]

@enduml
```

#### 3.6.5. Tabela de Mensagens

| **#** | **De** | **Para** | **Mensagem** | **Protocolo** | **Requisito** |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | [Ator] | [P1] | [Mensagem] | [Protocolo] | [Requisito] |
| 2 | [P1] | [P2] | [Mensagem] | [Protocolo] | [Requisito] |
| 3 | [P2] | [P3] | [GenerateDataKey] | [Protocolo] | [Requisito] |
| 4 | [P3] | [P2] | [Data Key] | [Protocolo] | - |
| 5 | [P2] | [P4] | [PutObject] | [Protocolo] | - |
| 6 | [P2] | [P1] | [Resposta] | [Protocolo] | - |
| 7 | [Ator] | [P5] | [Acesso] | [Protocolo] | - |
| 8 | [P5] | [P4] | [GetObject] | [Protocolo] | - |
| 9 | [P4] | [P5] | [Objeto] | [Protocolo] | - |

#### 3.6.6. Riscos e Mitigações

| **Risco** | **Probabilidade** | **Impacto** | **Mitigação** |
| :--- | :--- | :--- | :--- |
| [Risco 1] | [Alta/Média/Baixa] | [Alto/Médio/Baixo] | [Mitigação] |
| [Risco 2] | [Alta/Média/Baixa] | [Alto/Médio/Baixo] | [Mitigação] |
| [Risco 3] | [Alta/Média/Baixa] | [Alto/Médio/Baixo] | [Mitigação] |

---

## 4. DIAGRAMA DE CLASSES CONSOLIDADO

```plantuml
@startuml
title Modelo de Design Consolidado - [NOME DO PROJETO]

skinparam classBackgroundColor #F5F5F5

package "Rede" {
  class "VPC" as VPC {
    - cidr: [CIDR]
    - subnets: List<Subnet>
  }
  class "Subnet" as Subnet {
    - cidr: String
    - type: Public/Private
    - az: String
  }
  VPC "1" -- "*" Subnet
}

package "Computação" {
  class "ComputeInstance" as EC2 {
    - instanceType: [Classe]
    - ami: [AMI]
  }
  class "AutoScalingGroup" as ASG {
    - min: [N]
    - max: [N]
  }
  class "LoadBalancer" as ALB {
    - type: [Tipo]
  }
  ASG "1" -- "*" EC2
  ALB "1" -- "*" EC2
}

package "Banco de Dados" {
  class "DatabaseInstance" as RDS {
    - instanceClass: [Classe]
    - multiAZ: [true/false]
  }
  class "ReadReplica" as RR {
    - instanceClass: [Classe]
  }
  RDS "1" -- "*" RR
}

package "Segurança" {
  class "SecurityGroup" as SG
  class "IAMRole" as IAM
  class "KMSKey" as KMS
}

package "Armazenamento" {
  class "StorageBucket" as S3
  class "CloudFront" as CF
  S3 "1" -- "1" CF
}

EC2 --> RDS : usa
EC2 --> S3 : usa
EC2 --> SG : protegido
EC2 --> IAM : assume
ALB --> SG : protegido
RDS --> SG : protegido
RDS --> KMS : criptografado
S3 --> KMS : criptografado

@enduml
```

---

## 5. MATRIZ DE RASTREAMENTO CONSOLIDADA

| **Fluxo** | **Requisito (Doc. Suplementar)** | **Caso de Uso (Semana 3)** | **Pacote (Semana 4)** | **Classe (Semana 5/6)** | **Serviços AWS** |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Fluxo 1 | [Requisito] | [UC-ARQ-XXX] | [Pacote] | [Classe] | [Serviços] |
| Fluxo 2 | [Requisito] | [UC-ARQ-XXX] | [Pacote] | [Classe] | [Serviços] |
| Fluxo 3 | [Requisito] | [UC-ARQ-XXX] | [Pacote] | [Classe] | [Serviços] |
| Fluxo 4 | [Requisito] | [UC-ARQ-XXX] | [Pacote] | [Classe] | [Serviços] |
| Fluxo 5 | [Requisito] | [UC-ARQ-XXX] | [Pacote] | [Classe] | [Serviços] |
| Fluxo 6 | [Requisito] | [UC-ARQ-XXX] | [Pacote] | [Classe] | [Serviços] |

---

## 6. CONSIDERAÇÕES FINAIS

### 6.1. Lições Aprendidas

- Os **diagramas de sequência** demonstram a ordem cronológica das mensagens entre componentes.
- Os **diagramas de comunicação** complementam a visão estrutural das interações.
- Os **fluxos críticos** cobrem os principais cenários do projeto.
- A **consolidação da arquitetura** valida a coerência entre todos os artefatos produzidos.
- O **CloudWatch** aparece em todos os fluxos como componente transversal de monitoramento.

### 6.2. Próximos Passos

- **Semana 8:** Consolidação Final do Modelo de Design e Revisão do DAS.
- **Semana 9:** Estratégias de Deploy (Blue-Green, Canary, Rolling) e CI/CD.
- **Semana 10:** Introdução a Containers (Docker) e Orquestração (ECS/EKS).

---

## 7. APROVAÇÕES

| **Função** | **Nome** | **Data** | **Assinatura** |
| :--- | :--- | :--- | :--- |
| Arquiteto de Soluções | | | |
| Arquiteto de Design | | | |
| Professor Responsável | | | |
| Coordenador do Curso | | | |

---

## 8. HISTÓRICO DE VERSÕES

| **Versão** | **Data** | **Autor** | **Descrição das Alterações** |
| :--- | :--- | :--- | :--- |
| 0.1 | [DD/MM/AAAA] | [Nome do Grupo] | Criação inicial do documento. |
| 1.0 | [DD/MM/AAAA] | [Nome do Grupo] | Versão completa com todos os fluxos. |

---

**FIM DO DOCUMENTO**

---

## INSTRUÇÕES DE PREENCHIMENTO

### Como Utilizar Este Modelo

1. **Substitua os placeholders** `[NOME DO PROJETO]`, `[DD/MM/AAAA]`, `[Nome do Grupo]` pelas informações do seu projeto.
2. **Adapte os fluxos** conforme as necessidades específicas do seu projeto (nem todos terão 6 fluxos).
3. **Preencha as tabelas de mensagens** com os detalhes do seu caso.
4. **Utilize os diagramas PlantUML** como base, adaptando os participantes e mensagens.
5. **Documente os riscos** e mitigações para cada fluxo.
6. **Valide a consistência** com os artefatos das semanas anteriores.

### Critérios de Avaliação

| **Critério** | **Peso** | **Descrição** |
| :--- | :--- | :--- |
| **Completude dos Fluxos** | 25% | Todos os fluxos críticos estão modelados? |
| **Diagramas PlantUML** | 20% | Os diagramas estão corretos e completos? |
| **Tabelas de Mensagens** | 20% | As mensagens estão detalhadas e corretas? |
| **Justificativas Técnicas** | 20% | As decisões são bem fundamentadas? |
| **Riscos e Mitigações** | 15% | Os riscos estão identificados e mitigados? |