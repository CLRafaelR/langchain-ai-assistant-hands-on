Today, you are slated to deliver a succinct 20-minute talk on your recent research findings. You are in the process of creating Markdown-rendered slides, aiming to allocate roughly one minute per slide, culminating in an estimated total of 20 slides.

The following guidelines must be adhered to when composing your Markdown slides:

## Requirements """"""

### Formats

1. Prefix each slide's title with `##`, followed by an empty line preceding the body text. You must have at least 20 headers and its contents, since you have to create at least 20 slides.
2. Ensure slide titles accurately encapsulate the essence of your paper's content.
3. Include a minimum of three and a maximum of five key points per slide to thoroughly yet succinctly convey the information.
4. Where necessary, provide up to two supplementary explanations for each key point to elucidate further.

Example Markdown format for presentation slides:

```
## Introduction

- Key Point 1
  - Supplementary Explanation 1.1
  - Supplementary Explanation 1.2
- Key Point 2
  - Supplementary Explanation 2.1
  - Supplementary Explanation 2.2
- Key Point 3
- ...

## Materials and Methods

- Key Point 1
- Key Point 2
- Key Point 3
  - Supplementary Explanation 3.1
  - Supplementary Explanation 3.2

- ...

## Results

- Key Point 1
  - Supplementary Explanation 1.1
  - Supplementary Explanation 1.2
- Key Point 2
  - Supplementary Explanation 2.1
  - Supplementary Explanation 2.2
- Key Point 3
  - Supplementary Explanation 3.1
  - Supplementary Explanation 3.2
- ...

## Discussion

- Key Point 1
  - Supplementary Explanation 1.1
  - Supplementary Explanation 1.2
- Key Point 2
  - Supplementary Explanation 2.1
  - Supplementary Explanation 2.2
- Key Point 3
  - Supplementary Explanation 3.1
  - Supplementary Explanation 3.2
- ...

## Conclusion

- Key Point 1
- Key Point 2
- Key Point 3
- ...
```

1. You must explain all figures and tables in the original paper. For sections with such visuals, use a two-column format as demonstrated:

```
## Topics Requiring Visual Aids

::: {.columns}

:::: {.column}

- Key Point 1
  - Supplementary Explanation 1.1
  - Supplementary Explanation 1.2
- Key Point 2
  - Supplementary Explanation 2.1
  - Supplementary Explanation 2.2
- Key Point 3
  - Supplementary Explanation 3.1
  - Supplementary Explanation 3.2
- ...

::::

:::: {.column}

<Markdown syntax for inserting tables/figures>

![](/path/to/image)

| Example | Table |
|---------|-------|
| Data 1  | Data 2|

::::

:::
```

6. Cite research using @mentions as per the original paper, for example, `[@Paolazzi_etal2016; @Paolazzi_etal2017; @Paolazzi_etal2019]`.

### Contents

#### As a distinguished psycholinguist, explain all contents the most clearly

As a distinguished psycholinguist renowned for your scholarly contributions and engaging conference presentations, you adeptly cater to both novices in linguistics and those unacquainted with psychological experimentation, cognitive science, and Bayesian statistics. Your presentations deftly combine technical jargon with layman's terms to enhance understanding. Moreover, your discourse is meticulously crafted to meet the expectations of seasoned linguists by delving into complex, niche topics.

#### Based on the Paper

The key points and supplementary explanations must be derived exclusively from the original paper's content. Refrain from incorporating unsolicited suggestions, personal interpretations, or speculative comments about future research that are not present in the paper. Failure to authentically represent the paper's content will result in accusations of plagiarism and could permanently tarnish your academic publishing credentials. Ensure that your presentation strictly reflects the original paper.

For instance, it is unacceptable to mention "challenge to the previous research" without detailing how this research contrasts with prior studies. Instead, specify "challenge to the previous research on `<number>` points" and then clearly articulate these points through the corresponding number of supplementary explanations.

#### Focus on the Main Topic

You must cover:

- Predictions for reading times
- Predictions for accuracy
- Actual results of reading times and how it differs from the predictions
- Actual results of accuracy and how it differs from the predictions
- Conclusion

Use the figures and tables in the original paper for clearer explanation.

""""""

Now craft slides based on the Results, and Conclusion part from the original paper!

## Results, and Conclusion part from the original paper

"""
# Experiment: Self-paced reading task with comprehension question {#sec:expt-benefactive-cq}

## Predictions

### Predictions for the reading time

As argued by @Paolazzi_etal2019 and @Paolazzi_etal2021_CL, the shorter reading times for passives than for actives were attributed to differences in the predictability of upcoming words/phrases based on antecedents between passives and actives. In Japanese, a dative *=ni* marked NP may signal that the sentence is passive, and an accusative *=o* marked NP may signal that the sentence is active. Thus, if parsers of native Japanese speakers are actively predicting the upcoming elements based on antecedents, reading time differences between conditions can occur in    the verb (R5) and the modal immediately following the verb (R6), as shown in Table \@ref(tab:stimuli-1).

Meanwhile, a *=ni*~[dat]{.smallcaps}~-marked NP may not be sufficient to predict that a passive verb follows,  and  the facilitatory effect for passives may not occur. In this case,  the reading time would be longer in V-*te morau* passives than in V-*te ageru* actives. Since both active voice and passive voice were analytically marked using auxiliary verbs in this experiment, the longer reading time for passives can be attributed more to the processing load needed to resolve the mapping of the thematic roles and grammatical functions (i.e. diathesis processing) than morphological inflection in the passive verb [as found by @Yokoyama_etal2006]. A spill-over and/or delay of the processing load encountered in the verb region (R5) may also occur, resulting in longer reading times in passives for verbs (R5), for modal particles immediately following verbs (R6), or for both regions.

### Predictions for the comprehension question tasks

@Paolazzi_etal2021_CL [Experiment 3] found that if both active and passive were used in the questions about thematic relations (i.e. who did something to whom), the difference in accuracy between actives and passives was neutralised, as the question and its target sentence matched by being  in the passive voice and caused a facilitatory priming effect in favour of passive targets. Thus, a facilitatory effect caused by the voice match between the question and its target is also expected in Japanese.

## Results

### Reading time data {#reading-time-data}

As illustrated in Table \@ref(tab:tab-reading-time) (and Figure \@ref(fig:fig-ben-read-time-R1-R6) in \@ref(sec:reading-time-all-regions)), the median and mean reading time for V-*te morau* benefactive passive was longer than V-*te ageru* benefactive active in both verb (R5) and modal (R6) region. However, Bayes factors moderately favoured the alternative models and the presence of the effect of target voice only when the prior SDs were very constrained (i.e. $\text{SD} \leq 0.1$ for R5 and $\text{SD} \leq 0.025$ for R6) and thus yielded tiny estimates of the coefficient for the target voice, as demonstrated in Figure \@ref(fig:fig-R5-R6-table-fixef-voice). Furthermore, Bayes factors favoured the null models and the absence of the effect of the target voice when the prior SD was less constrained and thus yielded stable estimates of the coefficient for the target voice. This means that the voice contrast between V-*te morau* and V-*te ageru* had little impact on reading times.

```{=tex}
\begin{table}

\centering
\resizebox{\linewidth}{!}{
\begin{tabular}[t]{c>{\centering\arraybackslash}m{3.5em}>{\centering\arraybackslash}m{3.5em}>{\centering\arraybackslash}m{3.5em}>{\centering\arraybackslash}m{3.5em}}
\toprule
\multicolumn{1}{c}{} & \multicolumn{2}{c}{R5: Verb} & \multicolumn{2}{c}{R6: Modal particle} \\
\cmidrule(l{3pt}r{3pt}){2-3} \cmidrule(l{3pt}r{3pt}){4-5}
Target voice & Median & Mean & Median & Mean\\
\midrule
\makecell[t]{V-\textit{te ageru} (active)} & 808 & 1074.7 & 499 & 631.9\\
\makecell[t]{V-\textit{te morau} (passive)} & 909 & 1333.0 & 531 & 718.7\\
\bottomrule
\end{tabular}}
\caption{\label{tab:tab-reading-time}Median and mean reading time (ms) by condition}
\end{table}
```
(ref:cap-fig-ben-read-time-all-regions) Raw reading time for the verb
region (R5) and the modal particle region (R6); Thick bars and thin bars
indicate the 66% and 95% quantile intervals of data respectively, and
bullets indicate the median reading time.

```{=tex}
\begin{figure}[!htbp]

{\centering \includegraphics[width=1\linewidth]{figures/0-SPR-fig-R5-R6-table-fixef-voice-1} 

}

\caption{Change in estimate (with 95\% Credible Interval) and Bayes factor for target voice by prior SD in the region of verb (R5) and the modal (R6)}(\#fig:fig-R5-R6-table-fixef-voice)
\end{figure}
```
### Accuracy of comprehension questions

As Figure \@ref(fig:fig-accuracy-facet-cq-NP-order) illustrates, accuracy was lower for V-*te morau* passive targets than V-*te ageru* active targets. This is supported by strong evidence of $\text{BF}_{10}$ as prior SD increases, as shown in Figure \@ref(fig:fig-accuracy-table-fixef). Accuracy was lower for comprehension question whose NP order was NP1 $\to$ NP2 than for those whose NP order was NP2 $\to$ NP1, supported by strong evidence of $\text{BF}_{10}$. Moreover, when comprehension questions had NP1 $\to$ NP2 order, matching the voice between target sentences and their comprehension questions drastically increased the accuracy, both in V-*te ageru* actives and V-*te morau* passives. These voice matching effects were corroborated by the extreme evidence of $\text{BF}_{10}$. However, such voice matching effects were not supported in either V-*te ageru* actives or V-*te morau* passives with low $\text{BF}_{10}$ when comprehension questions had a NP2 $\to$ NP1 order.

(ref:cap-fig-accuracy-facet-cq-NP-order) Raw accuracy for the comprehension question by condition

```{=tex}
\begin{figure}[!htbp]

{\centering \includegraphics[width=1\linewidth]{figures/0-SPR-fig-accuracy-facet-cq-NP-order-1} 

}

\caption{(ref:cap-fig-accuracy-facet-cq-NP-order)}(\#fig:fig-accuracy-facet-cq-NP-order)
\end{figure}
```

```{=tex}
\begin{figure}[!htbp]

{\centering \includegraphics[width=1\linewidth]{figures/0-SPR-fig-accuracy-table-fixef-1} 

}

\caption{Change in estimate (with 95\% Credible Interval) and Bayes factor for factors by prior SD}(\#fig:fig-accuracy-table-fixef)
\end{figure}
```

# General discussion and conclusion {#sec:discussion}

## Comparable reading time difference between V-*te morau* benefactive passive and V-*te ageru* benefactive active

In the raw data, reading times for *V-te morau* passives were longer than *V-te ageru* actives. The current results differ from the results in English [@Paolazzi_etal2016; @Paolazzi_etal2017; @Paolazzi_etal2019] and in German [@Grillo_etal2019] showing that passives have numerically shorter reading times than actives. However,  Bayes factors did not clearly support either the presence or absence of the effect of voice on reading time difference. These findings contradict to the prediction derived from the previous research in SVO languages that the elements prior to the verb region (e.g. a *=ni*[dat]{.smallcaps}-marked NP in R4 in this experiment) may signal that the subsequent region and entire sentence is passive, leading to shorter reading times for passive compared to actives. Possible reasons for the lack of reading time differences could be due to sentence processing specific to V-*te morau* and V-*te ageru*.

Both V-*te morau* and V-*te ageru* overtly mark passive and active voice respectively, and they both analytically express voice in a similar morphological composition.  Therefore, it is possible that the same processing load and time were required for the actives as the passives.  In contrast, in the pair of V-$\emptyset$ active and V-(*r*)*are* passive, as well as in the pair of English active and *be* passive (*be* V.[pst.ptcp]{.smallcaps}), only the passive has a morphosyntactically complex marker.  Thus, only passives may tend to be more cognitively demanding, and this might have resulted in the clearer difference between active and passive in previous research. The manifestation of the processing load may differ when comparing the pair of V-*te morau* and V-*te ageru*,  and when comparing the pair V-(*r*)*are* passive and V-$\emptyset$ active, and the comparison of the former may not be measured by the reading times in this study.   Therefore, further research that examines other behavioural measurements is necessary. In experiments comparing the processing of V-(*r*)*are* passive and V-$\emptyset$ active, both morphological processing [Lexical decision task by @Yokoyama_etal2006] and processing involving syntax [picture-sentence matching task by @Kinno_etal2008; and @Tanaka_etal2017] showed activation of the left inferior frontal gyrus for V-(*r*)*are* passive. However, this alone does not tell us whether the left inferior frontal gyrus is more strongly activated by morphological processing (the internal process to form a verb base phrase/verb chunk) or syntactic processing (the whole VP/sentence level). It is not possible to determine whether the processing of the diathesis  or the voice  is more difficult. It is only with V-*te morau* and V-*te ageru*, which have a similar morphological processing, that it is possible to clarify the differences in brain activation on syntactic processing in the active and passive voice, after matching the morphological processing as much as possible.

## Accuracy

In general, accuracy in the comprehension questions targeting V-*te morau* passive was lower than those targeting V-*te ageru* active. Since V-*te morau* and V-*te ageru* share a similar morphological composition, syntactic factors---namely, the mapping of patient to grammatical subject in passives---are more likely to induce this accuracy difference than morphological factors. Moreover, the accuracy in comprehension questions targeting V-*te morau* passives was significantly improved by questions in V-(*r*)*are* passives, compared to those in actives. This replicates what @Paolazzi_etal2021_CL found in thier study of English passives, and suggests that V-*te morau* primes V-(*r*)*are*, facilitating the processing of V-(*r*)*are* and alleviating the cognitive load required to maintain and retrieve the representation of V-*te morau*. This priming further implies that the patientive beneficiaries in V-*te morau* benefactive passive and normal patients in V-(*r*)*are* passive could be represented and processed as one broad patientive macrorole in the native speakers' parser. 

Interestingly, accuracy for comprehension questions targeting V-*te ageru* active sharply decreased when the questions were in V-(*r*)*are* passive causing a voice mismatch.  This indicates that V-(*r*)*are* passive intervened post-interpretive process [i.e. memorising the contents of a sentence and using them to do other action, @Caplan_Waters1999], such as responding comprehension questions in our experiment, for V-*te ageru* active.   Unlike what has previously been considered, both passive and active  diathesis can possibly be prone to diathesis mismatch between the target and the question.

Moreover, a facilitating priming effect from V-*te morau* to V-(*r*)*are* was elicitable only when a V-*te morau* target and its question using V-(*r*)*are* have a same NP order (i.e. NP1 $\to$ NP2 order both in the targets and comprehension questions). 


# Conclusion and limitations {#sec:conclusion}

The Japanese analytical benefactive passive, V-*te morau*, is indeed more difficult to comprehend than its active counterpart V-*te ageru*, which was evident in accuracy in the comprehension questions, not reading times.   In our experiment, we aligned the morphological features of passive and active voices. Consequently, it is unsurprising that the reading time for passive sentences did not decrease compared to the active ones. This contrasts with earlier findings in English [@Paolazzi_etal2016; @Paolazzi_etal2017; @Paolazzi_etal2019] and German [@Grillo_etal2019].

Previous studies suggested that the verb region is read faster in passive constructions due to the stronger morphological signals indicating passivisation (e.g. copula verbs and PPs denoting the agent). In the current study, there existed a morphological signal in passive sentences in R3 (the second NP), specifically the agentive NP marked by the dative *=ni*, which differed from the patientive NP marked by the accusative *=o* in actives within the same region. Nonetheless, we found no reduction in reading times for the subsequent verb (R5) and modal particle (R6) regions in passives.

Hence, the morphological cues that facilitate passive reading, as reported in prior studies, might have limited impact in Japanese passives. Future work will address this possibility by comparing reading times between V-(*r*)*are* passives and V-$\emptyset$ actives.

Alternatively, this effect might be unobservable in experiments that control the morphological factors between passives and actives. For a more comprehensive understanding of this phenomenon, future research should replicate our results using languages in which pairs of passive-active constructions demonstrate an equipollent alternation, such as Finnish, Kafa, and Sinhala [@Zúñiga_Kittilä2019_book], akin to Japanese *V-te morau* and *V-te ageru*. Considering the relative scarcity of this alternation pattern from a typological perspective [@Zúñiga_Kittilä2019_book], such an approach would also contribute to a in-depth cross-linguistic validation in psycholinguistics. 

Furthermore, the improvement in accuracy for comprehension questions targeting V-*te morau* sentences with V-(*r*)*are* questions gave a new insight on the range of the patientive macrorole. This results suggests that patientive beneficiaries in V-*te morau* benefactive passive and normal patients in V-(*r*)*are* passive could be categorised under a unified patientive macrorole within the cognitive process of native speakers' parser.

However, the generalisability of this result may be subject to certain limitations. One such constraint is that the priming effect became apparent only when both a V-*te morau* target and its corresponding V-(*r*)*are* question maintained identical NP order. Consequently, one might raise a question regarding whether the observed facilitating priming effect from V-*te morau* to V-(*r*)*are* is attributable to the circumstance in which the NP denoting a non-agentive semantic role emerges as the syntactic subject in both constructions.

Nevertheless, the increase in accuracy observed when the questions targeting V-*te morau* were formulated as V-(*r*)*are* would not have occurred if these semantic roles were considered entirely distinct entities. Any such distinction would have resulted in interference between these two passive constructions, leading to a decrease in accuracy despite the same word order between the two consturctions. Future research will explore whether the current findings are rooted in the primability between the beneficiary of V-*te morau* and the patient of V-(*r*)*are*, by comparing the primability of these roles, as well as the primability between the beneficiary and a role that falls outside both the agentive and patientive macroroles, or between the patient and such a role.
"""

Now reformat the original paper to fit the presentation format as I instruct. Return the Markdown format only. 

Your answer: Take a deep breath. Let's think step by step.