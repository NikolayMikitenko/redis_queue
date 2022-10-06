FROM continuumio/anaconda3

ADD environment.yml /tmp/environment.yml
RUN conda env create -n api -f /tmp/environment.yml

ENV PATH /opt/conda/envs/api/bin:$PATH

WORKDIR /app

COPY . .
 
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "80"]