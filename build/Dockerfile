
# ###############
# https://www.jeffgeerling.com/blog/2017/use-arg-dockerfile-dynamic-image-specification
ARG IMAGE_VERSION
FROM $IMAGE_VERSION

LABEL maintainer="Paolo D'Onorio De Meo <paolo@proofmedia.io>"

# ###############
RUN apk --no-cache update && \
    apk --no-cache upgrade && apk add \
    git \
    && rm -rf /var/cache/apk/*
# other packages:
# bash less vim git busybox-extras dumb-init

# ###############
# RUN mkdir /docker-entrypoint.d/
# COPY ./docker-entrypoint.sh /usr/local/bin/docker-entrypoint
# RUN chmod +x /usr/local/bin/*
# ENTRYPOINT ["/usr/bin/dumb-init", "--"]
# CMD ["docker-entrypoint"]

# ###############
COPY ./requirements.txt /tmp/requirements.txt
RUN pip install --upgrade -r /tmp/requirements.txt

# ###############
VOLUME /app
WORKDIR /app
CMD [ "sleep", "1234567890" ]
