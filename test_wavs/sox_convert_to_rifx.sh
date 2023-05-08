#! /bin/sh






sox 4-chan_16-bit_signed_PCM.wav -B 4-chan_16-bit_signed_PCM_RIFX.wav



sox mono_8-bit_unsigned_PCM.wav -B mono_8-bit_unsigned_PCM_RIFX.wav
sox mono_16-bit_signed_PCM.wav -B mono_16-bit_signed_PCM_RIFX.wav
sox mono_24-bit_signed_PCM.wav -B mono_24-bit_signed_PCM_RIFX.wav
sox mono_32-bit_signed_PCM.wav -B mono_32-bit_signed_PCM_RIFX.wav
sox mono_32-bit_float.wav -B mono_32-bit_float_RIFX.wav
sox mono_64-bit_float.wav -B mono_64-bit_float_RIFX.wav
sox mono_a-law.wav -B mono_a-law_RIFX.wav
sox mono_u-law.wav -B mono_u-law_RIFX.wav


sox stereo_8-bit_unsigned_PCM.wav -B stereo_8-bit_unsigned_PCM_RIFX.wav
sox stereo_16-bit_signed_PCM.wav -B stereo_16-bit_signed_PCM_RIFX.wav
sox stereo_24-bit_signed_PCM.wav -B stereo_24-bit_signed_PCM_RIFX.wav
sox stereo_32-bit_signed_PCM.wav -B stereo_32-bit_signed_PCM_RIFX.wav
sox stereo_32-bit_float.wav -B stereo_32-bit_float_RIFX.wav
sox stereo_64-bit_float.wav -B stereo_64-bit_float_RIFX.wav
sox stereo_a-law.wav -B stereo_a-law_RIFX.wav
sox stereo_u-law.wav -B stereo_u-law_RIFX.wav
