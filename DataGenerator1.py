
def DataGenerator(Key):

    import numpy as np

    if Key[1] == "A":
        alpha = 0

    omega_0 = int(Key[2]) * (np.pi / 30)
    theta = np.arange(0, ((int(Key[3])*360)+int(Key[3])))
    
    r = 25/1000

    if Key[4] == "E":
        r = 40/1000
    elif [4] == "S":
        r = 25/1000
    
    h = 70/1000  # mm, Distance between centre of rotation and origin
    b = 157/1000  # mm, Origin to slider track (sensor 2).
    c = 135/1000  # mm, Origin to sensor 1.

    omega = np.sqrt(omega_0**2 + 2 * alpha * theta)  # rad s^-1
    A = (r * np.sin(np.radians(theta + 180))) / (h - r * np.cos(np.radians(theta + 180)))
    XS1X = c * A
    XS2X = b * A
    XS1Y = -c + np.sqrt(c**2 - (c * A)**2)
    B = (h * np.cos(np.radians(theta)) + r) / ((h + r * np.cos(np.radians(theta)))**2)
    VS1X = -c * r * omega * B
    VS2X = -b * r * omega * B
    VS1Y = (np.gradient(XS1Y, theta)) * omega * (360 / (2 * np.pi))
    C = (h * (h - r * np.cos(np.radians(theta + 180)) + 2 * r * (h * np.cos(np.radians(theta + 180)) - r))) / ((h - r * np.cos(np.radians(theta + 180)))**3)
    AS1X = c * r * np.sin(np.radians(theta)) * C * omega**2
    AS2X = b * r * np.sin(np.radians(theta)) * C * omega**2
    AS1Y = (np.diff(VS1Y) / np.diff(theta)) * (omega[:-1] * (360 / (2 * np.pi)))

    # Function to pad with nan
    def pad_with_nan(v):
        return np.pad(v, (0, ((int(Key[3])*360)+int(Key[3])) - len(v)), 'constant', constant_values=np.nan)

    XS1X = pad_with_nan(XS1X)
    XS1Y = pad_with_nan(XS1Y)
    XS2X = pad_with_nan(XS2X)
    VS1X = pad_with_nan(VS1X)
    VS1Y = pad_with_nan(VS1Y)
    VS2X = pad_with_nan(VS2X)
    AS1X = pad_with_nan(AS1X)
    AS1Y = pad_with_nan(AS1Y)
    AS2X = pad_with_nan(AS2X)

    return theta, XS1X, XS1Y, XS2X, VS1X, VS1Y, VS2X, AS1X, AS1Y, AS2X

#Key = ["S", "A", "60", "2", "E"]
#theta, XS1X, XS1Y, XS2X, VS1X, VS1Y, VS2X, AS1X, AS1Y, AS2X = DataGenerator(Key)
