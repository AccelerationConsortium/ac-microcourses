```{warning}
Recently, HiveMQ Cloud changed such that `hivemq-com-chain.der` (a Certificate Authority (CA) file) is not transferrable across different broker instances. The [latest `hivemq-com-chain.der` file](https://raw.githubusercontent.com/sparks-baird/self-driving-lab-demo/main/src/public_mqtt_sdl_demo/hivemq-com-chain.der) from [`self-driving-lab-demo`](https://github.com/sparks-baird/self-driving-lab-demo) will be hard-coded to the `self-driving-lab-demo` public test credentials (i.e., what is used in Module 1 - Running the Demo), so the *tutorials* should run without issue as long as you are using that file. However, the *assignment* requires you to have your own HiveMQ Cloud broker instance, so you will need to [generate a `hivemq-com-chain.der` file specific to your instance](https://colab.research.google.com/github/sparks-baird/self-driving-lab-demo/blob/main/notebooks/7.2.1-hivemq-openssl-certificate.ipynb) and upload it to your microcontroller in place of the default one.
```