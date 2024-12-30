FROM golang:1.23-alpine
ARG HUGO_VERSION
ARG DART_SASS_VERSION
RUN apk add --no-cache git curl gcompat
RUN curl -LJO https://github.com/sass/dart-sass/releases/download/${DART_SASS_VERSION}/dart-sass-${DART_SASS_VERSION}-linux-x64.tar.gz
RUN tar -xf dart-sass-${DART_SASS_VERSION}-linux-x64.tar.gz
RUN cp -r dart-sass/* /usr/local/bin
RUN rm -rf dart-sass
RUN apk add --no-cache --repository=https://dl-cdn.alpinelinux.org/alpine/edge/community hugo
RUN hugo mod get
RUN hugo mod vendor
