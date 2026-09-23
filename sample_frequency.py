sample_rate = 48000
frequency = 440

period_duration = 1 / frequency
samples_per_period = sample_rate / frequency

print("Frequency:", frequency, "Hz")
print("Period duration:", period_duration, "seconds")
print("Samples in one period:", samples_per_period)
