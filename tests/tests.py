import os, sys 
sys.path.insert(0, os.path.abspath('../'))
import wavpy
import wavpy_sndf #use soundfile as a benchmark
import numpy as np
import numpy.testing as npt

test_wavs_dir = "../test_wavs/"
fListPCM = ["mono_16-bit_signed_PCM",
            "mono_24-bit_signed_PCM",
            "mono_32-bit_signed_PCM",
            "stereo_16-bit_signed_PCM",
            "stereo_24-bit_signed_PCM",
            "stereo_32-bit_signed_PCM",
            "4-chan_16-bit_signed_PCM",
            "4-chan_24-bit_signed_PCM",
            "4-chan_32-bit_signed_PCM"]

fListFLOAT32 = ["mono_32-bit_float",
                "stereo_32-bit_float",
                "4-chan_32-bit_float"]

fListIEEE = ["mono_32-bit_float",
             "stereo_32-bit_float",
             "mono_64-bit_float",
             "stereo_64-bit_float",
             "4-chan_32-bit_float",
             "4-chan_64-bit_float"]

for f in fListPCM:
    print("====================")
    print("Testing file : " + f)
    #compare wavread with wavpy and wavpy_sndf
    snd, fs, nbits = wavpy.wavread(test_wavs_dir+f+".wav")
    snd_sndf, fs_sndf, nbits_sndf = wavpy_sndf.wavread(test_wavs_dir+f+".wav")
    npt.assert_array_equal(snd, snd_sndf)
    npt.assert_equal(fs, fs_sndf)
    npt.assert_equal(nbits, nbits_sndf)

    #test writing
    wavpy.wavwrite(snd, fs, nbits, "wavpy.wav")
    wavpy_sndf.wavwrite(snd, fs, nbits, "wavpy_sndf.wav")
    snd1, fs1, nbits1 = wavpy_sndf.wavread("wavpy.wav")
    snd2, fs2, nbits2 = wavpy_sndf.wavread("wavpy_sndf.wav")
    npt.assert_array_equal(snd1, snd2)
    npt.assert_equal(fs1, fs2)
    npt.assert_equal(nbits1, nbits2)

for f in fListFLOAT32:
    print("====================")
    print("Testing file : " + f)
    #compare wavread with wavpy and wavpy_sndf
    snd, fs, nbits = wavpy.wavread(test_wavs_dir+f+".wav")
    snd_sndf, fs_sndf, nbits_sndf = wavpy_sndf.wavread(test_wavs_dir+f+".wav")
    npt.assert_array_equal(snd, snd_sndf)
    npt.assert_equal(fs, fs_sndf)
    npt.assert_equal(nbits, nbits_sndf)

    #test writing
    wavpy.wavwrite(snd, fs, nbits, "wavpy.wav")
    wavpy_sndf.wavwrite(snd, fs, nbits, "wavpy_sndf.wav")
    snd1, fs1, nbits1 = wavpy_sndf.wavread("wavpy.wav")
    snd2, fs2, nbits2 = wavpy_sndf.wavread("wavpy_sndf.wav")
    npt.assert_array_equal(snd1, snd2)
    npt.assert_equal(fs1, fs2)
    npt.assert_equal(nbits1, nbits2)

for f in fListIEEE:
    print("====================")
    print("Testing file : " + f)
    #compare wavread with wavpy and wavpy_sndf
    snd, fs, nbits = wavpy.wavread(test_wavs_dir+f+".wav")
    snd_sndf, fs_sndf, nbits_sndf = wavpy_sndf.wavread(test_wavs_dir+f+".wav")
    npt.assert_array_equal(snd, snd_sndf)
    npt.assert_equal(fs, fs_sndf)
    npt.assert_equal(nbits, nbits_sndf)

    #test writing
    wavpy.wavwrite(snd, fs, nbits, "wavpy.wav", wave_format="IEEE_FLOAT")
    wavpy_sndf.wavwrite(snd, fs, nbits, "wavpy_sndf.wav", wave_format="IEEE_FLOAT")
    snd1, fs1, nbits1 = wavpy_sndf.wavread("wavpy.wav")
    snd2, fs2, nbits2 = wavpy_sndf.wavread("wavpy_sndf.wav")
    npt.assert_array_equal(snd1, snd2)
    npt.assert_equal(fs1, fs2)
    npt.assert_equal(nbits1, nbits2)


         

os.remove("wavpy.wav")
os.remove("wavpy_sndf.wav")
