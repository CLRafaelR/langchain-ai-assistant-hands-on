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

- How statistical models were constructed (prior settings, and how to interpret Bayes Factors)
- Predictions on the experimental results

""""""

Now craft slides based on the Methods part from the original paper, since this must be explained in detail.

## Methods part from the original paper

"""
# Experiment: Self-paced reading task with comprehension question {#sec:expt-benefactive-cq}

### Data analysis

#### Data exclusion criteria

Since 55 participants participated or were suspected of participating in the experiment multiple times, their data were removed from our analyses. The data from 50 participants were also removed as the stimuli were not properly presented or were suspected of not being properly presented to them. Data from 2 participants were removed due to recording errors on the server. Data from 2 participants with overall accuracy for distractors is \<75% were removed from the final analysis, following @Paolazzi_etal2019. Ultimately, the data from 145 participants were eventually analysed.

In PCIbex, a trial proceeds to the last region with little or no reading in the middle, if the space key is held down during a trial instead of pressing it each time a region is read. In such a case, the reading time of each region tends to be recorded as around 35 ms.  Therefore, the reading times less than 50 ms were also excluded.


#### Statistical models

We fit Bayesian generalised mixed effect models with by-participants and by-items correlated varying intercept and varying slopes using `R` [@R-base]. We used `brms` package [@R-brms] for the model building, with the backend of `cmdstanr` [@R-cmdstanr] for the coefficient calculation, and with the backend of `rstan` [@R-rstan] to pass `stanfit` objects to `bridgesampling` [@R-bridgesampling] for the Bayes factor calculation. We fit every model using `brms::brm()` with 4 chains and 4 cores in parallel,  2000 warm-up and 50000 post-warm-up iterations, and a target mean acceptance probability $\delta = 0.9$ for the NUTS sampler. 

We calculated the Bayes factors for the alternative over the null model ($\text{BF}_{10}$) to test whether each explanatory variable had a non-null effect on the response variables.  For instance, to test the presence of voice effect (i.e. difference in reading time or accuracy between V-*te morau* versus V-*te ageru*), we compared an alternative model with the coefficient (parameter) of voice effect against a null model without that coefficient,  by calculating a $\text{BF}_{10}$. The $\text{BF}_{10}$ for voice effect larger than one indicates that the difference in voice affects the reading time or accuracy. On the other hand, the $\text{BF}_{10}$ less than one means that there is no effect of voice on the reading time or accuracy. Lee and Wagenmakers' criteria [-@BCM2013, derived from Jeffreys, ]  was used to determine the strength of the evidence for alternative models or null models:




```{=latex}
\renewcommand{\labelitemii}{}
%\renewcommand{\labelitemii}{\normalfont\bfseries \textendash}
```
-   Evidence for the alternative model
    -    Extreme
        evidence
    -   
        Very strong evidence
    -   
        Strong evidence
    -   
        Moderate evidence
    -   
        Anecdotal evidence
-   Evidence for the null model
    -   
        Anecdotal evidence
    -   
        Moderate evidence



```{=latex}
%\renewcommand{\labelitemii}{}
\renewcommand{\labelitemii}{\normalfont\bfseries \textendash}
```

Since the priors of both the explanatory variables and intercept may radically affect the computation of Bayes factors [See Section 15.3 of @PL-BDA2021], we calibrated those priors using prior predictive checks following @Schad_etal2020 and @Schad_etal2022.  To track changes in the values of coefficient and $\text{BF}_{10}$ depending on priors, we calculated $\text{BF}_{10}$ multiple times for each explanatory variable using normally-distributed priors with a mean of zero, but with different SDs, adapting the procedure of @Nicenboim_etal2020.

##### Reading time data {#sec:cq-reading-time}

Reading time was assumed to be log-normally distributed. The explanatory variables of interest, namely voice of the target, was sum-coded, with V-*te morau* benefactive passive coded as $1$ and V-*te ageru* benefactive passive coded as $-1$. The number of characters in the region and the absolute trial order were also added to the models as covariates. The absolute trial order is the order in which one target is presented among all stimuli including distractors. Both the number of characters in the region and the trial order are $z$-transformed, following @PL-BDA2021 [Section 9.2]. Since the number of characters differed by condition of voice (i.e. the between-item factor), there was no random slope of items for the factor.

According to prior predictive checks, we used normally-distributed priors for target voice with varying SD of 0.5, 0.25, 0.1, 0.075, 0.05, 0.025, 0.01, 0.0075, 0.005, 0.0025, and 0.001.  For other parameters, we used the priors summarised in Table \@ref(tab:priors-reading-time).

```{=tex}
\begin{table}[!bth]

\centering
\resizebox{\linewidth}{!}{
\begin{tabular}[t]{ccc}
\toprule
Coefficient & R5: Verb & R6: Modal particle\\
\midrule
Intercept & $\text{N}(6.8, 0.2)$ & $\text{N}(6.5, 0.2)$\\
Region length & $\text{N}(0, 0.1)$ & $\text{N}(0, 0.1)$\\
Trial order & $\text{N}(0, 0.1)$ & $\text{N}(0, 0.1)$\\
Scale parameter $\sigma$ & $\text{N}_{+}(0, 0.2)$ & $\text{N}_{+}(0, 0.3)$\\
\addlinespace[0.3em]
\multicolumn{3}{l}{\textbf{Parameters for random effects}}\\
\hspace{1em}SD $\tau$ & $\text{N}(0, 0.2)$ & $\text{N}(0, 0.1)$\\
\hspace{1em}Correlation parameter $\rho$ & $\text{LKJ}(\eta = 2)$ & $\text{LKJ}(\eta = 2)$\\
\bottomrule
\end{tabular}}
\caption{\label{tab:priors-reading-time}Priors decided according to prior predicative checks}
\end{table}
```
##### Accuracy of comprehension questions

We fit mixed effects logistic regressions to the accuracy data. The voice of the target was sum-coded, with V-*te morau* benefactive passive coded as $-1$ and V-*te ageru* benefactive passive coded as $1$. The NP order in comprehension questions was also sum-coded, with NP1 $\to$ NP2 (the same as the target) coded as $1$ and NP2 $\to$ NP1 (reversed from the target) coded as $-1$. The voice (mis)match effect  was coded using a nested sum contrast [@Schad_etal2020_contrasts], so that 1 is assigned if voice matches between target and question, as summarised in Table \@ref(tab:nested-sum-contrast). The $z$-transformed absolute trial order was also added to the models as a covariate.

According to prior predictive checks, we used normally-distributed priors for target voice with varying SD of 0.5, 0.25, 0.1, and 0.05. We used $\text{N}(1.3, 0.2)$ priors for intercepts, $\text{N}(0, 0.1)$ priors for the slopes, and LKJ priors with $\eta = 2$ for the correlation matrices.

```{=tex}
\begin{table}

\centering
\resizebox{\linewidth}{!}{
\begin{tabular}[t]{>{\centering\arraybackslash}m{4em}>{\centering\arraybackslash}m{4em}>{\centering\arraybackslash}m{5em}>{\centering\arraybackslash}m{5em}>{\centering\arraybackslash}m{5em}>{\centering\arraybackslash}m{5em}}
\toprule
\multicolumn{1}{c}{} & \multicolumn{1}{c}{} & \multicolumn{2}{c}{\makecell[c]{NP order in question\\(NP1 $\to$ NP2)}} & \multicolumn{2}{c}{\makecell[c]{NP order in question\\(NP2 $\to$ NP1)}} \\
\cmidrule(l{3pt}r{3pt}){3-4} \cmidrule(l{3pt}r{3pt}){5-6}
Target voice & Question voice & Voice match & Voice match & Voice match & Voice match\\
\midrule
 & V-$\emptyset$\newline (active) & 1 & 0 & 0 & 0\\

\multirow[t]{-2}{4em}{\centering\arraybackslash \parbox{4em}{\centering{}V-\textit{te}\newline \textit{ageru}\newline (active)}} & V-(\textit{r})\textit{are}\newline (passive) & -1 & 0 & 0 & 0\\
\cmidrule{1-6}
 & V-$\emptyset$\newline (active) & 0 & -1 & 0 & 0\\

\multirow[t]{-2}{4em}{\centering\arraybackslash \parbox{4em}{\centering{}V-\textit{te}\newline \textit{morau}\newline (passive)}} & V-(\textit{r})\textit{are}\newline (passive) & 0 & 1 & 0 & 0\\
\cmidrule{1-6}
 & V-$\emptyset$\newline (active) & 0 & 0 & 1 & 0\\

\multirow[t]{-2}{4em}{\centering\arraybackslash \parbox{4em}{\centering{}V-\textit{te}\newline \textit{ageru}\newline (active)}} & V-(\textit{r})\textit{are}\newline (passive) & 0 & 0 & -1 & 0\\
\cmidrule{1-6}
 & V-$\emptyset$\newline (active) & 0 & 0 & 0 & -1\\

\multirow[t]{-2}{4em}{\centering\arraybackslash \parbox{4em}{\centering{}V-\textit{te}\newline \textit{morau}\newline (passive)}} & V-(\textit{r})\textit{are}\newline (passive) & 0 & 0 & 0 & 1\\
\bottomrule
\end{tabular}}
\caption{\label{tab:nested-sum-contrast}Nested contrast coding for voice match}
\end{table}
```
"""

Now reformat the original paper to fit the presentation format as I instruct. Return the Markdown format only. 

Your answer: Take a deep breath. Let's think step by step.