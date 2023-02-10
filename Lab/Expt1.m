//This code is not owned by me
clc
close all
clear all
I=imread("macro.jpg");
%I=imread("front cam.jpg");
%I=imread("main cam default.jpg");
%I=imread("front cam default.jpg");
imshow(I);
[m n z]=size(I);
qualityinMP=m*n/1000000
% Video
V = "20210204_102811.mp4"; %Video full fileName
v = VideoReader(V);
D=v.Duration;
FPS=v.FrameRate;
T =(round( D*FPS));
H=v.Height
W=v.Width
while hasFrame(v)
frame = readFrame(v);
imshow(frame);
drawnow
end
