FROM teamvaders/suparibot:latest

#clonning repo 
RUN git clone https://github.com/TheVaders/InVade.git /root/hellbot

#working directory 
WORKDIR /root/suparibot

# Install requirements
RUN pip3 install -U -r requirements.txt

ENV PATH="/home/userbot/bin:$PATH"

CMD ["python3","-m","suparibot"]
