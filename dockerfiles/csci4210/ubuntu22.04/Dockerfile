FROM ubuntu:22.04

# Install python3
RUN apt-get update \
    && apt-get -y --no-install-recommends install python3 \
    && rm -rf /var/lib/apt/lists/*

# Install Java 21
RUN apt-get update \
    && apt-get -y --no-install-recommends install openjdk-21-jdk \
    && rm -rf /var/lib/apt/lists/*

# Setup JAVA_HOME -- useful for docker commandline
ENV JAVA_HOME /usr/lib/jvm/java-21-openjdk-amd64/
RUN export JAVA_HOME

# Install C/C++
RUN apt-get update \
    && apt-get -y --no-install-recommends install gcc g++ \
    && rm -rf /var/lib/apt/lists/*

# Install Valgrind
RUN apt-get update \
    && apt-get -y --no-install-recommends install valgrind \
    && rm -rf /var/lib/apt/lists/*

# Install pip
RUN apt-get update \
    && apt-get -y --no-install-recommends install python3-pip \
    && rm -rf /var/lib/apt/lists/*

# Install numpy
RUN pip3 install numpy 

