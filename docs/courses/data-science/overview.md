# 📈 Data science for self-driving labs

```{include} description.md
```

## 🔑 Recommended Prerequisites

The **recommended prerequisite** for this course is ["Building a 'Hello World' for Self-Driving Labs"](https://ac-microcourses.readthedocs.io/en/latest/certificate-framework.html#building-a-hello-world-for-self-driving-labs).

## 🎯 Learning Outcomes

- Describe a materials discovery task using data science language and concepts
- Adapt a Bayesian optimization script to find an optimal chocolate chip cookie recipe
- Judiciously choose an advanced optimization setup that matches a materials discovery task
- Programatically upload a completed dataset to Figshare, create a benchmark model, and host it on HuggingFace

## 🛠️ Competencies/Skills
- Data science literacy
- Bayesian optimization
- Advanced Bayesian optimization
- Workflow orchestration
- Benchmarking

## 🧩 Modules

```{list-table}
   :header-rows: 1

   * - Module Name
     - Topics
     - Learning Outcomes
   * - Gentle intro to Bayesian optimization
     - * Design of experiments
       * Quasi-random search methods
       * Bayesian optimization
       * Expected improvement (EI)
       * Ax Platform
       * Honegumi template generator
     - * Describe a materials discovery task using data science language and concepts
       * Adapt a Bayesian optimization script to find an optimal chocolate chip cookie recipe
   * - Multi-objective optimization
     - * Pareto fronts
       * Hypervolume
       * EHVI
       * Objective thresholds
     - * Explain the significance of a Pareto front
       * Compare simple scalarization with expected hypervolume improvement
       * Explore the effect of setting objective thresholds
   * - Constrained optimization
     - * Linear constraints
       * Nonlinear constraints
       * Compositional constraints
       * Order constraints
     - * Provide examples of materials discovery tasks with constraints
       * Adapt a Bayesian optimization script to include constraints
   * - High-dimensional optimization
     - * Curse of dimensionality
       * SAASBO
     - * Explain the curse of dimensionality
       * Compare the efficiency of expected improvement and SAASBO as a function of dimensionality
   * - Featurization
     - * Domain knowledge integration
       * Contextual variables
       * Predefined candidates
     - * Explain the advantages and disadvantages of featurization
       * Adapt a Bayesian optimization script to use predefined candidates with featurization
       * Adapt a Bayesian optimization script to use contextual variables
   * - Multi-fidelity optimization
     - * Cost-fidelity tradeoffs
       * Knowledge gradient
     - * Explain the effect of cost-fidelity tradeoffs on optimization
       * Assess the efficiency of expected improvement at fixed fidelities vs. knowledge gradient
       * Adapte a Bayesian optimization script to use a knowledge gradient
   * - Benchmark datasets and models
     - * Benchmarks
       * Surrogate models
       * Random forest regression
       * FAIR data
       * Model deployment
       * APIs
     - * Programatically upload a completed dataset to Figshare
       * Create a benchmark model with scikit-learn
       * Host a model on HuggingFace
```

<!-- Module Name | Topics | Learning Outcomes
--- | --- | ---
Gentle intro to Bayesian optimization | <ul><li>Design of experiments</li><li>Quasi-random search methods</li><li>Bayesian optimization</li><li>Expected improvement (EI)</li><li>Ax Platform</li><li>Honegumi template generator</li></ul> | <ul><li>Describe a materials discovery task using data science language and concepts</li><li>Adapt a Bayesian optimization script to find an optimal chocolate chip cookie recipe</li></ul>
Multi-objective optimization | <ul><li>Pareto fronts</li><li>Hypervolume</li><li>EHVI</li><li>Objective thresholds</li></ul> | <ul><li>Explain the significance of a Pareto front</li><li>Compare simple scalarization with expected hypervolume improvement</li><li>Explore the effect of setting objective thresholds</li></ul>
Constrained optimization | <ul><li>Linear constraints</li><li>Nonlinear constraints</li><li>Compositional constraints</li><li>Order constraints</li></ul> | <ul><li>Provide examples of materials discovery tasks with constraints</li><li>Adapt a Bayesian optimization script to include constraints</li></ul>
High-dimensional optimization | <ul><li>Curse of dimensionality</li><li>SAASBO</li></ul> | <ul><li>Explain the curse of dimensionality</li><li>Compare the efficiency of expected improvement and SAASBO as a function of dimensionality</li></ul>
Featurization | <ul><li>Domain knowledge integration</li><li>Contextual variables</li><li>Predefined candidates</li></ul> | <ul><li>Explain the advantages and disadvantages of featurization</li><li>Adapt a Bayesian optimization script to use predefined candidates with featurization</li><li>Adapt a Bayesian optimization script to use contextual variables</li></ul>
Multi-fidelity optimization | <ul><li>Cost-fidelity tradeoffs</li><li>Knowledge gradient</li></ul> | <ul><li>Explain the effect of cost-fidelity tradeoffs on optimization</li><li>Assess the efficiency of expected improvement at fixed fidelities vs. knowledge gradient</li><li>Adapte a Bayesian optimization script to use a knowledge gradient</li></ul>
Benchmark datasets and models | <ul><li>Benchmarks</li><li>Surrogate models</li><li>Random forest regression</li><li>FAIR data</li><li>Model deployment</li><li>APIs</li></ul> | <ul><li>Programatically upload a completed dataset to Figshare</li><li>Create a benchmark model with scikit-learn</li><li>Host a model on HuggingFace</li></ul> -->


<!-- In intro, require Bayes opt video and user input for the different questions. This could be a GitHub discussion, comments in a PR, entry in the Canvas course, etc. -->

<!-- Mixed-variable optimization | Numerical parameters, categorical parameters |  -->

<!-- Module: Large language models for materials discovery @KevinJablonka can perhaps convert his 1-hr tutorial into this one -->

<!-- Noisy optimization | Bayesian optimization<br>Observation noise<br>Noisy expected improvement (NEI) | Explain the effect of observation noise on optimization<br>Compare the efficiency of expected improvement and NEI as a function of observation noise -->

<!-- NOTE: Moving workflow orchestration to robotics, with a covalent tutorial in hello world -->

## ⚖️ Course Assessments and Grading Schema

This course follows the same ["Course Assessments and Grading Schema"](https://ac-microcourses.readthedocs.io/en/latest/certificate-framework.html#course-assessments-and-grading-schema) format as *Building a "Hello World" for Self-Driving Labs*.
