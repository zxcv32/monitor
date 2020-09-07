#!/bin/bash
docker image rm monitor_nano:latest
docker-compose -p monitor down
docker-compose -p monitor up -d