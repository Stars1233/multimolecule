---
language: rna
tags:
  - Biology
  - RNA
license: agpl-3.0
datasets:
  - multimolecule/ensembl-genome-browser
library_name: multimolecule
pipeline_tag: fill-mask
mask_token: "<mask>"
widget:
  - example_title: "HIV-1"
    text: "GGUC<mask>CUCUGGUUAGACCAGAUCUGAGCCU"
    output:
      - label: "*"
        score: 0.07707168161869049
      - label: "<null>"
        score: 0.07588472962379456
      - label: "U"
        score: 0.07178673148155212
      - label: "N"
        score: 0.06414645165205002
      - label: "Y"
        score: 0.06385370343923569
  - example_title: "microRNA-21"
    text: "UAGC<mask>UAUCAGACUGAUGUUG"
    output:
      - label: "*"
        score: 0.07969731837511063
      - label: "<null>"
        score: 0.07818876206874847
      - label: "A"
        score: 0.07302683591842651
      - label: "N"
        score: 0.06714905053377151
      - label: "W"
        score: 0.0667526125907898
---

# UTR-LM

Pre-trained model on 5’ untranslated region (5’UTR) using masked language modeling (MLM), Secondary Structure (SS), and Minimum Free Energy (MFE) objectives.

## Statement

_A 5’ UTR Language Model for Decoding Untranslated Regions of mRNA and Function Predictions_ is published in [Nature Machine Intelligence](https://doi.org/10.1038/s42256-024-00823-9), which is a Closed Access / Author-Fee journal.

> Machine learning has been at the forefront of the movement for free and open access to research.
>
> We see no role for closed access or author-fee publication in the future of machine learning research and believe the adoption of these journals as an outlet of record for the machine learning community would be a retrograde step.

The MultiMolecule team is committed to the principles of open access and open science.

We do NOT endorse the publication of manuscripts in Closed Access / Author-Fee journals and encourage the community to support Open Access journals and conferences.

Please consider signing the [Statement on Nature Machine Intelligence](https://openaccess.engineering.oregonstate.edu).

## Disclaimer

This is an UNOFFICIAL implementation of the [A 5’ UTR Language Model for Decoding Untranslated Regions of mRNA and Function Predictions](https://doi.org/10.1101/2023.10.11.561938) by Yanyi Chu, Dan Yu, et al.

The OFFICIAL repository of UTR-LM is at [a96123155/UTR-LM](https://github.com/a96123155/UTR-LM).

> [!WARNING]
> The MultiMolecule team is unable to confirm that the provided model and checkpoints are producing the same intermediate representations as the original implementation.
> This is because
>
> The proposed method is published in a Closed Access / Author-Fee journal.

**The team releasing UTR-LM did not write this model card for this model so this model card has been written by the MultiMolecule team.**

## Model Details

UTR-LM is a [bert](https://huggingface.co/google-bert/bert-base-uncased)-style model pre-trained on a large corpus of 5’ untranslated regions (5’UTRs) in a self-supervised fashion. This means that the model was trained on the raw nucleotides of RNA sequences only, with an automatic process to generate inputs and labels from those texts. Please refer to the [Training Details](#training-details) section for more information on the training process.

### Variants

- **[multimolecule/utrlm-te_el](https://huggingface.co/multimolecule/utrlm-te_el)**: The UTR-LM model for Translation Efficiency of transcripts and mRNA Expression Level.
- **[multimolecule/utrlm-mrl](https://huggingface.co/multimolecule/utrlm-mrl)**: The UTR-LM model for Mean Ribosome Loading.

### Model Specification

<table>
<thead>
  <tr>
    <th>Variants</th>
    <th>Num Layers</th>
    <th>Hidden Size</th>
    <th>Num Heads</th>
    <th>Intermediate Size</th>
    <th>Num Parameters (M)</th>
    <th>FLOPs (G)</th>
    <th>MACs (G)</th>
    <th>Max Num Tokens</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>UTR-LM MRL</td>
    <td rowspan="2">6</td>
    <td rowspan="2">128</td>
    <td rowspan="2">16</td>
    <td rowspan="2">512</td>
    <td rowspan="2">1.21</td>
    <td rowspan="2">0.35</td>
    <td rowspan="2">0.18</td>
    <td rowspan="2">1022</td>
  </tr>
  <tr>
    <td>UTR-LM TE_EL</td>
  </tr>
</tbody>
</table>

### Links

- **Code**: [multimolecule.utrlm](https://github.com/DLS5-Omics/multimolecule/tree/master/multimolecule/models/utrlm)
- **Data**:
  - [Ensembl Genome Browser](https://ensembl.org)
  - [Human 5′ UTR design and variant effect prediction from a massively parallel translation assay](https://doi.org/10.1038/s41587-019-0164-5)
  - [High-Throughput 5’ UTR Engineering for Enhanced Protein Production in Non-Viral Gene Therapies](https://doi.org/10.1101/2021.10.14.464013)
- **Paper**: [A 5’ UTR Language Model for Decoding Untranslated Regions of mRNA and Function Predictions](http://doi.org/10.1038/s41467-021-24436-7)
- **Developed by**: Yanyi Chu, Dan Yu, Yupeng Li, Kaixuan Huang, Yue Shen, Le Cong, Jason Zhang, Mengdi Wang
- **Model type**: [BERT](https://huggingface.co/google-bert/bert-base-uncased) - [ESM](https://huggingface.co/facebook/esm2_t48_15B_UR50D)
- **Original Repository**: [a96123155/UTR-LM](https://github.com/a96123155/UTR-LM)

## Usage

The model file depends on the [`multimolecule`](https://multimolecule.danling.org) library. You can install it using pip:

```bash
pip install multimolecule
```

### Direct Use

#### Masked Language Modeling

You can use this model directly with a pipeline for masked language modeling:

```python
>>> import multimolecule  # you must import multimolecule to register models
>>> from transformers import pipeline

>>> unmasker = pipeline("fill-mask", model="multimolecule/utrlm-te_el")
>>> unmasker("gguc<mask>cucugguuagaccagaucugagccu")
[{'score': 0.07707168161869049,
  'token': 23,
  'token_str': '*',
  'sequence': 'G G U C * C U C U G G U U A G A C C A G A U C U G A G C C U'},
 {'score': 0.07588472962379456,
  'token': 5,
  'token_str': '<null>',
  'sequence': 'G G U C C U C U G G U U A G A C C A G A U C U G A G C C U'},
 {'score': 0.07178673148155212,
  'token': 9,
  'token_str': 'U',
  'sequence': 'G G U C U C U C U G G U U A G A C C A G A U C U G A G C C U'},
 {'score': 0.06414645165205002,
  'token': 10,
  'token_str': 'N',
  'sequence': 'G G U C N C U C U G G U U A G A C C A G A U C U G A G C C U'},
 {'score': 0.06385370343923569,
  'token': 12,
  'token_str': 'Y',
  'sequence': 'G G U C Y C U C U G G U U A G A C C A G A U C U G A G C C U'}]
```

#### RNA Secondary Structure Prediction

You can use this model to predict the secondary structure of an RNA sequence:

```python
>>> import multimolecule  # you must import multimolecule to register models
>>> from transformers import pipeline

>>> predictor = pipeline("rna-secondary-structure", model="multimolecule/utrlm-mrl")
>>> predictor("ggucuc")
{'sequence': 'G G U C U C',
 'secondary_structure': '......',
 'contact_map': [[0.4812554717063904, 0.47794032096862793, 0.4789176285266876, 0.4882325828075409, 0.474841445684433, 0.4968946874141693],
  [0.47794032096862793, 0.4934563636779785, 0.4848025441169739, 0.49337026476860046, 0.4595194160938263, 0.4890444576740265],
  [0.4789176285266876, 0.4848025441169739, 0.489326536655426, 0.4909892976284027, 0.48537197709083557, 0.46868011355400085],
  [0.4882325828075409, 0.49337026476860046, 0.4909892976284027, 0.4644699990749359, 0.49569272994995117, 0.4653873145580292],
  [0.474841445684433, 0.4595194160938263, 0.48537197709083557, 0.49569272994995117, 0.4874499440193176, 0.4952647387981415],
  [0.4968947470188141, 0.4890444576740265, 0.4686800539493561, 0.4653873145580292, 0.4952647387981415, 0.4828568994998932]]}
```

### Downstream Use

#### Extract Features

Here is how to use this model to get the features of a given sequence in PyTorch:

```python
from multimolecule import RnaTokenizer, UtrLmModel


tokenizer = RnaTokenizer.from_pretrained("multimolecule/utrlm-te_el")
model = UtrLmModel.from_pretrained("multimolecule/utrlm-te_el")

text = "UAGCUUAUCAGACUGAUGUUG"
input = tokenizer(text, return_tensors="pt")

output = model(**input)
```

#### Sequence Classification / Regression

> [!NOTE]
> This model is not fine-tuned for any specific task. You will need to fine-tune the model on a downstream task to use it for sequence classification or regression.

Here is how to use this model as backbone to fine-tune for a sequence-level task in PyTorch:

```python
import torch
from multimolecule import RnaTokenizer, UtrLmForSequencePrediction


tokenizer = RnaTokenizer.from_pretrained("multimolecule/utrlm-te_el")
model = UtrLmForSequencePrediction.from_pretrained("multimolecule/utrlm-te_el")

text = "UAGCUUAUCAGACUGAUGUUG"
input = tokenizer(text, return_tensors="pt")
label = torch.tensor([1])

output = model(**input, labels=label)
```

#### Token Classification / Regression

> [!NOTE]
> This model is not fine-tuned for any specific task. You will need to fine-tune the model on a downstream task to use it for token classification or regression.

Here is how to use this model as backbone to fine-tune for a nucleotide-level task in PyTorch:

```python
import torch
from multimolecule import RnaTokenizer, UtrLmForTokenPrediction


tokenizer = RnaTokenizer.from_pretrained("multimolecule/utrlm-te_el")
model = UtrLmForTokenPrediction.from_pretrained("multimolecule/utrlm-te_el")

text = "UAGCUUAUCAGACUGAUGUUG"
input = tokenizer(text, return_tensors="pt")
label = torch.randint(2, (len(text), ))

output = model(**input, labels=label)
```

#### Contact Classification / Regression

> [!NOTE]
> This model is not fine-tuned for any specific task. You will need to fine-tune the model on a downstream task to use it for contact classification or regression.

Here is how to use this model as backbone to fine-tune for a contact-level task in PyTorch:

```python
import torch
from multimolecule import RnaTokenizer, UtrLmForContactPrediction


tokenizer = RnaTokenizer.from_pretrained("multimolecule/utrlm-te_el")
model = UtrLmForContactPrediction.from_pretrained("multimolecule/utrlm-te_el")

text = "UAGCUUAUCAGACUGAUGUUG"
input = tokenizer(text, return_tensors="pt")
label = torch.randint(2, (len(text), len(text)))

output = model(**input, labels=label)
```

## Training Details

UTR-LM used a mixed training strategy with one self-supervised task and two supervised tasks, where the labels of both supervised tasks are calculated using [ViennaRNA](https://viennarna.readthedocs.io).

1. **Masked Language Modeling (MLM)**: taking a sequence, the model randomly masks 15% of the tokens in the input then runs the entire masked sentence through the model and has to predict the masked tokens. This is comparable to the Cloze task in language modeling.
2. **Secondary Structure (SS)**: predicting the secondary structure of the `<mask>` token in the MLM task.
3. **Minimum Free Energy (MFE)**: predicting the minimum free energy of the 5’ UTR sequence.

### Training Data

The UTR-LM model was pre-trained on 5’ UTR sequences from three sources:

- **[Ensembl Genome Browser](https://ensembl.org)**: Ensembl is a genome browser for vertebrate genomes that supports research in comparative genomics, evolution, sequence variation and transcriptional regulation. UTR-LM used 5’ UTR sequences from 5 species: human, rat, mouse, chicken, and zebrafish, since these species have high-quality and manual gene annotations.
- **[Human 5′ UTR design and variant effect prediction from a massively parallel translation assay](https://doi.org/10.1038/s41587-019-0164-5)**: Sample et al. proposed 8 distinct 5' UTR libraries, each containing random 50 nucleotide sequences, to evaluate translation rules using mean ribosome loading (MRL) measurements.
- **[High-Throughput 5’ UTR Engineering for Enhanced Protein Production in Non-Viral Gene Therapies](https://doi.org/10.1038/s41467-021-24436-7)**: Cao et al. analyzed endogenous human 5’ UTRs, including data from 3 distinct cell lines/tissues: human embryonic kidney 293T (HEK), human prostate cancer cell (PC3), and human muscle tissue (Muscle).

UTR-LM preprocessed the 5’ UTR sequences in a 4-step pipeline:

1. removed all coding sequence (CDS) and non-5' UTR fragments from the raw sequences.
2. identified and removed duplicate sequences
3. truncated the sequences to fit within a range of 30 to 1022 bp
4. filtered out incorrect and low-quality sequences

Note [`RnaTokenizer`][multimolecule.RnaTokenizer] will convert "T"s to "U"s for you, you may disable this behaviour by passing `replace_T_with_U=False`.

### Training Procedure

#### Preprocessing

UTR-LM used masked language modeling (MLM) as one of the pre-training objectives. The masking procedure is similar to the one used in BERT:

- 15% of the tokens are masked.
- In 80% of the cases, the masked tokens are replaced by `<mask>`.
- In 10% of the cases, the masked tokens are replaced by a random token (different) from the one they replace.
- In the 10% remaining cases, the masked tokens are left as is.

#### Pre-training

The model was trained on two clusters:

1. 4 NVIDIA V100 GPUs with 16GiB memories.
2. 4 NVIDIA P100 GPUs with 32GiB memories.

## Citation

**BibTeX**:

```bibtex
@article {chu2023a,
	author = {Chu, Yanyi and Yu, Dan and Li, Yupeng and Huang, Kaixuan and Shen, Yue and Cong, Le and Zhang, Jason and Wang, Mengdi},
	title = {A 5{\textquoteright} UTR Language Model for Decoding Untranslated Regions of mRNA and Function Predictions},
	elocation-id = {2023.10.11.561938},
	year = {2023},
	doi = {10.1101/2023.10.11.561938},
	publisher = {Cold Spring Harbor Laboratory},
	abstract = {The 5{\textquoteright} UTR, a regulatory region at the beginning of an mRNA molecule, plays a crucial role in regulating the translation process and impacts the protein expression level. Language models have showcased their effectiveness in decoding the functions of protein and genome sequences. Here, we introduced a language model for 5{\textquoteright} UTR, which we refer to as the UTR-LM. The UTR-LM is pre-trained on endogenous 5{\textquoteright} UTRs from multiple species and is further augmented with supervised information including secondary structure and minimum free energy. We fine-tuned the UTR-LM in a variety of downstream tasks. The model outperformed the best-known benchmark by up to 42\% for predicting the Mean Ribosome Loading, and by up to 60\% for predicting the Translation Efficiency and the mRNA Expression Level. The model also applies to identifying unannotated Internal Ribosome Entry Sites within the untranslated region and improves the AUPR from 0.37 to 0.52 compared to the best baseline. Further, we designed a library of 211 novel 5{\textquoteright} UTRs with high predicted values of translation efficiency and evaluated them via a wet-lab assay. Experiment results confirmed that our top designs achieved a 32.5\% increase in protein production level relative to well-established 5{\textquoteright} UTR optimized for therapeutics.Competing Interest StatementThe authors have declared no competing interest.},
	URL = {https://www.biorxiv.org/content/early/2023/10/14/2023.10.11.561938},
	eprint = {https://www.biorxiv.org/content/early/2023/10/14/2023.10.11.561938.full.pdf},
	jourPre-trainingxiv}
}
```

## Contact

Please use GitHub issues of [MultiMolecule](https://github.com/DLS5-Omics/multimolecule/issues) for any questions or comments on the model card.

Please contact the authors of the [UTR-LM paper](https://doi.org/10.1101/2023.10.11.561938) for questions or comments on the paper/model.

## License

This model is licensed under the [AGPL-3.0 License](https://www.gnu.org/licenses/agpl-3.0.html).

```spdx
SPDX-License-Identifier: AGPL-3.0-or-later
```
