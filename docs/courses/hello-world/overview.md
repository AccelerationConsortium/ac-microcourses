# 💡 Building a "Hello World" for self-driving labs

```{include} description.md
```

## 🔑 Recommended Prerequisites <!-- alternative: ✅ -->

For participants to complete this course within the expected timeframe (approx. 20 hours), intermediate proficiency in Python programming is recommended.

## 🎯 Learning Outcomes

- Describe key terms and principles of self-driving labs
- Send commands and receive sensor data over WiFi using standard frameworks such as MQTT
- Store experiment configurations and results in a MongoDB database
- Implement software on a microcontroller to adjust device power and read sensor data
- Adapt a Bayesian optimization script from packages such as the Ax Platform to iteratively suggest new colors to try <!-- Bayes opt YouTube video here, in data science, or in both? EDIT: data science -->
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
* - Intro to Git and GitHub (optional)
  - - Git
    - GitHub
    - The GitHub flow
    - GitHub terminology
  - - Set up a GitHub account
    - Clone a GitHub repository
    - Create a GitHub issue
    - Create a GitHub pull request
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

## ⚖️ Course Assessments and Grading Schema

The course begins with an "Introduction to git and GitHub" based on [GitHub Education's starter course](https://github.com/education/github-starter-course). While optional and ungraded, it provides the necessary background to interact with later assignments. Each module thereafter consists of:

1. A guided notebook tutorial (ungraded)
2. A standalone notebook assignment (graded, 5 points)
3. A mini project (graded, 10 points)

The guided notebook tutorial is provided as a Jupyter notebook with embedded instructions and code snippets. The standalone notebook assignment is provided as a Jupyter notebook with instructions and partially filled code snippets. The mini project is an opportunity to directly apply the skills from the notebooks in an isolated environment within an interactive GitHub repository. Autograding of the notebook and mini project is performed via GitHub actions, and grades are automatically reported to GitHub Classroom. To see how that works, watch ["GitHub Classroom: How students complete assignments"](https://www.youtube.com/watch?v=ObaFRGp_Eko). Grades from GitHub Classroom are then periodically synced to Quercus, the University of Toronto's learning management system which is based on Instructure's open-source Canvas platform. A passing grade is considered 50% or greater.
