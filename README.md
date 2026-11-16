# Somesh Mridha — Engineering Portfolio

A responsive engineering portfolio presenting my education, research, undergraduate projects, experience, and achievements through case studies, original figures, and an interactive research-results chart.

**[Visit the live portfolio →](https://someshmridhaofficial.netlify.app/)**

## What the website contains

- Three engineering case studies: LEO satellite OFDM Doppler estimation, reinforcement-learning-based PMSM control, and solar PV-fed wireless EV charging.
- Thirteen unaltered original project and research figures, with source captions and links to full-resolution images.
- An interactive LS/WLS Doppler-error chart and a downloadable CSV of 18 selected result pairs.
- Education at The University of Osaka and VIT Vellore, including current GPA and final CGPA.
- Internship, leadership, learning records, and competition achievements.
- A downloadable English résumé and professional contact links.
- English, Hindi, Bengali, Tamil, Japanese, and Sanskrit interfaces. English is the first-visit default; a visitor’s selection is remembered locally.
- Responsive layouts, keyboard-accessible controls, reduced-motion support, and print styles.

## Engineering projects

| Case study | Scope of the evidence |
| --- | --- |
| **Doppler estimation for LEO satellite OFDM** | Ongoing master’s research using fixed synthetic multipath channels. Six estimator variants, 18 channel/SNR conditions, and 3,600 paired simulation frames. Selected raw-WLS improvements at 0 dB do not establish consistent BER or across-SNR superiority. |
| **PMSM field-oriented control with reinforcement learning** | Undergraduate team project with Simulink implementation and PI/RL response plots. Different speed-reference profiles and inconsistent agent labels in the source report limit quantitative comparisons. |
| **Solar PV-fed wireless EV charging** | Undergraduate team project modelling the source, conversion, receiver, charging, backup, and load-detection chain. Results support simulated operating points; moving-vehicle charging and hardware performance were not validated. |

The repository contains the website, selected figures, and the displayed result subset. The original MATLAB/Simulink models, full research code, private transcripts, and complete university reports are outside this repository’s scope. Team projects are identified as such throughout the portfolio.

## Run locally

The website is plain HTML, CSS, and JavaScript. It needs no package installation or build step.

```sh
python -m http.server 8765 --directory dist
```

Open `http://localhost:8765/` in your browser. You can also open `dist/index.html` directly.

## Repository structure

```text
dist/
  index.html                 Page structure and fallback English content
  style.css                  Responsive layout and typography
  app.js                     Main interaction logic and English/Japanese text
  evidence.js                Evidence metadata and original case-study content
  languages.js               Compiled Hindi/Bengali/Tamil/Sanskrit content
  assets/
    evidence/                Original figures and selected research CSV
    logos/                   Organisation logos and source attribution
    Somesh_Mridha_Resume.pdf  English résumé
translations/                Editable Hindi/Bengali/Tamil/Sanskrit JSON
content-reference.json       English/Japanese reference for translation checks
build-languages.py           Translation validation and compilation
netlify.toml                 Static publishing directory
```

## Update content

1. Edit page structure in `dist/index.html`, English/Japanese copy in `dist/app.js`, and evidence metadata in `dist/evidence.js`.
2. Edit additional-language content in `translations/`.
3. Run `python build-languages.py` to validate and regenerate `dist/languages.js` after changing translation JSON.
4. Check JavaScript syntax with `node --check dist/app.js` and `node --check dist/languages.js`.
5. Preview the updated page and affected case studies before publishing.

Original figures retain their source text and numerical data; adjacent captions and descriptions are translated. The downloadable résumé remains in English and is labelled accordingly in every interface language. Website translations do not imply spoken proficiency in those languages.

## Publish

The current public website is hosted on Netlify. The included `netlify.toml` sets the publishing folder to `dist`. There is no build command. Connecting this repository to Netlify is a separate hosting setup step; creating the GitHub repository alone does not change the live website.

## Source and attribution

Engineering content comes from my undergraduate project reports, original research exports, and professional records. The website implementation and translations were prepared with AI assistance.

University, employer, course-provider, association, and competition logos retain their respective owners’ rights. Their source pages and asset provenance are recorded in `dist/assets/logos/sources.json`. Their use identifies the relevant institution or organiser.

## Contact

[Portfolio](https://someshmridhaofficial.netlify.app/) · [GitHub profile](https://github.com/someshmridha) · [LinkedIn](https://www.linkedin.com/in/somesh-mridha-7b853326b/) · [Email](mailto:someshmridha.official@gmail.com)
