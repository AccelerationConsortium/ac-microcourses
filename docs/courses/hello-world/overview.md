# 💡 Building a "Hello World" for self-driving labs

```{include} description.md
```

<!-- ```{raw} html
:file: clslab-light-slideshow.html
``` -->

![](./images/clslab-light.gif)
*Animated schematic diagram of the "Hello World" demo: A microcontroller controls the LEDs and reads sensor data. The difference between the target color and the measured color is fed into an adaptive experimentation algorithm, and the process repeats itself.*


## 🔑 Recommended Prerequisites <!-- alternative: ✅ -->

For participants to complete this course within the expected timeframe (approx. 20 hours), intermediate proficiency in Python programming is recommended.

```{include} ./hardware-note.md
```

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
* - Running the SDL demo
  - - Database management
    - Bayesian optimization
    - Microcontrollers
  - - Describe key terms and principles of self-driving labs
    - Preview an end-to-end self-driving lab
    - Upload software to a microcontroller
* - Blink and Read
  - - Microcontrollers
    - MicroPython
  - - Write MicroPython scripts
    - Use a microcontroller
* - Bayesian optimization
  - - Design of experiments
    - Data visualization
  - - Compare grid and random search vs. Bayesian optimization
    - Visualize optimization efficiency
* - Device communication
  - - MQTT
    - Broker/client
  - - Send commands to a microcontroller
    - Receive sensor data from a microcontroller
* - Logging data
  - - MongoDB
    - Database management
  - - Set up a MongoDB account and database
    - Upload data directly from microcontroller
* - Module integration
  - - Systems design
  - - Connect the pieces to complete the SDL demo
* - Lab sensor system
  - - Environmental sensors
  - - Continuously log temperature, humidity, vibration, etc.
```

<!-- Continuously log temperature, humidity, pressure, light, and accelerometer data -->

## ⚖️ Course Assessments and Grading Schema

Each module will contain the following:

1. 🧭 A guided notebook tutorial (ungraded)
2. 📓 A standalone notebook assignment (graded, 5 points)
3. 🛠️ A mini project (graded, 10 points)

The guided notebook tutorial is provided as a Jupyter notebook with embedded instructions and code snippets. The standalone notebook assignment is provided as a Jupyter notebook with instructions and partially filled code snippets. The mini project is an opportunity to directly apply the skills from the notebooks in an isolated environment within an interactive GitHub repository. Autograding of the notebook and mini project is performed via GitHub actions, and grades are automatically reported to GitHub Classroom. To see how that works, watch ["GitHub Classroom: How students complete assignments"](https://www.youtube.com/watch?v=ObaFRGp_Eko). Grades from GitHub Classroom are then periodically synced to Quercus, the University of Toronto's learning management system which is based on Instructure's open-source Canvas platform. A passing grade is considered 70% or greater.
