FROM python:3.6

MAINTAINER umemiya

ARG project_dir=/show_killme_image_api/

ADD requirements.txt $project_dir
ADD api.py $project_dir
ADD killme.py $project_dir

WORKDIR $project_dir
RUN pip install -r requirements.txt

CMD ["python","app.py"]