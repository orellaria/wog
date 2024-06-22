From python 
WORKDIR /app
Copy . . 
run pip install requests
CMD ["python","main.py"]
EXPOSE 8080

