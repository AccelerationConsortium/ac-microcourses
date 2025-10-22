```{warning}
Recently, HiveMQ Cloud changed such that `hivemq-com-chain.der` (a Certificate Authority (CA) file) is not transferrable across different broker instances. However, a **non-expiring certificate solution** is now available using the intermediate certificate (ISRG Root X1) instead of the server-specific certificate.

For the *tutorials*, the [latest `hivemq-com-chain.der` file](https://raw.githubusercontent.com/sparks-baird/self-driving-lab-demo/main/src/public_mqtt_sdl_demo/hivemq-com-chain.der) from [`self-driving-lab-demo`](https://github.com/sparks-baird/self-driving-lab-demo) is hard-coded to the `self-driving-lab-demo` public test credentials (i.e., what is used in Module 1 - Running the Demo), so the tutorials should run without issue.

For the *assignment*, which requires you to have your own HiveMQ Cloud broker instance, you can [generate a non-expiring `hivemq-com-chain.der` file](https://colab.research.google.com/github/sparks-baird/self-driving-lab-demo/blob/main/notebooks/7.2.1-hivemq-openssl-certificate.ipynb) using the intermediate certificate. This certificate will work across different HiveMQ broker instances and won't expire like the previous server-specific certificates.
```
