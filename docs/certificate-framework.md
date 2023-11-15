# 🎓 Microcourse Details

Here, we provide details for the five core microcourses, including title, description, prerequisites, learning outcomes, skills, modules, and assessment formats.

## 💡 Building a "Hello World" for self-driving labs

```{include} courses/hello-world/description.md
```

### 🔑 Recommended Prerequisites <!-- alternative: ✅ -->

For participants to complete this course within the expected timeframe (approx. 20 hours), intermediate proficiency in Python programming is recommended.

### 🎯 Learning Outcomes

- Describe key terms and principles of self-driving labs
- Send commands and receive sensor data over WiFi using standard frameworks such as MQTT
- Store experiment configurations and results in a MongoDB database
- Implement software on a microcontroller to adjust device power and read sensor data
- Adapt a Bayesian optimization script from packages such as the Ax Platform to iteratively suggest new colors to try <!-- Bayes opt YouTube video here, in data science, or in both? EDIT: data science -->
- Implement workflow orchestration for a color experiment using packages such as Covalent
- Modify the system to record temperature, humidity, barometric pressure, and accelerometer measurements

### 🛠️ Competencies/Skills
- Basic self-driving lab literacy
- Database management
- Workflow orchestration
- Bayesian optimization
- Microcontrollers and sensors
- Hardware/software communication

### 🧩 Modules

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

### ⚖️ Course Assessments and Grading Schema

The course begins with an "Introduction to git and GitHub" based on [GitHub Education's starter course](https://github.com/education/github-starter-course). While optional and ungraded, it provides the necessary background to interact with later assignments. Each module thereafter consists of:

1. A guided notebook tutorial (ungraded)
2. A standalone notebook assignment (graded, 5 points)
3. A mini project (graded, 10 points)

The guided notebook tutorial is provided as a Jupyter notebook with embedded instructions and code snippets. The standalone notebook assignment is provided as a Jupyter notebook with instructions and partially filled code snippets. The mini project is an opportunity to directly apply the skills from the notebooks in an isolated environment within an interactive GitHub repository. Autograding of the notebook and mini project is performed via GitHub actions, and grades are automatically reported to GitHub Classroom. To see how that works, watch ["GitHub Classroom: How students complete assignments"](https://www.youtube.com/watch?v=ObaFRGp_Eko). Grades from GitHub Classroom are then periodically synced to Quercus, the University of Toronto's learning management system which is based on Instructure's open-source Canvas platform. A passing grade is considered 50% or greater.

## 📈 Data science for self-driving labs

Unleash the power of data science in the realm of self-driving laboratories. This remote, asynchronous course empowers you to apply data science concepts to materials discovery tasks. You'll create Bayesian optimization scripts using the Ax Platform, explore advanced optimization topics, and use the Honegumi template generator to create an advanced optimization setup for a materials discovery task. Additionally, you'll learn to share your findings by uploading datasets to FigShare, creating benchmark models with scikit-learn, and hosting models on HuggingFace.

### 🔑 Recommended Prerequisites

The **recommended prerequisite** for this course is ["Building a 'Hello World' for Self-Driving Labs"](https://ac-microcourses.readthedocs.io/en/latest/certificate-framework.html#building-a-hello-world-for-self-driving-labs).

### 🎯 Learning Outcomes

- Describe a materials discovery task using data science language and concepts
- Adapt a Bayesian optimization script to find an optimal chocolate chip cookie recipe
- Judiciously choose an advanced optimization setup that matches a materials discovery task
- Programatically upload a completed dataset to Figshare, create a benchmark model, and host it on HuggingFace

### 🛠️ Competencies/Skills
- Data science literacy
- Bayesian optimization
- Advanced Bayesian optimization
- Workflow orchestration
- Benchmarking

### 🧩 Modules

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

### ⚖️ Course Assessments and Grading Schema

This course follows the same ["Course Assessments and Grading Schema"](https://ac-microcourses.readthedocs.io/en/latest/certificate-framework.html#course-assessments-and-grading-schema) format as *Building a "Hello World" for Self-Driving Labs*.

## 🦾 Robotics for self-driving labs

Embark on a journey into the world of robotics and automation for self-driving laboratories. This asynchronous, remote course equips you with the skills to control peristaltic pumps, linear actuators, automated liquid handlers, and solid dispensers using a Pico W microcontroller, a motor driver, and the Covalent workflow orchestration package. You'll also learn to control mobile cobots using the Robot Operating System (ROS) framework and to perform spatial referencing and ID recognition via AprilTags and OpenCV. The course will conclude with a solid sample transfer workflow using Covalent, ROS, AprilTags, OpenCV, and a multi-axis robot.

### 🔑 Recommended Prerequisites

The **recommended prerequisite** for this course is ["Building a 'Hello World' for Self-Driving Labs"](https://ac-microcourses.readthedocs.io/en/latest/certificate-framework.html#building-a-hello-world-for-self-driving-labs).

### 🎯 Learning Outcomes

- Implement software to control a peristaltic pump via a microcontroller and a motor driver
- Build the "Digital Pipette" and implement software to control the linear actuator
- Perform liquid transfer between vials with an automated liquid handler (Jubilee or Opentrons)
- Demonstrate control of a mobile cobot using the robot operating system (ROS) framework
- Demonstrate spatial referencing and ID lookup by using OpenCV and AprilTags
- Use ROS, AprilTags, and a multi-axis robot to perform solid sample transfer

### 🛠️ Competencies/Skills

- Motor drivers
- Automated liquid handlers
- Robotic control
- Computer vision
- Automated solid handlers

### 🧩 Modules

```{list-table}
:header-rows: 1

* - Module Name
  - Topics
  - Learning Outcomes
* - Controlling pumps and pipettes
  - * Workflow orchestration
    * Microcontrollers
    * Peristaltic pumps
    * Linear actuators
    * Motor drivers
  - * Implement software to control a peristaltic pump via a microcontroller and a motor driver
    * Build the "Digital Pipette" and implement software to control the linear actuator
* - Automated liquid handlers
  - * Workflow orchestration
    * Jubilee
    * Opentrons
  - * Perform liquid transfer between vials with an automated liquid handler (Jubilee or Opentrons)
* - Mobile robotics
  - * ROS
  - * Demonstrate control of a mobile cobot using the Robot Operating System (ROS)
* - Computer vision
  - * OpenCV
    * AprilTags
  - * Demonstrate spatial referencing and ID lookup by using OpenCV and AprilTags
* - Solid sample transfer
  - * Workflow orchestration
    * ROS
    * AprilTags
    * Multi-axis robotics
  - * Use ROS, AprilTags, and a multi-axis robot to perform solid sample transfer
```

### ⚖️ Course Assessments and Grading Schema

This course follows the same ["Course Assessments and Grading Schema"](https://ac-microcourses.readthedocs.io/en/latest/certificate-framework.html#course-assessments-and-grading-schema) format as *Building a "Hello World" for Self-Driving Labs*.

## 🧑‍💻 Software development for self-driving labs

Elevate your software development skills in the context of self-driving laboratories. This asynchronous, remote course introduces software development concepts and best practices and productivity tools such as integrated development environments (IDEs) with VS Code, unit testing with pytest, continuous integration via GitHub actions, and documentation creation using Sphinx and Read the Docs. You'll also learn to deploy materials discovery campaigns on cloud servers or dedicated hardware and run offline simulations using cloud hosting. The recommended prerequisite for this course is *Building a "Hello World" for Self-Driving Labs*.

### 🎯 Learning Outcomes

- List software development best practices and corresponding benefits
- Identify productivity tools for developers that increase efficiency
- Write unit tests using tools such as pytest
- Create Python documentation using sphinx and rtd
- Implement continuous integration (CI) using tools such as GitHub actions
- Create a project template using PyScaffold
- Launch a cloud server or server on dedicated local hardware that runs a materials discovery campaign
- Run an offline simulation using cloud hosting

### 🛠️ Competencies/Skills

- Software development literacy
- Unit testing
- Documentation
- Compute hardware
- Cloud computing

### 🧩 Modules

```{list-table}
:header-rows: 1

* - Module Name
  - Topics
  - Learning Outcomes
* - Setting up VS Code
  - * IDEs
    * Miniconda
    * VS Code extensions
  - * Set up VS Code
    * Install Miniconda
    * Install VS Code extensions
* - Debugging in VS Code
  - * Print statements
    * Setting breakpoints
    * Inspecting variables
    * Stepping through code
    * Debug console
    * Debug configurations
  - * Use print statements to debug code
    * Set breakpoints
    * Inspect variables
    * Step through code
    * Use the debug console
    * Set up debug configurations
* - Unit testing
  - * pytest
    * Test result interpretation
    * Debugging
    * Test-driven development
  - * Explain the purpose of unit tests
    * Write unit tests for the light-mixing demo
    * Run and interpret unit tests to fix code
    * Explain test-driven development
* - Automated documentation
  - * Markdown
    * Documentation as code
    * Sphinx
    * Readthedocs
  - * Write documentation in Markdown
    * Explain what documentation as code means
    * Set up a readthedocs account and publish a readthedocs page
* - Continuous integration (CI)
  - * Continuous integration
    * GitHub actions
    * Unit tests
    * Documentation
  - * Explain the purpose of continuous integration
    * Set up a GitHub actions workflow
    * Run unit tests and documentation builds on GitHub actions
* - Project templates
  - * PyScaffold
    * Cookiecutter
    * Project initialization
    * Project adaptation
  - * Create a project template using PyScaffold
    * Add project content
* - Launching a free cloud server
  - * Serverless computing
    * PythonAnywhere
    * Deploying Applications
  - * Launch a free cloud server
    * Deploy a materials discovery campaign on a cloud server
* - On-demand cloud simulations
  - * Cloud computing
    * Setting up an AWS account
    * AWS Lambda
  - * Run an on-demand cloud simulation
    * Integrate a cloud simulation into a materials discovery campaign
```

<!-- Python packaging with PyPI | Packages<br>PyPI<br>pip<br>Twine | Explain the purpose of packages<br>Set up a PyPI account<br>Upload a package to PyPI -->
<!-- Using LLMs to enhance coding workflows via GitHub Copilot Chat | Understanding LLMs<br>GitHub Copilot Chat<br>Code Suggestions<br>Code Completions<br>Code Refactoring | Explain the purpose of LLMs<br>Explore the use of GitHub Copilot Chat -->

<!-- https://www.w3schools.com/aws/ -->

<!-- note that print statements (similarly cell evaluation outputs for notebooks) are an important beginner method of debugging -->

### ⚖️ Course Assessments and Grading Schema

This course follows the same ["Course Assessments and Grading Schema"](https://ac-microcourses.readthedocs.io/en/latest/certificate-framework.html#course-assessments-and-grading-schema) format as *Building a "Hello World" for Self-Driving Labs*.

## 🏢 AC training lab capstone project <!-- Alternative emoji: 🏗️ -->

Turn your self-driving lab expertise into a real-world project. During this course, you will propose, design, and build a self-driving laboratory at the AC training lab equipped with education- and research-grade equipment including liquid handlers, solid dispensers, Cartesian-axis systems, and mobile robotic arms. Prior to arrival, you'll create schematic figures, write white papers, and present your proposals to a team of scientists. During a week-long in-person experience, you'll implement your proposal and document your progress. After the visit, you will share your designs, data, and documentation to contribute to the public knowledge base.

### 🔑 Prerequisites

Due to the intensive nature of this course and to maximize the value to the participants, the **prerequisites** for this course are:

- 💡 [Building a "Hello World" for Self-Driving Labs](https://ac-microcourses.readthedocs.io/en/latest/certificate-framework.html#building-a-hello-world-for-self-driving-labs).
- 📈 [Data Science for Self-Driving Labs](https://ac-microcourses.readthedocs.io/en/latest/certificate-framework.html#data-science-for-self-driving-labs)
- 🦾 [Robotics for Self-Driving Labs](https://ac-microcourses.readthedocs.io/en/latest/certificate-framework.html#robotics-for-self-driving-labs)
- 🧑‍💻 [Software Development for Self-Driving Labs](https://ac-microcourses.readthedocs.io/en/latest/certificate-framework.html#software-development-for-self-driving-labs)

By completing these requirements, participants will be equipped to propose, design, and execute a capstone project at the AC Training Lab.

### 🎯 Learning Outcomes

- Propose a self-driving lab via a schematic figure
- Write a white paper for the self-driving laboratory
- Present the proposal to a team of scientists
- Design and execute a capstone project at the AC Training Lab
- Provide a project update with proposed next steps
- Share the designs, data, and documentation publicly

### 🛠️ Competencies/Skills

- Scientific communication
- Systems design
- Dissemination
- Interdisciplinary teamwork

### 🧩 Modules

```{list-table}
:header-rows: 1

* - Module Name
  - Topics
  - Learning Outcomes
* - Project proposal
  - * Figures
    * White papers
    * Presentations
  - * Propose a self-driving lab via a schematic figure
    * Write a white paper for the self-driving laboratory
    * Present the proposal to a team of scientists
* - Design and execution
  - * SDL design
    * Implementation
    * Documentation
  - * Design and execute the project at the AC training lab
    * Provide a project update with proposed next steps
* - Dissemination
  - * Project update
    * Knowledge sharing
    * Data and documentation
  - * Share the designs, data, and documentation publicly
```

### ⚖️ Course Assessments and Grading Schema

Performance in this course is assessed via rubrics that evaluate the quality of the proposal, design/build, and  stages. The proposal rubric evaluates the schematic figure, white paper, and presentation. The design rubric evaluates the design, implementation, and documentation. The build rubric evaluates the build, implementation, and documentation. Each module is worth 100 points.
