<!--- This is an auto-generated file. Please do not edit directly. Instead, edit
in course-data.yaml and run the `scripts/generate_overviews.py` file. --->

# 💡 Introduction to AI for Discovery using Self-driving Labs

Self-driving laboratories (SDLs) incorporate AI and automation into scientific laboratories to speed up the discovery of new materials for applications such as clean energy and cancer drugs. Discover the essential principles of SDLs by building a 'Hello World' SDL from scratch. In this asynchronous, remote course, you will build a self-driving color matcher using dimmable LEDs and a light sensor. This introduction will help you implement hardware/software communication, database integration, microcontroller programming, and Bayesian optimization. Each of these are important components of an SDL, and you will get a taste of these in the course modules. In the final module, you will piece together the individual components to create your very own SDL demo. This introductory course will prepare you for deeper dives in data science, robotics, software development, and system design in later microcourses.

![](./images/clslab-light.gif)
Animated schematic diagram of the 'Hello World' demo: A microcontroller controls the LEDs and reads sensor data. The difference between the target color and the measured color is fed into an adaptive experimentation algorithm, and the process repeats itself.

## 🔑 Recommended Prerequisites


```{include} ./hardware-note.md
```

For participants to complete this course within the expected timeframe (approx. 20 hours), beginner proficiency in Python programming is recommended.




## 🎯 Learning Outcomes


- Describe key terms and principles of self-driving labs
- Send commands and receive sensor data over WiFi using standard frameworks such as MQTT
- Store experiment configurations and results in databases such as MongoDB
- Implement software on a microcontroller such as Raspberry Pi Pico W to adjust device power and read sensor data
- Adapt a Bayesian optimization script from packages such as the Ax Platform to iteratively suggest new experiments to try
- Integrate the individual SDL components to orchestrate the full 'Hello World' workflow

## 🛠️ Competencies/Skills


- Basic self-driving lab literacy
- Microcontrollers and sensors
- Bayesian optimization
- Hardware/software communication
- Database management
- Workflow orchestration

## 🧩 Modules

The orientation modules are intended to be completed in under one hour in total. The modules after are intended to take approximately 2-3 hours each, assuming that the recommended prerequisites from above have been met.

```{list-table}
:header-rows: 1

* - Module Name
  - Topics
  - Learning Outcomes

* - 0. Orientation
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

* - 1. Running the SDL demo
  - * Database management
    * Bayesian optimization
    * Microcontrollers
  - * Describe key terms and principles of self-driving labs
    * Preview an end-to-end self-driving lab
    * Upload software to a microcontroller

* - 2. Blink and Read
  - * Microcontrollers
    * MicroPython
  - * Write MicroPython scripts
    * Use a microcontroller

* - 3. Bayesian optimization
  - * Design of experiments
    * Bayesian optimization
    * Data visualization
  - * Adapt a Bayesian optimization script to perform color-matching
    * Compare Bayesian optimization with other search methods
    * Visualize optimization efficiency

* - 4. Device communication
  - * MQTT
    * Broker/client
  - * Send commands to a microcontroller
    * Receive sensor data from a microcontroller

* - 5. Data logging
  - * MongoDB
    * Database management
  - * Set up a MongoDB account and database
    * Upload data directly from microcontroller
    * Extract and collate data from database

* - 6. Module integration
  - * Systems design
  - * Describe how individual components of an SDL can be integrated
    * Perform system-level debugging and troubleshooting
    * Conduct a full SDL experimental campaign

```

## ⚖️ Course Assessments and Grading Schema

Each module will contain the following:<br><br><ul><li>🧭 A guided notebook tutorial (ungraded)</li><li>📓 A knowledge check (graded, 5 points)</li><li>🛠️ A mini project (graded, 10 points*)</li></ul><br><br>*The final module's project is worth 30 points.

<div align="center">

[⬅️ Return to list of microcourses](../../index.md#microcourses)

</div>
