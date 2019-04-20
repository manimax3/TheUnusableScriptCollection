#FROM tensorflow/tensorflow:1.13.0rc1-gpu-py3
FROM tensorflow/tensorflow:1.12.0-rc2-gpu-py3

# Python3
RUN apt-get install -y python3 python3-dev python3 python3-pip
RUN pip3 install pip --upgrade

ARG CONDA_VERSION=Anaconda3-4.4.0-Linux-x86_64.sh
ARG CONDA_PATH=/opt/conda
ARG USER=vizdoom


RUN apt-get update && apt-get install -y --fix-missing \
	build-essential \
	cmake \
	gfortran \
	git \
	wget \
	curl \
	graphicsmagick \
	libgraphicsmagick1-dev \
	libatlas-dev \
	libavcodec-dev \
	libavformat-dev \
	libgtk2.0-dev \
	libjpeg-dev \
	liblapack-dev \
	libswscale-dev \
	pkg-config \
	python3-dev \
	python3-numpy \
	software-properties-common \
	zip \
	&& apt-get clean && rm -rf /tmp/* /var/tmp/*

RUN cd ~ && \
	mkdir -p dlib && \
	git clone -b 'v19.9' --single-branch https://github.com/davisking/dlib.git dlib/ && \
	cd  dlib/ && \
	python3 setup.py install --yes USE_AVX_INSTRUCTIONS

RUN pip3 --no-cache-dir install \
	pygmo \
	Pillow \
	dlib \
	face-recognition \
	opencv-python \
	requests \
	inputs \
	moviepy








############################################
# ViZDoom
############################################

# ViZdoom dependencies
RUN apt-get update
RUN apt-get install -y \
    build-essential \
    bzip2 \
    cmake \
    curl \
    git \
    libboost-all-dev \
    libbz2-dev \
    libfluidsynth-dev \
    libfreetype6-dev \
    libgme-dev \
    libgtk2.0-dev \
    libjpeg-dev \
    libopenal-dev \
    libpng12-dev \
    libsdl2-dev \
    libwildmidi-dev \
    libzmq3-dev \
    nano \
    nasm \
    pkg-config \
    rsync \
    software-properties-common \
    sudo \
    tar \
    timidity \
    unzip \
    wget \
    zlib1g-dev

# Python3
RUN apt-get install -y python3-dev python3 python3-pip
RUN pip3 install pip --upgrade


# Enables X11 sharing and creates user home directory
ENV USER_NAME root
ENV HOME_DIR /home/$USER_NAME
#
# Replace HOST_UID/HOST_GUID with your user / group id (needed for X11)
ENV HOST_UID 1000
ENV HOST_GID 1000

#RUN export uid=${HOST_UID} gid=${HOST_GID} && \
#    mkdir -p ${HOME_DIR} && \
#    echo "$USER_NAME:x:${uid}:${gid}:$USER_NAME,,,:$HOME_DIR:/bin/bash" >> /etc/passwd && \
#    echo "$USER_NAME:x:${uid}:" >> /etc/group && \
#    echo "$USER_NAME ALL=(ALL) NOPASSWD: ALL" > /etc/sudoers.d/$USER_NAME && \
#    chmod 0440 /etc/sudoers.d/$USER_NAME && \
#    chown ${uid}:${gid} -R ${HOME_DIR}


#RUN git clone https://github.com/mwydmuch/ViZDoom ${HOME_DIR}/vizdoom
#RUN pip3 install ${HOME_DIR}/vizdoom

#USER ${USER_NAME}
#WORKDIR ${HOME_DIR}

RUN pip3 --no-cache-dir install vizdoom







############################################
# Roboschool
############################################
#RUN cd ~
#RUN apt-get update && apt-get install -y \
#      git cmake ffmpeg pkg-config \
#      qtbase5-dev libqt5opengl5-dev libassimp-dev \
#      libpython3.5-dev libboost-python-dev libtinyxml-dev


#ENV ROBOSCHOOL_PATH /opt/roboschool

#RUN mkdir -p /opt/bullet3/build \
#	&& cd /opt/bullet3/build \
#	&& cmake -DBUILD_SHARED_LIBS=ON -DUSE_DOUBLE_PRECISION=1 \
#	-DCMAKE_INSTALL_PREFIX:PATH=${ROBOSCHOOL_PATH}/roboschool/cpp-household/bullet_local_install \
#	-DBUILD_CPU_DEMOS=OFF -DBUILD_BULLET2_DEMOS=OFF \
#	-DBUILD_EXTRAS=OFF  -DBUILD_UNIT_TESTS=OFF \
#	-DBUILD_CLSOCKET=OFF -DBUILD_ENET=OFF \
#	-DBUILD_OPENGL3_DEMOS=OFF .. \
#	&& make \
#	&& make install \
#	&& pip3 install -e .\
#	&& ldconfig \
#	&& make clean


############################################
# marlo
############################################

#ENV MALMO_MINECRAFT_ROOT /opt/MalmoPlatform/Minecraft
#ENV MALMO_XSD_PATH /opt/MalmoPlatform/Schemas

#RUN pip3 install -U malmo
#RUN pip3 install -U marlo

#RUN cd /opt \
#	&& python -c 'import malmo.minecraftbootstrap; malmo.minecraftbootstrap.download()' \
#	&& chown -R user:user MalmoPlatform/




############################################
# pybullet
############################################
RUN pip3 --no-cache-dir install pybullet


############################################
# StarCraft II
############################################
RUN cd ~ && \
	git clone https://github.com/deepmind/pysc2.git && \
	pip3 --no-cache-dir install pysc2/


############################################
# Gym
############################################
RUN apt-get update && apt-get install -y \
	python3-dev zlib1g-dev libjpeg-dev cmake swig \
	python-pyglet python3-opengl libboost-all-dev libsdl2-dev \
	libosmesa6-dev patchelf ffmpeg xvfb

RUN pip3 --no-cache-dir install gym[atari]
RUN pip3 --no-cache-dir install gym[box2d]
RUN pip3 --no-cache-dir install gym[classic_control]
#RUN pip3 --no-cache-dir install gym[robotics]
RUN pip3 --no-cache-dir install gym[toy_text]


############################################
# Coach
############################################
RUN apt-get update && apt-get install -y --fix-missing \
	python3-pip cmake zlib1g-dev python3-tk python-opencv \
	libboost-all-dev \
	libblas-dev liblapack-dev libatlas-base-dev gfortran \
	libsdl-dev libsdl-image1.2-dev libsdl-mixer1.2-dev libsdl-ttf2.0-dev libsmpeg-dev libportmidi-dev libavformat-dev libswscale-dev \
	dpkg-dev build-essential python3.5-dev libjpeg-dev  libtiff-dev libsdl1.2-dev libnotify-dev freeglut3 freeglut3-dev libsm-dev libgtk2.0-dev libgtk-3-dev libwebkitgtk-dev libgtk-3-dev libwebkitgtk-3.0-dev libgstreamer-plugins-base1.0-dev \
	libav-tools libsdl2-dev swig cmake

RUN cd ~ && \
	git clone https://github.com/NervanaSystems/coach.git/ && \
	cd coach && \
	pip3 install -e .



############################################
# Baselines
############################################

RUN cd ~ && \
	git clone https://github.com/openai/baselines.git && \
	cd baselines && \
	pip3 install -e .

############################################
# Stable Baselines
############################################

RUN pip3 --no-cache-dir install \
	stable-baselines




