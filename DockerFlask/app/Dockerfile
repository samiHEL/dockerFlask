# Use an official Python runtime as an image
FROM python:3.6

# The EXPOSE instruction indicates the ports on which a container

# Sets the working directory for following COPY and CMD instructions
# Notice we haven’t created a directory by this name - this instruction
# creates a directory with this name if it doesn’t exist
WORKDIR /app
COPY /templates /app/templates/
COPY requirements.txt .
COPY app.py .
COPY app_test.py .
RUN python -m pip install --upgrade pip
RUN pip install --trusted-host pypi.org --trusted-host pypi.python.org --trusted-host=files.pythonhosted.org --no-cache-dir -r requirements.txt
RUN python3 -m unittest discover -p app_test.py
# Run app.py when the container launches
#COPY app_test.py /app
#RUN python -m unittest app_test.py
EXPOSE 5000
CMD python app.py
