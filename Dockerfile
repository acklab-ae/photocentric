FROM python:3

RUN pip install --upgrade pip && \
    pip install torch torchvision pillow pandas tqdm matplotlib
    
CMD python /data/analyze.py
    

