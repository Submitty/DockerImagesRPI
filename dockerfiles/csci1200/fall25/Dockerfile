FROM ubuntu:22.04

ARG TARGETARCH

RUN apt-get update

RUN apt-get install -y python3
RUN apt-get install -y libpython3.10
RUN apt-get install -y python3-dev

RUN apt-get install -y clang lld lldb
RUN apt-get install -y gcc g++ 
RUN if [ $TARGETARCH = "amd64" ]; then apt-get install -y gdb; fi

RUN apt-get install -y xz-utils
RUN apt-get install -y curl

RUN apt-get install -y cmake
RUN apt-get install -y  make

RUN apt-get install -y --no-install-recommends wget ca-certificates rsync 

RUN apt-get install -y valgrind 
RUN apt-get install -y imagemagick 
RUN apt-get install -y wkhtmltopdf
RUN apt-get install -y xvfb 
RUN apt-get install -y time


# =====================================================
ENV DRMEMORY_TAG=release_2.6.0
ENV DRMEMORY_VERSION=2.6.0
ENV SUBMITTY_INSTALL_DIR=/usr/local/submitty
RUN apt-get update \
    && mkdir -p ${SUBMITTY_INSTALL_DIR}/drmemory \
    && cd /tmp \
    && wget https://github.com/DynamoRIO/drmemory/releases/download/${DRMEMORY_TAG}/DrMemory-Linux-${DRMEMORY_VERSION}.tar.gz \
    && tar -xpzf DrMemory-Linux-${DRMEMORY_VERSION}.tar.gz \
    && rsync --delete -a /tmp/DrMemory-Linux-${DRMEMORY_VERSION}/ ${SUBMITTY_INSTALL_DIR}/drmemory \
    && rm -rf /tmp/DrMemory* \
    && chown -R root ${SUBMITTY_INSTALL_DIR}/drmemory \
    && chmod -R 755 ${SUBMITTY_INSTALL_DIR}/drmemory 

# =====================================================
ENV AnalysisTools_Version=v.18.06.00
ENV SUBMITTY_INSTALL_DIR=/usr/local/submitty
RUN apt-get update \
    && mkdir -p ${SUBMITTY_INSTALL_DIR}/SubmittyAnalysisTools \
    && wget -nv "https://github.com/Submitty/AnalysisTools/releases/download/${AnalysisTools_Version}/count" -O ${SUBMITTY_INSTALL_DIR}/SubmittyAnalysisTools/count \
    && wget -nv "https://github.com/Submitty/AnalysisTools/releases/download/${AnalysisTools_Version}/plagiarism" -O ${SUBMITTY_INSTALL_DIR}/SubmittyAnalysisTools/plagiarism \
    && wget -nv "https://github.com/Submitty/AnalysisTools/releases/download/${AnalysisTools_Version}/diagnostics" -O ${SUBMITTY_INSTALL_DIR}/SubmittyAnalysisTools/diagnostics \
    && chmod -R 755 ${SUBMITTY_INSTALL_DIR}/SubmittyAnalysisTools 

# =====================================================
ENV AnalysisToolsTS_Version=v23.06.01
ENV SUBMITTY_INSTALL_DIR=/usr/local/submitty
RUN apt-get update \
    && mkdir -p ${SUBMITTY_INSTALL_DIR}/SubmittyAnalysisToolsTS/build \
    && wget -nv "https://github.com/Submitty/AnalysisToolsTS/releases/download/${AnalysisToolsTS_Version}/submitty_count_ts" -O ${SUBMITTY_INSTALL_DIR}/SubmittyAnalysisToolsTS/build/submitty_count_ts \
    && wget -nv "https://github.com/Submitty/AnalysisToolsTS/releases/download/${AnalysisToolsTS_Version}/submitty_diagnostics_ts" -O ${SUBMITTY_INSTALL_DIR}/SubmittyAnalysisToolsTS/build/submitty_diagnostics_ts \
    && chmod -R 755 ${SUBMITTY_INSTALL_DIR}/SubmittyAnalysisToolsTS 


# =====================================================
# cleanup
RUN rm -rf /var/lib/apt/lists/*

#start the container from bash
CMD [ “/bin/bash” ]
