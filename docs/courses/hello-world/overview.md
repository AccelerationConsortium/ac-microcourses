# 💡 Introduction to AI for Discovery using Self-driving Labs

Discover the essential principles of self-driving laboratories (SDLs) by building a 'Hello World' SDL from scratch. In this asynchronous, remote course, you will build a self-driving color matcher using dimmable LEDs and a light sensor. This introduction will help you implement hardware/software communication via MQTT, database integration via MongoDB, microcontroller programming with a Raspberry Pi Pico W, and optimization via the Adaptive Experimentation (Ax) Platform. The course will conclude with an expansion of the demo to the research-relevant task of continuously logging temperature, humidity, pressure, light, and accelerometer data.

![](./images/clslab-light.gif)
Animated schematic diagram of the 'Hello World' demo: A microcontroller controls the LEDs and reads sensor data. The difference between the target color and the measured color is fed into an adaptive experimentation algorithm, and the process repeats itself.

## 🔑 Recommended Prerequisites

For participants to complete this course within the expected timeframe (approx. 20 hours), intermediate proficiency in Python programming is recommended.



## 🎯 Learning Outcomes


- Describe key terms and principles of self-driving labs
- Send commands and receive sensor data over WiFi using standard frameworks such as MQTT
- Store experiment configurations and results in a MongoDB database
- Implement software on a microcontroller to adjust device power and read sensor data
- Adapt a Bayesian optimization script from packages such as the Ax Platform to iteratively suggest new colors to try
- Implement workflow orchestration for a color experiment using packages such as Covalent
- Modify the system to record temperature, humidity, barometric pressure, and accelerometer measurements

## 🛠️ Competencies/Skills


- Basic self-driving lab literacy
- Database management
- Workflow orchestration
- Bayesian optimization
- Microcontrollers and sensors
- Hardware/software communication

## 🧩 Modules

```{list-table}
:header-rows: 1

* - Module Name
  - Topics
  - Learning Outcomes

* - Intro to Git and GitHub
  - * Git
    * GitHub
    * Version control
  - * Describe the purpose of Git and GitHub
    * Create a GitHub account
    * Create a repository
    * Clone a repository
    * Commit changes
    * Push changes
    * Pull changes

* - Intro to GitHub Classroom Assignments
  - * GitHub Classroom
    * Codespaces
    * pytest
    * Python modules
    * GitHub actions
  - * Run a unit test
    * Fix a simple Python function
    * Define continuous integration

* - Running the SDL demo
  - * Database management
    * Bayesian optimization
    * Microcontrollers
  - * Describe key terms and principles of self-driving labs
    * Preview an end-to-end self-driving lab
    * Upload software to a microcontroller

* - Blink and Read
  - * Microcontrollers
    * MicroPython
  - * Write MicroPython scripts
    * Use a microcontroller

* - Bayesian optimization
  - * Design of experiments
    * Data visualization
  - * Compare grid and random search vs. Bayesian optimization
    * Visualize optimization efficiency

* - Device communication
  - * MQTT
    * Broker/client
  - * Send commands to a microcontroller
    * Receive sensor data from a microcontroller

* - Logging data
  - * MongoDB
    * Database management
  - * Set up a MongoDB account and database
    * Upload data directly from microcontroller

* - Module integration
  - * Systems design
  - * Connect the pieces to complete the SDL demo

* - Lab sensor system
  - * Environmental sensors
  - * Continuously log temperature, humidity, vibration, etc.

```

## ⚖️ Course Assessments and Grading Schema

Each module will contain the following:<br><br><ul><li>🧭 A guided notebook tutorial (ungraded)</li><li>📓 A knowledge check (graded, 5 points)</li><li>🛠️ A mini project (graded, 10 points)</li></ul>

<div align="center">

[⬅️ Return to list of microcourses](../../index.md#microcourses)

</div>
