#!/bin/zsh
kubectl apply -f  appsecrets.yml 
kubectl apply -f  application.yml 
kubectl apply -f authdb.yml
kubectl apply -f guitardb.yml

