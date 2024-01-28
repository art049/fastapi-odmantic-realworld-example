FROM node

WORKDIR /realworld

RUN git clone https://github.com/gothinkster/realworld.git .

ENTRYPOINT [ "./api/run-api-tests.sh" ]
