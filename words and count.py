def largest_word(sentence):
    splarray = sentence.split()
    countarr = [len(i) for i in splarray]


stri = "Hello how are you"
x = stri.split()
print(x)
lenarr = [len(i) for i in x]
print(lenarr)
arraylength = len(lenarr)
mergedarr = []
for i in range(arraylength):
    mergedarr.append((x[i], lenarr[i]))
print(mergedarr)

lar = 0
val = []
for i in range(len(mergedarr)):
    if mergedarr[i][1] > lar:
        lar = mergedarr[i][1]
        val = mergedarr[i]
print(mergedarr)
print(lar)
print(val)