# 📈 Data science for self-driving labs

```{include} description.md
```

![](./images/ax-repo/bo_1d_opt.gif)

*Animation of 1D Bayesian Optimization: A Gaussian Process surrogate model can be used with an acquisition function to seamlessly transition from exploration to optimization in noisy settings. Source: [https://ax.dev/docs/bayesopt.html](https://ax.dev/docs/bayesopt.html)*

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

<!-- In intro, require Bayes opt video and user input for the different questions. This could be a GitHub discussion, comments in a PR, entry in the Canvas course, etc. -->

<!-- Mixed-variable optimization | Numerical parameters, categorical parameters |  -->

<!-- Module: Large language models for materials discovery @KevinJablonka can perhaps convert his 1-hr tutorial into this one -->

<!-- Noisy optimization | Bayesian optimization<br>Observation noise<br>Noisy expected improvement (NEI) | Explain the effect of observation noise on optimization<br>Compare the efficiency of expected improvement and NEI as a function of observation noise -->

<!-- NOTE: Moving workflow orchestration to robotics, with a covalent tutorial in hello world -->

## ⚖️ Course Assessments and Grading Schema

This course follows the same ["Course Assessments and Grading Schema"](https://ac-microcourses.readthedocs.io/en/latest/certificate-framework.html#course-assessments-and-grading-schema) format as *Building a "Hello World" for Self-Driving Labs*.
