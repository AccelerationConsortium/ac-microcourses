```{warning}
Recently, HiveMQ Cloud changed such that `hivemq-com-chain.der` (a Certificate Authority (CA) file) is not transferrable across different broker instances. However, a **non-expiring certificate solution** is available using the intermediate certificate (ISRG Root X1) instead of the server-specific certificate.

A non-expiring, "root" certificate is contained in `sdl_demo.zip` packages [releases](https://github.com/sparks-baird/self-driving-lab-demo/releases) v0.8.13 and beyond [[colab](https://colab.research.google.com/gist/sgbaird/5ddef425e8d4aae454a69fbce8654faf/hivemq-root-cert.ipynb)]. You can also [generate a `hivemq-com-chain.der` certificate specific to your HiveMQ instance](https://colab.research.google.com/github/sparks-baird/self-driving-lab-demo/blob/main/notebooks/7.2.1-hivemq-openssl-certificate.ipynb). We recommend using the non-expiring, root certificate, which is applicable for all HiveMQ instances.
```
