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
* - Running the self-driving lab demo
  - - Database management
    - Bayesian optimization
    - Microcontrollers
    - Sensors
    - Device communication
  - - Describe key terms and principles of self-driving labs
    - Preview an end-to-end self-driving lab
    - Set up a MongoDB account and database
    - Set up a HiveMQ account and instance
    - Upload software to a microcontroller
* - Blink the LEDs and read sensor data
  - - Microcontrollers
    - Sensors
  - - Familiarize the MicroPython programming language
    - Send commands to a microcontroller
    - Receive sensor data from a microcontroller
* - Bayesian optimization for color matching
  - - Design of experiments
    - Bayesian optimization
    - Data visualization
  - - Compare grid and random search vs. Bayesian optimization
    - Visualize optimization efficiency
* - Hardware/software communication
  - - MQTT
    - Device communication
    - Host
    - Client
  - - Send commands to a microcontroller
    - Receive sensor data from a microcontroller
* - Logging data
  - - MongoDB
    - Database management
  - - Set up a MongoDB account and database
    - Upload data directly from microcontroller
* - Piecing the modules together
  - - Systems design
  - - Connect the pieces to complete the SDL demo
* - Convert to a lab sensor system
  - - Microcontrollers
    - Sensors
    - Device communication
    - Database management
  - - Continuously log temperature, humidity, pressure, light, and accelerometer data
```

<!-- In intro, require Bayes opt video and user input for the different questions. This could be a GitHub discussion, comments in a PR, entry in the Canvas course, etc. -->

<!-- Mixed-variable optimization | Numerical parameters, categorical parameters |  -->

<!-- Module: Large language models for materials discovery @KevinJablonka can perhaps convert his 1-hr tutorial into this one -->

<!-- Noisy optimization | Bayesian optimization<br>Observation noise<br>Noisy expected improvement (NEI) | Explain the effect of observation noise on optimization<br>Compare the efficiency of expected improvement and NEI as a function of observation noise -->

<!-- NOTE: Moving workflow orchestration to robotics, with a covalent tutorial in hello world -->

## ⚖️ Course Assessments and Grading Schema

This course follows the same ["Course Assessments and Grading Schema"](https://ac-microcourses.readthedocs.io/en/latest/certificate-framework.html#course-assessments-and-grading-schema) format as *Building a "Hello World" for Self-Driving Labs*.
