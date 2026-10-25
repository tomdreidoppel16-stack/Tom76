FROM python:3.12-slim
ENV PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1
WORKDIR /srv
# ffmpeg: original MP4 rendering; font: clear German captions in generated shorts.
RUN apt-get update && apt-get install -y --no-install-recommends \
    ffmpeg fonts-dejavu-core ca-certificates \
    && rm -rf /var/lib/apt/lists/*
COPY requirements.txt /srv/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt \
    && useradd --system --uid 10001 tomgpt
COPY boot.py core_bundle.py /srv/
RUN python boot.py --extract --dest /srv \
    && mkdir -p /srv/data /srv/output /srv/super_output \
    && chown -R tomgpt:tomgpt /srv/data /srv/output /srv/super_output
USER tomgpt
ENV TOMGPT_HOST=0.0.0.0 PORT=8000 \
    TOMGPT_SUPERCORE_OUTPUT=/srv/super_output \
    TOMGPT_OUTPUT=/srv/output \
    TOMGPT_VIDEO_OUTPUT=/srv/data/videos
EXPOSE 8000
CMD ["python", "-m", "tomgpt.server"]
