

<!--- WARNING: THIS IS AN AUTO-GENERATED FILE. DO NOT EDIT DIRECTLY. Instead,
edit in docs/course-data.yaml and run the `scripts/generate_overviews.py` file
or modify src/ac_microcourses/overview.md.jinja. --->

# 📊 Data Science: Course Overview


```{note}
:class: margin
[Registration is live](https://learn.utoronto.ca/programs-courses/courses/4131-ai-and-materials-databases-self-driving-labs)! Course quizzes and grades are available at https://q.utoronto.ca/.
```


Unleash the power of data science in the realm of self-driving laboratories. This remote, asynchronous course empowers you to apply data science concepts to materials discovery tasks. You'll create Bayesian optimization scripts, explore advanced optimization topics, and adapt templates to create an advanced optimization setup for a materials discovery task. Topics will include multi-objective, constrained, high-dimensional, multi-fidelity, batch, asynchronous, and domain-aware Bayesian optimization. Additionally, you'll learn to share your findings by uploading datasets to a data repository, creating benchmark models, and hosting models on data science platforms.


```{margin}
*Animation of 1D Bayesian Optimization: A Gaussian Process surrogate model can be used with an acquisition function to seamlessly transition from exploration to optimization in noisy settings. Source: [https://ax.dev/docs/bayesopt.html](https://ax.dev/docs/bayesopt.html)*
```


![](./images/ax-repo/bo_1d_opt.gif)


## 🔑 Prerequisites



The **recommended prerequisite** for this course is Introduction to AI for Discovery using Self-driving Labs


## 🎯 Learning Outcomes


- Describe and categorize a materials discovery task using data science language and concepts

- Customize a Bayesian optimization script to systematically identify the optimal chocolate chip cookie recipe, demonstrating practical application of optimization techniques

- Evaluate and select an advanced optimization setup that is best suited for a specific materials discovery task, showcasing critical analysis and decision-making skills

- Develop and execute a program to upload a dataset to a public database, construct a benchmark model, and deploy it online, illustrating proficiency in data sharing and model hosting



## 🛠️ Competencies/Skills


- Data science literacy

- Bayesian optimization

- Advanced Bayesian optimization

- Workflow orchestration

- Benchmarking



## 🧩 Modules

Each module is intended to take approximately 3-4 hours, assuming that the recommended prerequisites have been met.

```{list-table}
:header-rows: 1

* - Module Name
  - Topics
  - Learning Outcomes

* - 2.0 Orientation
  - * Git
    * GitHub
    * Version control
    * GitHub Classroom
    * Codespaces
  - * Describe the purpose of Git and GitHub
    * Create a GitHub account and a repository
    * Commit, push, and pull changes
    * Run a unit test and fix a simple Python function
    * Define continuous integration

* - 2.1 Single-objective
  - * Design of experiments
    * Quasi-random search methods
    * Bayesian optimization (BO)
    * Expected improvement (EI)
    * Ax Platform
    * Honegumi template generator
  - * Describe a materials discovery task using data science language and concepts
    * Adapt a Bayesian optimization script to find an optimal chocolate chip cookie recipe

* - 2.2 Multi-objective
  - * Pareto fronts
    * Hypervolume
    * qNEHVI
    * Objective thresholds
  - * Explain the significance of a Pareto front
    * Compare simple scalarization with expected hypervolume improvement
    * Explore the effect of setting objective thresholds

* - 2.3 Batch Optimization
  - * Conditioning
    * Batch optimization
    * Asynchronous optimization
    * Parallelism
  - * Explain the effect of parallelism on optimization efficiency in terms of wall time and resource utilization
    * Explain what conditioning is in the context of batch and asynchronous BO
    * Adapt a Bayesian optimization script to use batch optimization
    * Adapt a Bayesian optimization script to use asynchronous optimization

* - 2.4 Featurization
  - * Domain knowledge integration
    * Contextual variables
    * Predefined candidates
  - * Explain the advantages and disadvantages of featurization
    * Adapt a Bayesian optimization script to use predefined candidates with featurization
    * Adapt a Bayesian optimization script to use contextual variables

* - 2.5 Multi-task
  - * Multi-task optimization
    * Cost-fidelity tradeoffs
  - * Explain the effect of cost-fidelity tradeoffs on optimization
    * Explain when to use multi-fidelity vs. multi-task optimization vs. contextual optimization
    * Adapt a Bayesian optimization script to leverage data from a related task

* - 2.6 Benchmarking
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

<p>Each student is required to complete various quizzes and GitHub Classroom assignments. The course is structured into an orientation module followed by several modules. The course is graded on a pass/fail basis with 70% as the threshold for passing. Here is the breakdown of the points for each part of the course:</p><ul><li>🧭 Orientation Module: Worth 15 points.</li><li>📚 Modules 1-6: Each includes:<ul><li>🧭 A guided notebook tutorial (ungraded)</li><li>📓 A knowledge check (graded, 5 points)</li><li>🛠️ A GitHub Classroom assignment (graded, 10 points*)</li></ul></li></ul><p>*The final module's GitHub Classroom assignment is worth 30 points.</p><p>Note that partial points are available on certain assignments.</p>


## 👤 Course developer(s)


- Sterling Baird, PhD Materials Science and Engineering (Acceleration Consortium)
