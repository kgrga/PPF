import matplotlib.pyplot as plt

m = float(input("Unesi masu: "))
F = float(input("Unesi silu: "))

t= range(0, 11, 1)


x = [(F/m)*(pow(s,2))/2 for s in t]

v = [(F/m)*s for s in t]

a = [F/m for s in t]


plt.figure(figsize=(12,8))

#x-t graf
plt.subplot(3,1,1)
plt.plot(t, x)
plt.xlabel("t (s)")
plt.ylabel("x (m)")
plt.title("x - t graf")
plt.grid()

#v-t graf
plt.subplot(3,1,2)
plt.plot(t, v)
plt.xlabel("t (s)")
plt.ylabel("v (m/s)")
plt.title("v - t graf")
plt.grid()

#a-t graf
plt.subplot(3,1,3)
plt.plot(t, a)
plt.xlabel("t (s)")
plt.ylabel("a (m/s²)")
plt.title("a - t graf")
plt.grid()

plt.tight_layout()
plt.show()