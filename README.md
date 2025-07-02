## Statistical Analysis of Old Norse Eddic Poetry

This digital humanities project analyzed recurring alliterative collocations in Old Norse eddic poetry to distinguish deliberate poetic devices from chance occurrences. The corpus comprises approximately 12,000 verses of mostly anonymous mythological and legendary poetry composed in medieval Scandinavia and associated colonies. Working as a Stanford CESTA fellow with classics postdoc James Parkhouse and intern Poojit Hegde, I developed the computational framework to process and analyze these medieval texts.

### Project Context and Motivation

Old Norse poetic meter operates on alliterating stressed syllables per line rather than fixed syllable counts, creating frequent combinations of alliterating words. Similar to modern English expressions like "hearth and home" or "life and limb," these collocations carry rhetorical resonances beyond semantic meaning, offering insights into the aesthetics and worldviews of medieval composers and audiences. However, with finite words beginning with any letter, some combinations could recur by coincidence. The project used statistical testing to identify which alliterative combinations appeared more frequently than chance would predict, indicating deliberate poetic devices.

Due to time constraints, this proof-of-concept focused on one important manuscript (the Codex Regius) comprising roughly half the total corpus.

### Technical Implementation

**Data Compilation and Cleaning:**
The analysis began with manual compilation of alliterating stresses from each verse in the corpus. I developed comprehensive data cleaning procedures to handle corrupt verses with defective meter or indecipherable meaning resulting from centuries of manuscript transmission, while lemmatizing inflected forms to root forms for consistent analysis.

**Data Processing Pipeline:**
Built automated systems using Python to process the cleaned manuscript data across 29 poems:
- **Lemmatization and Normalization**: Developed algorithms to strip formatting artifacts and consolidate word variants, creating standardized root forms 
- **Alliteration Classification**: Implemented rule-based logic distinguishing simple consonant alliteration, vowel alliteration (treating all vowels as equivalent), and complex Nordic consonant clusters ('sk', 'sp', 'st' as distinct units)
- **Frequency Analysis**: Created counting algorithms tracking consolidated root frequencies across the corpus

**Co-occurrence Matrix Generation:**
Developed automated systems to generate contingency tables for all possible word pairs within alliterative lines, systematically identifying joint occurrences, single-word appearances, and absences to create comprehensive 2x2 contingency tables for statistical testing.

**Statistical Analysis:**
Implemented Fisher's exact test using SciPy to evaluate the independence of two variables given their observed distribution. The pipeline generated contingency tables for each collocation with frequency ≥2, performed mass statistical testing, and applied conservative Bonferroni correction to establish a significance threshold of p = 0.00006.

**Data Visualization:**
Created network representations using NetworkX with Jaccard similarity coefficients, where node sizes reflect word frequency and edge weights represent co-occurrence strength. Began experimenting with Gephi visualizations treating each significant collocate as the focal node of an ego network.

### Results

The analysis identified 77 collocations meeting the conservative significance threshold, including highly significant pairs like "vreiðr-vega" (angry-fight, p < 0.00001), "regin-rök" (gods-doom, p < 0.00001), and "skjöldungr-sköp" (prince-fate, p < 0.002). These findings provide quantitative evidence for deliberate formulaic techniques spanning multiple poems, suggesting established poetic formulas rather than coincidental combinations.

The computational approach revealed patterns that traditional literary analysis had recognized qualitatively but never measured systematically, providing a foundation for further literary-critical analysis of these combinations' poetic functions.
