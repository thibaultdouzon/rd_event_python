sed -E -i '' '/^\[localhost\]/d' /Users/thibaultdouzon/.ssh/known_hosts
docker run -it -p 8000:8000 -p 8022:22 tech_day_python