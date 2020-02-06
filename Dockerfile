FROM python:3

RUN pip install --upgrade pip && \
    pip install torch torchvision pillow pandas tqdm matplotlib
    
CMD echo "python /data/analyze.py <path to analyze>"
