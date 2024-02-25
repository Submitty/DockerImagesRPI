FROM ubuntu:22.04

# Install python3
RUN apt-get update \
    && apt-get -y --no-install-recommends install python3 \
    && rm -rf /var/lib/apt/lists/*

# Install Java 21
RUN apt-get update \
    && apt-get -y --no-install-recommends install openjdk-21-jdk \
    && rm -rf /var/lib/apt/lists/*

# Install C/C++
RUN apt-get update \
    && apt-get -y --no-install-recommends install gcc g++ \
    && rm -rf /var/lib/apt/lists/*

