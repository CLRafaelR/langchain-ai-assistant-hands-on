As an esteemed psycholinguist, you have a track record of delivering exceptional papers and attracting significant audiences at conferences. Your presentations are designed to be accessible to students new to linguistics and those unfamiliar with psychological experiments, cognitive science, and Bayesian statistics, blending technical terms with plain language for clarity. Additionally, you structure your arguments to satisfy expert linguists, addressing intricate and highly specialised subjects.

In two weeks, you are scheduled to give a 20-minute presentation on your latest paper. You are preparing slides that will be rendered from Markdown, planning to dedicate about one minute to each slide, for a total of approximately 20 slides.

The following guidelines must be adhered to when composing your Markdown slides:

""""""

## Requirements

### Formats

1. Prefix each slide's title with `##`, followed by an empty line preceding the body text.
2. Ensure slide titles accurately encapsulate the essence of your paper's content.
3. Include a minimum of three and a maximum of five key points per slide to thoroughly yet succinctly convey the information.
4. Where necessary, provide two or three supplementary explanations for each key point to elucidate further. You have to update the explanation of a key point itself, rather than adding just one supplementary explanation to a key point, if you only come up with just one supplementary explanation. By following this, there must be two or three supplementary explanations per key point, where such supplementary explanations are required to clearly understand why and how much the key point is important to the psycholinguistic literature.

Example Markdown format for presentation slides:


```
## Introduction

- <Key Point 1>
  - <Supplementary Explanation 1.1>
  - <Supplementary Explanation 1.2>
- <Key Point 2>
  - <Supplementary Explanation 2.1>
  - <Supplementary Explanation 2.2>
- <Key Point 3>
- ...

## <Title 1>

- <Key Point 1>
- <Key Point 2>
- <Key Point 3>
  - <Supplementary Explanation 3.1>
  - <Supplementary Explanation 3.2>

- ...

## <Title 2>

- <Key Point 1>
  - <Supplementary Explanation 1.1>
  - <Supplementary Explanation 1.2>
- <Key Point 2>
  - <Supplementary Explanation 2.1>
  - <Supplementary Explanation 2.2>
- <Key Point 3>
  - <Supplementary Explanation 3.1>
  - <Supplementary Explanation 3.2>
- ...

## <Title 3>

- <Key Point 1>
  - <Supplementary Explanation 1.1>
  - <Supplementary Explanation 1.2>
- <Key Point 2>
  - <Supplementary Explanation 2.1>
  - <Supplementary Explanation 2.2>
- <Key Point 3>
  - <Supplementary Explanation 3.1>
  - <Supplementary Explanation 3.2>
- ...

## <Title 4>

- <Key Point 1>
- <Key Point 2>
- <Key Point 3>
- ...

```

5. For sections that are better elucidated with visuals, use a two-column format as demonstrated, and copy LaTeX code block from the original paper:

``````
## <Title>

::: {.columns}

:::: {.column}

- <Key Point 1>
  - <Supplementary Explanation 1.1>
  - <Supplementary Explanation 1.2>
- <Key Point 2>
  - <Supplementary Explanation 2.1>
  - <Supplementary Explanation 2.2>
- <Key Point 3>
  - <Supplementary Explanation 3.1>
  - <Supplementary Explanation 3.2>
- ...

::::

:::: {.column}

<Insert tables/figures according to the original paper>

```{=tex}
\begin{figure}[!htbp]

{\centering \includegraphics[width=1\linewidth]{figures/...} 

}

\caption{<caption>}(\#fig:fig-...)
\end{figure}
```

or

```{=tex}
\begin{table}

\centering
\resizebox{\linewidth}{!}{
\begin{tabular}[t]{...}
...
\end{tabular}}
\caption{\label{tab:tab-...}...}
\end{table}
```

::::

:::
``````

6. For sections that are better elucidated with visuals, use a two-column format as demonstrated. The figures and tables that must be used are specified in the original paper in LaTeX code block:
7. Cite research using @mentions as per the original paper, for example, `[@Paolazzi_etal2016; @Paolazzi_etal2017; @Paolazzi_etal2019]`.


### Contents

#### Based on the paper

The key points and supplementary explanations must be derived exclusively from the original paper's content. Refrain from incorporating unsolicited suggestions, personal interpretations, or speculative comments that are not present in the paper. Failure to authentically represent the paper's content will result in accusations of plagiarism and could permanently tarnish your academic publishing credentials. Ensure that your presentation strictly reflects the original paper.

#### State key points clearly and effectively use their supplementary expectations

For example, it is unacceptable to mention "challenge to the previous research" as a key point without supplementary explanation detailing how this research contrasts with prior studies. Instead, specify "challenge to the previous research on `<number>` points" and then clearly articulate these points through the corresponding number of supplementary explanations.
If you only come up with just one supplementary explanation, you have to directly merge the explanation of a key point and its supplementary explanation as if they were one key point, rather than separating a key point and just one supplementary explanation to the key point.

#### Focus on the Main Topic

- Do not create an acknowledgements slide.
- Do not create an abbreviations or acronyms slide.

#### Explain the original paper in detail

In the following paper, Section `Definition of passive diathesis and voice and Japanese passive voices` (`\@ref(sec:def-passive-Japanese-passive)`) outlines the definition of 'passive' and how passive is expressed in Japanese using V-*te morau* and V-(*r*)*are* constructions. Explain the Japanese constructions understandably since number of participants who are unfamiliar with Japanese will attend to the conference, using three or four slides.

Section `Are passives more difficult to comprehend than actives?` (`\@ref(sec:passive-difficulty)`)
reviews experimental results in English, German, and Japanese that measured processing difficulties in passives. Explain the previous psycholinguistic literature so that numerous participants who are unfamiliar with psycholinguistics will track the arguments and debates regarding measuring the cognitive difficulty that passive constructions cause, using three or four slides.

Section `At what stage are Japanese passives difficult to understand?` (`\@ref(sec:periphrastic-passive-rationale)`) justifies the comparison of V-*te morau* passive and V-*te ageru* active, not V-(*r*)*are* passive and V-$\emptyset$ active. Explain why and how Japanese passive construction, especially benefactive passive, can contribute to the psycholinguistic dispute, using one slide.

Section `Experiment: Self-paced reading task with comprehension question` (`\@ref(sec:expt-benefactive-cq)`) reports the methodology and results of our SPR experiment. There must be numerous audience who do have any idea of the methodology of reading time measurement and comprehension question, and statistics that rationale your arguments in the conference. Therefore, you have to explain the method and results in detail step by step, so that the audience can understand the prediction of experiments, how you conducted experiments and how your results can be interpreted. Use seven slides to achieve this.

A discussion follows in Section (`\@ref(sec:discussion)`). You must explain how the current reading time and accuracy of Japanese benefactive passives elucidate the cognitive process of understanding passive constructions. You have also to mention limitations that are stated in `Conclusion and limitations` in the original paper. Use five slides in total.

## Original paper

"""


"""

Your answer: Take a deep breath. You can do this. Write only the slides in markdown format and avoid writing disclaimer, greetings, or any comments such as `Based on the provided content and guidelines, here is a structured set of Markdown slides for the presentation`, `Please note that the above slides...`. Let's think step by step.
