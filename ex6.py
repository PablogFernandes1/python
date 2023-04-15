n1 = int(input('a distance in meters: '))

km = n1 / 1000
hm = n1 / 100
dam = n1 / 10
dm = n1 * 10
cm = n1 * 100
mm = n1 * 1000

print ('The measurement of {}km corresponds to: \n{}km \n{}hm \n{}dam \n{}dm \n{}cm \n{}mm '.format(n1, km, hm, dam, dm, cm, mm))