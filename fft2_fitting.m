im = fitsread("7793_subtracted.fits");
[M, N] = size(im);

TF = isnan(im);
im(TF) = 0;

fim = fft2(im,2^nextpow2(M),2^nextpow2(N));
figure;
imagesc(abs(log2(fftshift(fim))))

fim(1:11) = [];
power = abs(fim(1:floor(N/2))).^2;
%maxfreq = exp(6);
freq =(1:N/2)/(N/2);%*maxfreq;
x = log(freq);
y = log(power);

figure;
plot(x,y, '.-')

curveFitter(x,y);
