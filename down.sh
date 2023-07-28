#!/bin/zsh
kubectl delete -f  appsecrets.yml
kubectl delete -f application.yml 
kubectl delete -f  authdb.yml
kubectl delete -f guitardb.yml

