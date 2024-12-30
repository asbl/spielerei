FROM golang:1.23-alpine
ARG HUGO_VERSION
ARG DART_SASS_VERSION
RUN apk add --no-cache git curl gcompat
RUN curl -LJO https://github.com/sass/dart-sass/releases/download/${DART_SASS_VERSION}/dart-sass-${DART_SASS_VERSION}-linux-x64.tar.gz
RUN tar -xf dart-sass-${DART_SASS_VERSION}-linux-x64.tar.gz
RUN cp -r dart-sass/* /usr/local/bin
RUN rm -rf dart-sass
RUN apk add --no-cache --repository=https://dl-cdn.alpinelinux.org/alpine/edge/community libstdc++
RUN curl -L "https://github.com/gohugoio/hugo/releases/download/v${HUGO_VERSION}/hugo_extended_${HUGO_VERSION}_Linux-64bit.tar.gz" -o hugo.tar.gz
RUN tar -xvzf hugo.tar.gz
RUN mv hugo /usr/local/bin/hugo
RUN hugo mod get
RUN hugo mod vendor
