FROM centos:latest
COPY Salary_Data.csv Salary_predictor.py ./
RUN yum update &&\
yum install python3 -y  &&\
pip3 install jupyter scikit-learn pandas numpy
