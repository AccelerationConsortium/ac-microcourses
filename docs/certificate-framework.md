# Microcourses

Here, we provide details for the five core microcourses, including title, description, learning outcomes, skills, and modules.

## 💡 Building a "Hello World" for self-driving labs

Discover the essential principles of self-driving laboratories (SDLs) by building a "Hello World" SDL from scratch. In this asynchronous, remote course, you will build a self-driving color matcher using dimmable LEDs and a light sensor. This introduction will help you implement hardware/software communication via MQTT, database integration via MongoDB, microcontroller programming with a Raspberry Pi Pico W, and optimization via the Adaptive Experimentation (Ax) Platform. The course will conclude with an expansion of the demo to the research-relevant task of continuously logging temperature, humidity, pressure, light, and accelerometer data. For participants to complete this course within the expected timeframe (15-20 hours), intermediate proficiency in Python programming is recommended.

### 🎯 Learning Outcomes <!-- Merge LO and C/S? into table? Maybe not - implies one-to-one correspondence between the lines-->

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

<!-- I'm not sure I like the module name/topics/LO table format. Perhaps a module name as a subheading -->

### 🧩 Modules

Module Name | Topics | Learning Outcomes
---- | ---- | ----
Running the self-driving lab demo | <ul><li>Database management</li><li>Bayesian optimization</li><li>Microcontrollers</li><li>Sensors</li><li>Device communication</li></ul> | <ul><li>Describe key terms and principles of self-driving labs</li><li>Preview an end-to-end self-driving lab</li><li>Set up a MongoDB account and database</li><li>Set up a HiveMQ account and instance</li><li>Upload software to a microcontroller</li></ul>
Blink the LEDs and read sensor data | <ul><li>Microcontrollers</li><li>Sensors</li></ul> | <ul><li>Familiarize the MicroPython programming language</li><li>Send commands to a microcontroller</li><li>Receive sensor data from a microcontroller</li></ul>
Bayesian optimization for color matching | <ul><li>Design of experiments</li><li>Bayesian optimization</li><li>Data visualization</li></ul> | <ul><li>Compare grid and random search vs. Bayesian optimization</li><li>Visualize optimization efficiency</li></ul>
Hardware/software communication | <ul><li>MQTT</li><li>Device communication</li><li>Host</li><li>Client</li></ul> | <ul><li>Send commands to a microcontroller</li><li>Receive sensor data from a microcontroller</li></ul>
Logging data | <ul><li>MongoDB</li><li>Database management</li></ul> | <ul><li>Set up a MongoDB account and database</li><li>Upload data directly from microcontroller</li></ul>
Piecing the modules together | <ul><li>Systems design</li></ul> | <ul><li>Connect the pieces to complete the SDL demo</li></ul>
Convert to a lab sensor system | <ul><li>Microcontrollers</li><li>Sensors</li><li>Device communication</li><li>Database management</li></ul> | <ul><li>Continuously log temperature, humidity, pressure, light, and accelerometer data</li></ul>

## 📈 Data science for self-driving labs

Unleash the power of data science in the realm of self-driving laboratories. This remote, asynchronous course empowers you to apply data science concepts to materials discovery tasks. You'll create Bayesian optimization scripts using the Ax Platform, explore advanced optimization topics, and use the Honegumi template generator to create an advanced optimization setup for a materials discovery task. Additionally, you'll learn to share your findings by uploading datasets to FigShare, creating benchmark models with scikit-learn, and hosting models on HuggingFace. The recommended prerequisite for this course is "Building a 'Hello World' for Self-Driving Labs".

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

Module Name | Topics | Learning Outcomes
--- | --- | ---
Gentle intro to Bayesian optimization | <ul><li>Design of experiments</li><li>Quasi-random search methods</li><li>Bayesian optimization</li><li>Expected improvement (EI)</li><li>Ax Platform</li><li>Honegumi template generator</li></ul> | <ul><li>Describe a materials discovery task using data science language and concepts</li><li>Adapt a Bayesian optimization script to find an optimal chocolate chip cookie recipe</li></ul>
Multi-objective optimization | <ul><li>Pareto fronts</li><li>Hypervolume</li><li>EHVI</li><li>Objective thresholds</li></ul> | <ul><li>Explain the significance of a Pareto front</li><li>Compare simple scalarization with expected hypervolume improvement</li><li>Explore the effect of setting objective thresholds</li></ul>
Constrained optimization | <ul><li>Linear constraints</li><li>Nonlinear constraints</li><li>Compositional constraints</li><li>Order constraints</li></ul> | <ul><li>Provide examples of materials discovery tasks with constraints</li><li>Adapt a Bayesian optimization script to include constraints</li></ul>
High-dimensional optimization | <ul><li>Curse of dimensionality</li><li>SAASBO</li></ul> | <ul><li>Explain the curse of dimensionality</li><li>Compare the efficiency of expected improvement and SAASBO as a function of dimensionality</li></ul>
Featurization | <ul><li>Domain knowledge integration</li><li>Contextual variables</li><li>Predefined candidates</li></ul> | <ul><li>Explain the advantages and disadvantages of featurization</li><li>Adapt a Bayesian optimization script to use predefined candidates with featurization</li><li>Adapt a Bayesian optimization script to use contextual variables</li></ul>
Multi-fidelity optimization | <ul><li>Cost-fidelity tradeoffs</li><li>Knowledge gradient</li></ul> | <ul><li>Explain the effect of cost-fidelity tradeoffs on optimization</li><li>Assess the efficiency of expected improvement at fixed fidelities vs. knowledge gradient</li><li>Adapte a Bayesian optimization script to use a knowledge gradient</li></ul>
Benchmark datasets and models | <ul><li>Benchmarks</li><li>Surrogate models</li><li>Random forest regression</li><li>FAIR data</li><li>Model deployment</li><li>APIs</li></ul> | <ul><li>Programatically upload a completed dataset to Figshare</li><li>Create a benchmark model with scikit-learn</li><li>Host a model on HuggingFace</li></ul>

<!-- In intro, require Bayes opt video and user input for the different questions. This could be a GitHub discussion, comments in a PR, entry in the Canvas course, etc. -->

<!-- Mixed-variable optimization | Numerical parameters, categorical parameters |  -->

<!-- Module: Large language models for materials discovery @KevinJablonka can perhaps convert his 1-hr tutorial into this one -->

<!-- Noisy optimization | Bayesian optimization<br>Observation noise<br>Noisy expected improvement (NEI) | Explain the effect of observation noise on optimization<br>Compare the efficiency of expected improvement and NEI as a function of observation noise -->

<!-- NOTE: Moving workflow orchestration to robotics, with a covalent tutorial in hello world -->

## 🦾 Robotics for self-driving labs

Embark on a journey into the world of robotics and automation for self-driving laboratories. This asynchronous, remote course equips you with the skills to control peristaltic pumps, linear actuators, automated liquid handlers, and solid dispensers using a Pico W microcontroller, a motor driver, and the Covalent workflow orchestration package. You'll also learn to control mobile cobots using the Robot Operating System (ROS) framework and to perform spatial referencing and ID recognition via AprilTags and OpenCV. The course will conclude with a solid sample transfer workflow using Covalent, ROS, AprilTags, OpenCV, and a multi-axis robot. The recommended prerequisite for this course is *Building a "Hello World" for Self-Driving Labs*.

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
Module Name | Topics | Learning Outcomes
---- | ---- | ----
Controlling pumps and pipettes | <ul><li>Workflow orchestration</li><li>Microcontrollers</li><li>Peristaltic pumps</li><li>Linear actuators</li><li>Motor drivers</li></ul> | <ul><li>Implement software to control a peristaltic pump via a microcontroller and a motor driver</li><li>Build the "Digital Pipette" and implement software to control the linear actuator</li></ul>
Automated liquid handlers | <ul><li>Workflow orchestration</li><li>Jubilee</li><li>Opentrons</li></ul> | <ul><li>Perform liquid transfer between vials with an automated liquid handler (Jubilee or Opentrons)</li></ul>
Mobile robotics | <ul><li>ROS</li></ul> | <ul><li>Demonstrate control of a mobile cobot using the Robot Operating System (ROS)</li></ul>
Computer vision | <ul><li>OpenCV</li><li>AprilTags</li></ul> | <ul><li>Demonstrate spatial referencing and ID lookup by using OpenCV and AprilTags</li></ul>
Solid sample transfer | <ul><li>Workflow orchestration</li><li>ROS</li><li>AprilTags</li><li>Multi-axis robotics</li></ul> | <ul><li>Use ROS, AprilTags, and a multi-axis robot to perform solid sample transfer</li></ul>

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

Module Name | Topics | Learning Outcomes
---- | ---- | ----
Setting up VS Code | <ul><li>IDEs</li><li>Miniconda</li><li>VS Code extensions</li></ul> | <ul><li>Set up VS Code</li><li>Install Miniconda</li><li>Install VS Code extensions</li></ul>
Debugging in VS Code | <ul><li>Print statements</li><li>Setting breakpoints</li><li>Inspecting variables</li><li>Stepping through code</li><li>Debug console</li><li>Debug configurations</li></ul> | <ul><li>Use print statements to debug code</li><li>Set breakpoints</li><li>Inspect variables</li><li>Step through code</li><li>Use the debug console</li><li>Set up debug configurations</li></ul>
Unit testing| <ul><li>pytest</li><li>Test result interpretation</li><li>Debugging</li><li>Test-driven development</li></ul> | <ul><li>Explain the purpose of unit tests</li><li>Write unit tests for the light-mixing demo</li><li>Run and interpret unit tests to fix code</li><li>Explain test-driven development</li></ul>
Automated documentation | <ul><li>Markdown</li><li>Documentation as code</li><li>Sphinx</li><li>Readthedocs</li></ul> | <ul><li>Write documentation in Markdown</li><li>Explain what documentation as code means</li><li>Set up a readthedocs account and publish a readthedocs page</li></ul>
Continuous integration (CI) | <ul><li>Continuous integration</li><li>GitHub actions</li><li>Unit tests</li><li>Documentation</li></ul> | <ul><li>Explain the purpose of continuous integration</li><li>Set up a GitHub actions workflow</li><li>Run unit tests and documentation builds on GitHub actions</li></ul>
Project templates | <ul><li>PyScaffold</li><li>Cookiecutter</li><li>Project initialization</li><li>Project adaptation</li></ul> | <ul><li>Create a project template using PyScaffold</li><li>Add project content</li></ul>
Launching a free cloud server | <ul><li>Serverless computing</li><li>PythonAnywhere</li><li>Deploying Applications</li></ul> | <ul><li>Launch a free cloud server</li><li>Deploy a materials discovery campaign on a cloud server</li></ul>
On-demand cloud simulations | <ul><li>Cloud computing</li><li>Setting up an AWS account</li><li>AWS Lambda</li></ul> | <ul><li>Run an on-demand cloud simulation</li><li>Integrate a cloud simulation into a materials discovery campaign</li></ul>

<!-- Python packaging with PyPI | Packages<br>PyPI<br>pip<br>Twine | Explain the purpose of packages<br>Set up a PyPI account<br>Upload a package to PyPI -->
<!-- Using LLMs to enhance coding workflows via GitHub Copilot Chat | Understanding LLMs<br>GitHub Copilot Chat<br>Code Suggestions<br>Code Completions<br>Code Refactoring | Explain the purpose of LLMs<br>Explore the use of GitHub Copilot Chat -->

<!-- https://www.w3schools.com/aws/ -->

<!-- note that print statements (similarly cell evaluation outputs for notebooks) are an important beginner method of debugging -->

## 🏢 AC training lab capstone project <!-- Alternative emoji: 🏗️ -->

Turn your self-driving lab expertise into a real-world project. During this course, you will propose, design, and build a self-driving laboratory at the AC training lab equipped with education- and research-grade equipment including liquid handlers, solid dispensers, Cartesian-axis systems, and mobile robotic arms. Prior to arrival, you'll create schematic figures, write white papers, and present your proposals to a team of scientists. During a week-long in-person experience, you'll implement your proposal and document your progress. After the visit, you will share your designs, data, and documentation to contribute to the public knowledge base. The prerequisites for this course are *Building a "Hello World" for Self-Driving Labs*, *Data Science for Self-Driving Labs*, *Robotics for Self-Driving Labs*, and *Software Development for Self-Driving Labs*.

### 🎯 Learning Outcomes

- Propose a self-driving lab via a schematic figure
- Write a white paper for the self-driving laboratory
- Present the proposal to a team of scientists
- Design and build the proposed self-driving laboratory at the AC training lab
- Provide a project update with proposed next steps
- Share the designs, data, and documentation publicly

### 🛠️ Competencies/Skills

- Scientific communication
- Systems design
- Dissemination
- Interdisciplinary teamwork

### 🧩 Modules

Module Name | Topics | Learning Outcomes
---- | ---- | ----
Project proposal | <ul><li>Figures</li><li>White papers</li><li>Presentations</li></ul> | <ul><li>Propose a self-driving lab via a schematic figure</li><li>Write a white paper for the self-driving laboratory</li><li>Present the proposal to a team of scientists</li></ul>
Design and build | <ul><li>SDL design</li><li>Implementation</li><li>Documentation</li></ul> | <ul><li>Design and build the proposed self-driving laboratory at the AC training lab</li><li>Provide a project update with proposed next steps</li></ul>
Dissemination | <ul><li>Project update</li><li>Knowledge sharing</li><li>Data and documentation</li></ul> | <ul><li>Share the designs, data, and documentation publicly</li></ul>
