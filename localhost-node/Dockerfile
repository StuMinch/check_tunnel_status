FROM node:latest
WORKDIR /opt
ADD ./* /opt
COPY ./* /opt
RUN npm install
EXPOSE 5000
CMD ["node", "app_v2.js"]