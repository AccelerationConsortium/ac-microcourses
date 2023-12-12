<!--- This is an auto-generated file. Please do not edit directly. Instead, edit
in course-data.yaml and run the `scripts/generate_overviews.py` file. --->

# 📊 AI and Materials Databases for Self-Driving Labs

Unleash the power of data science in the realm of self-driving laboratories. This remote, asynchronous course empowers you to apply data science concepts to materials discovery tasks. You'll create Bayesian optimization scripts using the Ax Platform, explore advanced optimization topics, and use the Honegumi template generator to create an advanced optimization setup for a materials discovery task. Additionally, you'll learn to share your findings by uploading datasets to FigShare, creating benchmark models with scikit-learn, and hosting models on HuggingFace.

![](./images/ax-repo/bo_1d_opt.gif)
*Animation of 1D Bayesian Optimization: A Gaussian Process surrogate model can be used with an acquisition function to seamlessly transition from exploration to optimization in noisy settings. Source: [https://ax.dev/docs/bayesopt.html](https://ax.dev/docs/bayesopt.html)*

## 🔑 Recommended Prerequisites

The **recommended prerequisite** for this course is Introduction to AI for Discovery using Self-driving Labs



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

Each module is intended to take approximately 2-3 hours, assuming that the recommended prerequisites have been met.

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

* - Multi-fidelity and multi-task optimization
  - * Cost-fidelity tradeoffs
    * Knowledge gradient
  - * Explain the effect of cost-fidelity tradeoffs on optimization
    * Explain when to use multi-fidelity vs. multi-task optimization
    * Assess the efficiency of expected improvement at fixed fidelities vs. knowledge gradient
    * Adapt a Bayesian optimization script to use a knowledge gradient

* - Benchmark datasets and models
  - * Benchmarks
    * Surrogate models
    * Random forest regression
    * FAIR data
    * Model deployment
    * APIs
  - * Explain the effect of noise on benchmarking tasks
    * Programatically upload a completed dataset to Figshare
    * Create a benchmark model with scikit-learn
    * Host a model on HuggingFace

```

## ⚖️ Course Assessments and Grading Schema

Each module will contain the following:<br><br><ul><li>🧭 A guided notebook tutorial (ungraded)</li><li>📓 A knowledge check (graded, 5 points)</li><li>🛠️ A mini project (graded, 10 points)</li></ul>

<div align="center">

[⬅️ Return to list of microcourses](../../index.md#microcourses)

</div>
