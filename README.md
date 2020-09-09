# Mildstone
Mildstone project home

Mildstone ( pietra tenera in italiano ) is a collection of software tools that aim at organizing a central repository for the configuration and maintainment of embedded CoDAS devices.
The primary goal of the project is to provide a place where harware design and software code meet together in a single uniform way.

Mildstone is currently supporting ESP development but more high level boards will be supported soon.


Configuring a new repository to start playing with such tools the process is relatively simple:

<pre>
git clone https://gitlab.igi.cnr.it/rigoni/mildstone.git
cd autoconf-bootstrap
./bootstrap
./configure --enable-kconfig
# enjoy
</pre>

