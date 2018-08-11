# import wave
# import numpy as np
# import matplotlib.pyplot as plt
#
# # https://blog.csdn.net/qq_39516859/article/details/79903710
# filepath = "a.wav"
# f = wave.open(filepath, 'rb')
#
# params = f.getparams()
# nchannels, sampwidth, framerate, nframes = params[:4]
# strData = f.readframes(nframes)
# w = np.fromstring(strData, dtype=np.int16)
# w = w * 1.0 / (max(abs(w)))
# w = np.reshape(w, [nframes, nchannels])
# time = np.arange(0, nframes) * (1.0 / framerate)
#
# plt.figure()
# plt.subplot(5, 1, 1)
# plt.plot(time, w[:, 0])
# plt.xlabel("Time(s)")
# plt.title("First Channel")
# plt.savefig("a.png")
# plt.close()

import wave as we
import numpy as np
import matplotlib.pyplot as plt


def wavread(path):
    wavfile = we.open(path, "rb")
    params = wavfile.getparams()
    framesra, frameswav = params[2], params[3]
    datawav = wavfile.readframes(frameswav)
    wavfile.close()
    datause = np.fromstring(datawav, dtype=np.short)
    datause.shape = -1, 2
    datause = datause.T
    time = np.arange(0, frameswav) * (1.0 / framesra)
    return datause, time


def main():
    path = "a.wav"
    wavdata, wavtime = wavread(path)
    plt.title("Night.wav's Frames")
    plt.subplot(211)
    plt.plot(wavtime, wavdata[0], color='green')
    plt.subplot(212)
    plt.plot(wavtime, wavdata[1])
    plt.show()


main()