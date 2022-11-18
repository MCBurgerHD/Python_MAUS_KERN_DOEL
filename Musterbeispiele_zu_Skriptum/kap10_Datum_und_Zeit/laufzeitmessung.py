import time, math

start = time.process_time()
# Berechnung zum sinnlosen Zeit Totschlagen
for i in range(1, 1000000): x = math.sin(i)
end = time.process_time()
print('Start:', start, 'End:', end, 'Differenz: ', end-start, 'Sekunden')
# Start: 0.078125 End: 0.734375 Differenz:  0.65625 Sekunden