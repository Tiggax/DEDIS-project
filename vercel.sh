#!/bin/bash
 
if [[ $VERCEL_ENV == "production"  ]] ; then
  poetry run setup_prod
else
  poetry run setup_prod
fi