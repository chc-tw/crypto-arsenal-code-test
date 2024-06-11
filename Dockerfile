FROM continuumio/miniconda3

COPY environment.yml .

RUN conda env create -f environment.yml

SHELL ["conda", "run", "-n", "code_test", "/bin/bash", "-c"]

ENV PATH /opt/conda/envs/code_test/bin:$PATH

RUN echo "conda activate code_test" >> ~/.bashrc

WORKDIR /app

COPY . .
