## Diferentes modelos

![er-aluno-nota](images/er-aluno-nota.svg)

**Aluno:**

|RA   |Nome                           |
|-----|-------------------------------|
|63060|Allainclair Flausino dos Santos|
|63061|Yan Xurupita                   |
|63062|Roberto Carlos Hideki          |

**Nota:**

|Codigo|RA       |Valor |
|------|---------|------|
|**1** |**63060**|**10**|
|2     |63060    |10    |
|3     |63060    |10    |
|4     |63061    |9     |
|5     |63061    |8     |
|6     |63061    |7     |
|**7** |**63061**|**10**|
|8     |63062    |5     |
|9     |63062    |5     |
|10    |63062    |5     |
|**11**|**63062**|**10**|

![nota-grupo-aluno](images/nota-grupo-aluno.svg)

**Aluno:**

|RA   |Nome                           |
|-----|-------------------------------|
|63060|Allainclair Flausino dos Santos|
|63061|Yan Xurupita                   |
|63062|Roberto Carlos Hideki          |


**Grupo:**

|CodigoGrupo|
|-----------|
|1          |
|2          |
|3          |
|4          |

**Grupo Aluno:**

|CodigoGrupo|RA   |
|-----------|-----|
|1          |63060|
|1          |63061|
|1          |63062|
|2          |63060|
|3          |63061|
|4          |63062|
|5          |63062|
|5          |63061|

**Nota:**

|CodigoNota|CodigoGrupo|Valor |
|----------|-----------|------|
|**1**     |**1**      |**10**|
|2         |2          |10    |
|3         |2          |10    |
|4         |3          |9     |
|5         |3          |8     |
|6         |3          |7     |
|7         |4          |5     |
|8         |4          |5     |
|9         |4          |5     |

Diminuiu duas instâncias na tabela **Nota**.