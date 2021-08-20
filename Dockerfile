FROM ubuntu:18.04

# Use bash to support string substitution.
SHELL ["/bin/bash", "-c"]

RUN apt-get update
RUN apt-get upgrade -y

RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y \
    build-essential \
    cmake \
    git \
    hmmer \
    kalign \
    tzdata \
    wget \
    sudo \
    && rm -rf /var/lib/apt/lists/*

RUN mkdir /app
RUN git clone https://github.com/zoohoson/AssemForU.git /app

RUN wget -q -P /tmp \
    https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh \
    && bash /tmp/Miniconda3-latest-Linux-x86_64.sh -b -p /opt/conda \
    && rm /tmp/Miniconda3-latest-Linux-x86_64.sh

# Install conda packages.
ENV PATH="/opt/conda/bin:$PATH"


RUN conda update -qy conda \
    && conda install -y -c conda-forge \