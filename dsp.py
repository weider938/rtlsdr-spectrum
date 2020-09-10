import numpy as np
import time
import math

def ReturnInvInt(my_int, step=13):
    if my_int == 0:
        return 0
    else:
        cel_part = my_int
        return_int = 0
        ost = -1
        ost_arr = []
        while cel_part != 1:
            ost = cel_part % 2
            cel_part = cel_part // 2
            ost_arr.append(ost)
        ost_arr.append(1)
        # print(ost_arr)  # ВВЕДЕННОЕ ЧИСЛО bin
        if len(ost_arr) < step:
            for _ in range(0, step - ((len(ost_arr)))):
                ost_arr.append(0)
        # print(ost_arr) # перевернутый массив и добавленные нули
        cnt = 1
        for y in ost_arr:
            if y == 1:
                greed_2 = len(ost_arr) - cnt
                return_int = return_int + 2 ** greed_2
            cnt = cnt + 1
        # print(return_int)
        return return_int

def GetArrayFFTIndexes(win, step):
    array_to_ret = []
    for i in range(0, win):
        index = ReturnInvInt(my_int=i, step=step)
        array_to_ret.append(index)
    return array_to_ret

def get_window(window, wind_var):
    # 1 - sinus
    # 2 - hann
    # 3 - hamming
    # 4 - blackman-harris
    # 5 - blackman-natoll

    function_windowed_array = []
    for i in range(0, window):
        if wind_var == 1:
            function_windowed_array.append(math.sin((np.pi * i) / (window - 1)))
        elif wind_var == 2:
            function_windowed_array.append(0.5 * (1 - math.cos((2 * np.pi * i) / (window - 1))))
        elif wind_var == 3:
            function_windowed_array.append(0.53836 - (0.46164 * math.cos((2 * np.pi * i) / (window - 1))))
        elif wind_var == 4:
            a0 = 0.35875
            a1 = 0.48829
            a2 = 0.14128
            a3 = 0.01168
            function_windowed_array.append(a0 - a1 * math.cos((2 * np.pi * i) / (window - 1))
                                              + a2 * math.cos((4 * np.pi * i) / (window - 1))
                                              - a3 * math.cos((6 * np.pi * i) / (window - 1)))
        elif wind_var == 5:
            a0 = 0.3635819
            a1 = 0.4891775
            a2 = 0.1365995
            a3 = 0.0106411
            function_windowed_array.append(a0 - a1 * math.cos((2 * np.pi * i) / (window - 1))
                                              + a2 * math.cos((4 * np.pi * i) / (window - 1))
                                              - a3 * math.cos((6 * np.pi * i) / (window - 1)))
    return function_windowed_array

def fast_ft(signal=None,
            window=None,):
    Spectrum_FFT = []
    for i in range(0, window):
        Spectrum_FFT.append(float(0))

    step = 0
    if window == 128:
        step = 7
    elif window == 256:
        step = 8
    elif window == 512:
        step = 9
    elif window == 1024:
        step = 10
    elif window == 2048:
        step = 11
    elif window == 4096:
        step = 12
    elif window == 8192:
        step = 13
    elif window == 16384:
        step = 14
    elif window == 32768:
        step = 15
    elif window == 65536:
        step = 16
    elif window == 131072:
        step = 17
    elif window == 262144:
        step = 18
    else:
        step = -1
        print("Значение окна должно быть кратно степени 2")
    if step != -1:
        mas_index = GetArrayFFTIndexes(win=window, step=step)
        for i in range(0, step):
            size_block = 2 * pow(2, i)
            count_block = int(window / size_block)
            for m in range(0, int(count_block)):
                for k in range(0, int(size_block / 2)):
                    if i == 0:
                        index_0 = int(mas_index[m * size_block])
                        index_1 = int(mas_index[m * size_block + int(size_block / 2)])
                        S_0 = complex((signal[index_0]).real, (signal[index_0]).imag)
                        S_1 = complex((signal[index_1]).real, (signal[index_1]).imag)

                        W = complex(math.cos((3.141592 * 2 / size_block) * k),
                                    math.sin((3.141592 * 2 / size_block) * k))

                        index_0 = int(m * size_block + k)
                        index_1 = int(m * size_block + (size_block / 2) + k)
                        Spectrum_FFT[index_0] = S_0 + W * S_1
                        Spectrum_FFT[index_1] = S_0 - W * S_1
                    else:
                        index_0 = int(m * size_block + k)
                        index_1 = int(m * size_block + (size_block / 2) + k)

                        S_0 = Spectrum_FFT[index_0]
                        S_1 = Spectrum_FFT[index_1]
                        W = complex(math.cos((3.141592 * 2 / size_block) * k),
                                    math.sin((3.141592 * 2 / size_block) * k))

                        Spectrum_FFT[index_0] = S_0 + W * S_1
                        Spectrum_FFT[index_1] = S_0 - W * S_1
        list_coef_abs = []
        for coef in Spectrum_FFT:
            z = complex((coef.real / window), (coef.imag / window))
            value = float("{0:.6f}".format(abs(z)))*10000
            list_coef_abs.append(value)
        return list_coef_abs[::-1]

def find_max(list):
    max_ = list[0]
    for i in list:
        if i > max_:
            max_ = i
    return max_

def mult_signal_on_sin(signal=None,
                            window=None,
                            harmonic=None,
                            samp_rate=None,):

    signal_shift = []
    carrier = ((window - harmonic) * samp_rate) / window

    step_t = float(1 / samp_rate)
    for i in range(0, window):
        cos_ = float(math.cos((2 * np.pi * carrier * step_t * i)))
        sin_ = float(math.sin((2 * np.pi * carrier * step_t * i)))
        point = complex(cos_, sin_)
        new_sample = point * signal[i]
        signal_shift.append(new_sample)
    return signal_shift

def mult_signals(signal1, signal2):

    result = []
    if len(signal1) == len(signal2):
        for i in range(len(signal1)):
            s = signal1[i] * signal2[i]
            result.append(s)
    return result

def make_average(list_samples):
    average_array = []
    for _ in range(len(list_samples[0])):
        average_array.append(0)
    for item in list_samples:
        average_array = average_array + item
    average_array = average_array / len(list_samples)
    return average_array