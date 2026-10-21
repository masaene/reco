import cv2
import streamlit as st

video_path = './data/video.mp4'

cap = cv2.VideoCapture(video_path)
raw_video_data = open(video_path, 'rb')

st.video(raw_video_data)

