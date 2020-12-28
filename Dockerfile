FROM python:3.7 as build
RUN pip install stix-shifter
RUN git clone https://github.com/bioflash/stix-shifter && \
    cd stix-shifter && \
    git checkout story/stix-resilient && \
    export VERSION=1.0 && \
    export MODE=resilient && \
    python3 setup.py bdist_wheel

FROM python:3.7
RUN pip install stix-shifter
RUN pip install stix_shifter_utils
RUN pip install flask
COPY --from=build /stix-shifter/dist/ /stix-package
RUN pip install /stix-package/*
COPY app.py app.py
#CMD "python3 app.py"
ENTRYPOINT ["python3", "app.py"]