clc
clear
close all

open('graph0.fig')
h = findobj(gca,'Type','line');
%h = findobj(subplot(2,1,1),'Type','line');  % to receive data from 1st plot
x = h.XData;
y = h.YData;
%close all
% plot(x,y); % plots y(x)
dataArray = [x;y];
csvwrite('someData.csv', dataArray);