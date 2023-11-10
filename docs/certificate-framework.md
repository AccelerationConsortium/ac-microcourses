# 📜 Autonomous Systems for Discovery Certificate

While advanced materials hold the potential to improve our lives and our world, conventional methods of discovery are slow and expensive. "Self-driving" (i.e., autonomous) laboratories have the power to radically fast-track materials discovery—from an average of 20 years and $100 million to as little as 1 year and $1 million. This paradigm shift requires highly qualified personnel and multidisciplinary expertise. While extensive degree-based training can provide deep expertise in a single field, formal education options which provide needed cross-disciplinary skills are unavailable. This certificate will address this gap with training that introduces self-driving labs, provides deeper dives into data science, robotics, and software development, and facilitates a capstone project. Each course will contain a series of hands-on guided tutorials and coding exercises for participants to adapt and apply what they've learned.

## 🎯 Certificate Learning Outcomes

- Recreate a color-matching self-driving lab from scratch using RGB LEDs, a color sensor, a microcontroller, and Python
- Write a Python script that uses AI to iteratively suggest next experiments
- Use a database backend to programatically upload and retrieve materials data
- Write a Python script to orchestrate experimental and computational workflows
- Leverage state-of-the-art software development tools and implement best practices
- Develop, defend, and execute a project proposal for a self-driving lab

## 🎓 Courses

As an introduction, participants will design and build a "Hello World" for self-driving labs using physical hardware and Python. The certificate also provides deeper dives into data science, robotics, and software development. After completing these deeper dives, participants will be able to write a Python script that uses AI to iteratively suggest next experiments, use a database backend to programatically upload and retrieve materials data, and write a Python script to orchestrate experimental and computational workflows. Likewise, participants will be able to leverage state-of-the-art software development tools using best practices while implementing solutions to maximize efficiency and minimize frustration.

The certificate culminates in a project proposal which participants will develop, defend, and execute at the Acceleration Consortium's in-person training facility. This experience will provide familiarity with education- and research-grade equipment including liquid handlers, solid dispensers, Cartesian-axis systems, mobile robotic arms, a vertical lift module, and synthesis and characterization modules. Together, the learning outcomes of this certificate will provide a familiarity with the terminology, principles, and tools required for the highly interdisciplinary teams necessary to build state-of-the-art self-driving labs.

### 👋 Building a "Hello World" for self-driving labs

Discover the essential principles of self-driving laboratories (SDLs) by building a "Hello World" SDL from scratch. In this asynchronous, remote course, you will build a self-driving color matcher using dimmable LEDs and a light sensor. This introduction will help you implement hardware/software communication via MQTT, database integration via MongoDB, microcontroller programming with a Raspberry Pi Pico W, and optimization via the Adaptive Experimentation (Ax) Platform. The course will conclude with an expansion of the demo to the research-relevant task of continuously logging temperature, humidity, pressure, light, and accelerometer data. For participants to complete this course within the expected timeframe (15-20 hours), intermediate proficiency in Python programming is recommended.

#### 🎯 Learning Outcomes <!-- Merge LO and C/S? into table? Maybe not - implies one-to-one correspondence between the lines-->

- Describe key terms and principles of self-driving labs
- Use MQTT to send commands and receive sensor data over WiFi
- Store experiment configurations and results in a MongoDB database
- Implement software on a microcontroller to adjust device power and read sensor data
- Adapt a script for the Adaptive Experimentation (Ax) Platform to iteratively suggest new colors to try
- Modify the system to record temperature, humidity, barometric pressure, and accelerometer measurements

#### 🛠️ Competencies/Skills
- Basic self-driving lab literacy
- Database management
- Workflow orchestration
- Bayesian optimization
- Microcontrollers and sensors
- Hardware/software communication

#### 🧩 Modules
Module Name | Topics | Learning Outcomes
---- | ---- | ----
Running the self-driving lab demo | Database management, Bayesian optimization, microcontrollers, sensors, device communication |
Blink the LEDs and read sensor data | Microcontrollers, sensors |
| Bayesian optimization for color matching | Bayesian optimization |
| Hardware/software communication using MQTT | Device communication |
| Logging data to MongoDB | Database management |
| Bring it altogether | Systems design |
| Convert the demo to an all-purpose lab sensor system | Microcontrollers, sensors, device communication, database management |

### 📈 Data science for self-driving labs

Unleash the power of data science in the realm of self-driving laboratories. This remote, asynchronous course empowers you to apply data science concepts to materials discovery tasks. You'll create Bayesian optimization scripts using the Ax Platform, explore advanced optimization topics, and use the Honegumi template generator to create an advanced optimization setup for a materials discovery task. Additionally, you'll learn to share your findings by uploading datasets to FigShare, creating benchmark models with scikit-learn, and hosting models on HuggingFace. The recommended prerequisite for this course is "Building a 'Hello World' for Self-Driving Labs".

#### 🎯 Learning Outcomes

- Describe a materials discovery task using data science language and concepts
- Adapt a Bayesian optimization script to find an optimal chocolate chip cookie recipe
- Judiciously choose an advanced optimization setup that matches a materials discovery task
- Adapt a Covalent script to implement workflow orchestration for chocolate chip cookie optimization
- Programatically upload a completed dataset to figshare, create a benchmark model, and host it on HuggingFace or similar

#### 🛠️ Competencies/Skills
- Data science literacy
- Bayesian optimization
- Advanced Bayesian optimization
- Workflow orchestration
- Benchmarking

#### 🧩 Modules

Module Name | Topics | Learning Outcomes
--- | --- | ---
A gentle introduction to Bayesian optimization | Design of experiments, quasi-random search methods, Bayesian optimization, expected improvement, Ax Platform, Honegumi template generator |
Multi-objective optimization | Bayesian optimization, Pareto fronts, expected hypervolume improvement, domain knowledge integration through objective thresholds |
Constrained optimization | Bayesian optimization, linear constraints, nonlinear constraints, compositional constraints, order constraints |
High-dimensional optimization | Bayesian optimization, curse of dimensionality, sparse axis-aligned subspaces |
Featurization | Bayesian optimization, domain knowledge integration, contextual variables, predefined candidates |
Multi-fidelity optimization | Bayesian optimization, cost-fidelity tradeoffs, knowledge gradient acquisition function |
Creating benchmarks using Figshare, scikit-learn, and HuggingFace | Benchmarks, surrogate models, random forest regression, FAIR data, model deployment, application programming interfaces (APIs) |

<!-- Mixed-variable optimization | Numerical parameters, categorical parameters |  -->

<!-- Module: Large language models for materials discovery @KevinJablonka can perhaps convert his 1-hr tutorial into this one -->

<!-- NOTE: Moving workflow orchestration to robotics, with a covalent tutorial in hello world -->

### 🦾 Robotics for self-driving labs

Embark on a journey into the world of robotics and automation for self-driving laboratories. This asynchronous, remote course equips you with the skills to control peristaltic pumps, linear actuators, automated liquid handlers, and solid dispensers using a Pico W microcontroller, a motor driver, and the Covalent workflow orchestration package. You'll also learn to control mobile cobots using the Robot Operating System (ROS) framework and to perform spatial referencing and ID recognition via AprilTags and OpenCV. The course will conclude with a solid sample transfer workflow using Covalent, ROS, AprilTags, OpenCV, and a multi-axis robot. The recommended prerequisite for this course is "Building a 'Hello World' for Self-Driving Labs".

#### 🎯 Learning Outcomes

- Implement software to control a peristaltic pump via a microcontroller and a motor driver
- Build the "Digital Pipette" and implement software to control the linear actuator
- Perform liquid transfer between vials with an automated liquid handler (Jubilee or Opentrons)
- Demonstrate control of a mobile cobot using the robot operating system (ROS) framework
- Demonstrate spatial referencing and ID lookup by using OpenCV and AprilTags
- Use ROS, AprilTags, and a multi-axis robot to perform solid sample transfer

#### 🛠️ Competencies/Skills

- Motor drivers
- Automated liquid handlers
- Robotic control
- Computer vision
- Automated solid handlers

#### 🧩 Modules
Module Name | Topics | Learning Outcomes
---- | ---- | ----
Controlling pumps and pipettes | Workflow orchestration, microcontrollers, peristaltic pumps, linear actuators, motor drivers |
Automated liquid handlers | Workflow orchestration, Jubilee, Opentrons |
Mobile robotics | The Robot Operating System (ROS)
Computer vision | OpenCV, AprilTags |
Solid sample transfer | Workflow orchestration, ROS, AprilTags, multi-axis robot |

### 🧑‍💻 Software development for self-driving labs

Elevate your software development skills in the context of self-driving laboratories. This asynchronous, remote course introduces software development concepts and best practices and productivity tools such as integrated development environments (IDEs) with VS Code, unit testing with pytest, continuous integration via GitHub actions, and documentation creation using Sphinx and Read the Docs. You'll also learn to deploy materials discovery campaigns on cloud servers or dedicated hardware and run offline simulations using AWS. The recommended prerequisite for this course is "Building a 'Hello World' for Self-Driving Labs".

#### 🎯 Learning Outcomes

- List software development best practices and corresponding benefits
- Identify productivity tools for developers that increase efficiency
- Use pytest to write unit tests and use them with continuous integration via GitHub actions
- Create Python documentation using sphinx and rtd
- Launch a cloud server or server on dedicated local hardware that runs a materials discovery campaign
- Run an offline simulation using AWS

#### 🛠️ Competencies/Skills

- Software development literacy
- Unit testing
- Documentation
- Compute hardware
- Cloud computing

#### 🧩 Modules

Module Name | Topics | Learning Outcomes
---- | ---- | ----
Setting up VS Code | Integrated development environments (IDEs), miniconda, VS Code extensions |
Debugging in VS Code | Setting breakpoints, inspecting variables, stepping through code, debug console, debug configurations |
Automated unit testing with pytest | Writing test cases, running tests, interpreting test results, fixing tests, test-driven development |
Automated documentation with Sphinx and Readthedocs | Understanding Documentation, Sphinx Basics, Readthedocs Integration, Autodoc, RestructuredText (RST) Syntax, Hosting Documentation |
Using LLMs to enhance coding workflows via GitHub Copilot Chat | Understanding LLMs, GitHub Copilot Basics, Code Suggestions, Code Completions, Code Refactoring |
Launching a free cloud server with PythonAnywhere | Serverless computing, PythonAnywhere Basics, Deploying Applications |
Offline simulations with AWS | Cloud computing, setting up an AWS account, AWS Lambda |  <!-- https://www.w3schools.com/aws/ -->

### 🏢 AC training lab capstone project <!-- Alternative emoji: 🏗️ -->

Turn your self-driving lab expertise into a real-world project. During this course, you will propose, design, and build a self-driving laboratory at the AC training lab. Prior to arrival, you'll create schematic figures, write white papers, and present your proposals to a team of scientists. During a week-long in-person experience, you'll implement your proposal, document your progress, share designs and data, and contribute to the public knowledge base. The prerequisites for this course are "Building a 'Hello World' for Self-Driving Labs", "Data Science for Self-Driving Labs", "Robotics for Self-Driving Labs", and "Software Development for Self-Driving Labs".

#### 🎯 Learning Outcomes

- Propose a self-driving lab via a schematic figure
- Write a white paper for the self-driving laboratory
- Present the proposal to a team of scientists
- Design and build the proposed self-driving laboratory at the AC training lab
- Provide a project update with proposed next steps
- Share the designs, data, and documentation publicly

#### 🛠️ Competencies/Skills

- Scientific communication
- Systems design
- Knowledge sharing
- Interdisciplinary teamwork

#### 🧩 Modules

Module Name | Topics | Learning Outcomes
---- | ---- | ----
Project proposal | Figures, white papers, presentations |
Design and build | Self-driving lab design, implementation, documentation |
Dissemination | Project update, knowledge sharing, public data and documentation |
